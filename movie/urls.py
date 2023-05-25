from django.urls import path
from . import views

urlpatterns = [
    path('cast/', views.cast, name="cast"),
    path('movielogin/', views.loginUser, name="movieLogin"),
    path('useful/', views.logoutUser, name="movieLogout"),
    path('signup/', views.signupUser, name="signup"),
]