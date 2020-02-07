from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('welcome/', views.welcome, name="welcome"),

    
    path('login/', views.loginPage, name="login"),
    path('register/', views.registerPage, name="register"),
    path('logout/', views.logoutUser, name="logout"),

    # ajax
    path('validate_username/', views.validate_username, name='validate_username'),
    path('get_follows/', views.get_follows, name='get_follows'),
    path('ajax/update_navbar/', views.update_navbar, name='update_navbar'),
    path('ajax/addNote/', views.addNote, name='addNote'),
    path('ajax/deleteNote/', views.deleteNote, name='deleteNote'),

    path('user/<str:username>', views.profile, name='profile'),
    path('notification/', views.notification, name='notification'),
    path('messages/', views.chatMessages, name='chatMessages'),
]
