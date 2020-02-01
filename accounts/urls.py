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

    path('user/<str:username>', views.profile, name='profile'),
]
