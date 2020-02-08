from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.paginator import Paginator

from django.contrib.auth.models import User
from django.http import JsonResponse


# Create your views here.

from .models import *
from .forms import *
import json



@login_required(login_url='welcome')
def home(request):
	return render(request, 'accounts/home.html')

def welcome(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		return render(request, 'accounts/welcome.html')



def loginPage(request):
	print(request.POST)
	form = CreateUserForm()
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('home')
		else:
			messages.info(request, 'Username OR password is incorrect')
	else:
		return redirect('welcome')
	context = {'form':form}
	return render(request, 'accounts/welcome.html', context)

def registerPage(request):
	form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			form.save()
			user = form.cleaned_data.get('username')
			messages.success(request, 'Account was created for ' + user)
			messages.success(request, 'Log in with your username and password')
			allocate_diary_to_new_user(user)
			return redirect('login')
	else:
		return redirect('welcome')
	context = {'form':form}
	return render(request, 'accounts/welcome.html', context)

def allocate_diary_to_new_user(username):
	user = User.objects.get(username=username)
	diary = Diary.objects.create(diary_id= randomId(), owner=user, about_me="")
	diary.save()

def logoutUser(request):
	logout(request)
	return redirect('welcome')






def chatMessages(request):
	context = {}
	return render(request, 'accounts/message.html', context)


@login_required(login_url='welcome')
def profile(request, username):
	profile = Diary.objects.get(owner__username=username)
	posts = Post.objects.filter(diary_id=profile.id).order_by('-date_created')

	am_f = list(Follower.objects.filter(follower_id=profile.id))
	# To convert the query list from
	# <Follower: xlamide follows bolanle>, <Follower: xlamide follows django>
	# to ['bolanle', 'django']
	am_following = []
	for a in am_f:
		txt = str(a)
		x = txt.split(" ")
		am_following.append(x[2])

	f_me = list(Follower.objects.filter(following_id=profile.id))
	# To convert the query list from
	# <Follower: xlamide follows django>, <Follower: lams follows django>
	# to ['xalmide', 'lams']
	following_me = []
	for f in f_me:
		txt = str(f)
		x = txt.find("follows")
		following_me.append(txt[0:x].strip())

	context = {'profile': profile, 'posts': posts, 'am_following': am_following, 'following_me': following_me, }

	return render(request, 'accounts/profile.html', context)


@login_required(login_url='welcome')
def notification(request):
	# get current users notification
	diary = Diary.objects.get(owner__username=request.user.username)

	new_notifications = [] #empty list incase to new notification
	if diary.num_notification > 0:
		# Query Notication based on the last n (dairy.notification) notications of a particular diary
		new_notifications = Notification.objects.filter(owner=diary).order_by('-date_created')[:diary.num_notification]

	notifications = Notification.objects.filter(owner=diary).order_by('date_created').reverse()
	diary.num_notification = 0 #Reset the no. of notifications to 0 siince the notication logo has been clicked

	context = {'new_notifications': new_notifications,'notifications':notifications}
	return render(request, 'accounts/notification.html', context)


@login_required(login_url='welcome')
def update_nav(request):
	# get current users notification
	diary = Diary.objects.get(owner__username=request.user.username)
	if diary.num_notification > 0:
		data = {'notification': diary.num_notification}
	return JsonResponse(data)











###################   Ajax    ###################
def validate_username(request):
	username = request.GET.get('username', None)
	data = {
		'is_taken': User.objects.filter(username__iexact=username).exists()
	}

	return JsonResponse(data)

def get_follows(request):
	username = request.GET.get('username', None)
	type = request.GET.get('type', None)
	page = request.GET.get('page')

	profile = Diary.objects.get(owner__username=username)
	am_following = list(Follower.objects.filter(follower_id=profile.id))
	following_me = list(Follower.objects.filter(following_id=profile.id))

# using the Paginator class to state pagination
# 	if type == "following":
# 		pag = Paginator(am_following, 2)
# 	else:
# 		pag = Paginator(following_me, 2)
#
# 	return_list = pag.page(int(page)).object_list
# 	print(return_list)
#
# 	 # response json data
# 	data = {
# 		'return_list' : return_list,
# 	}



def addNote(request):
	if request.method == "POST":
		note = request.POST.get('note')
		user = User.objects.get(username=request.user.username)

		diary = Diary.objects.get(owner=user)
		post = Post.objects.create(post_id=randomId(), diary=diary, body=note)
		post.save()
		print(post)

		data = {
			'stat': "Success",
			'post_id':post.post_id
		}
	return JsonResponse(data)


def deleteNote(request):
	print("YOUR CODE MADE IT HERE HURRAY")
	if request.method == "POST":
		note_id = request.POST.get('note_id')
		user = User.objects.get(username=request.user.username)

		diary = Diary.objects.get(owner=user)
		post = Post.objects.get(post_id=note_id, diary=diary)
		post.delete()
		print(post)

		data = {
			'stat': "Success",
		}
	return JsonResponse(data)


def follow(request):
	if request.method == "POST":
		if request.POST.get('following') != request.user.username:
			if request.POST.get('action') == 'Follow':
				print("HERE1")
				follower = Diary.objects.get(owner__username=request.user.username)
				following = Diary.objects.get(owner__username=request.POST.get('following'))
				follow = Follower.objects.create(follower=follower, following=following, status="%s follows %s"%(follower, following))
				follow.save()
			elif request.POST.get('action') == 'Unfollow':
				follower = Diary.objects.get(owner__username=request.user.username)
				following = Diary.objects.get(owner__username=request.POST.get('following'))
				follow = Follower.objects.get(follower=follower, following=following,status="%s follows %s" % (follower, following))
				follow.delete()
			data = {
				'stat':"Success",
			}
		else:
			data = {
				'stat':"You can't Follow Yourself"
			}

	return JsonResponse(data)
