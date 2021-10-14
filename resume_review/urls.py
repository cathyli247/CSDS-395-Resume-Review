from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name="register"),
    path('', views.LoginView.as_view(), name="login"),
    path('home/', views.HomePageView.as_view(), name='home'),
    path('order/', views.OrderPageView.as_view(), name='order'),
    path('userorderdetail/', views.UserOrderDetailView.as_view(), name='userorderdetail'),
    path('user_profile/', views.UserProfileView.as_view(), name='user_profile'),

]