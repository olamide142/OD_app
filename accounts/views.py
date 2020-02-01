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

@login_required()
def profile(request, username):
	profile = Diary.objects.get(owner__username=username)
	posts = Post.objects.filter(diary_id = profile.id)
	am_following = list(Follower.objects.filter(follower_id=profile.id))
	following_me = list(Follower.objects.filter(following_id=profile.id))

	context = {'profile':profile, 'posts':posts, 'am_following':am_following,  'following_me':following_me,}
	return render(request, 'accounts/profile.html', context)


def loginPage(request):
	form = CreateUserForm()
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		print(username)
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
	return_list = json.dumps(am_following)
	return HttpResponse(
		json.dumps(am_following),
		content_type="application/json"
	)
