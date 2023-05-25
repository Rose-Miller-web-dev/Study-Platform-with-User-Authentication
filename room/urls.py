from django.urls import path
from . import views

urlpatterns = [
    path('roomlist/', views.roomlist, name="roomlist"),
    path('room_info/<str:pk>/', views.room_info, name="room_info"),
    path('delete-message/<str:pk>/', views.delete_, name="delete-message"),
    path('edit-message/<str:pk>/', views.edit_, name="edit-message"),
    path('profile/<str:pk>/', views.user_profile, name="profile"),
    path('roomlist/login/', views.roomlist_login, name="roomlist_login"),
]