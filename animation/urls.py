from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('signup/', views.signupUser, name="signup"),
    path('', views.home, name="home"),
    path('animations/', views.animations, name='animations'),
    path('animations/<str:pk>/', views.info, name="info"),
    path('animations/edit/<str:pk>/', views.edit, name="edit"),
    path('animations/delete/<str:pk>/', views.delete, name="delete"),
    path('animation/create/', views.create, name="create"),
    
]