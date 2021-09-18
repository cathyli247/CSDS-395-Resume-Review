from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('register/', views.RegisterView.as_view(), name="register"),
    path('login/', views.RegisterView.as_view(), name="login"),
]