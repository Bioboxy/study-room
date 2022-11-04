from django.urls import path ## as an alternative use path instead of url import

from django.conf.urls import url
from . import views    #since same folder, use the dot


urlpatterns = [
	path(r'login/', views.loginPage, name = 'login'),
	path(r'logout/', views.logoutUser, name = 'logout'),
	path(r'register/', views.registerUser, name = 'register'),
	path(r'', views.home, name = 'home'),
	path(r'profile/<str:pk>/', views.userProfile, name = 'profile'),
	path(r'room/<str:pk>/', views.room, name = 'room'), #url didn't work here...
	path(r'create-room/', views.createRoom, name = 'createroom'),
	path(r'update-room/<str:pk>/', views.updateRoom, name = 'updateroom'),
	path(r'delete-room/<str:pk>/', views.deleteRoom, name = 'deleteroom'),
	path(r'delete-message/<str:pk>/', views.deleteMessage, name = 'deletemessage'),


]