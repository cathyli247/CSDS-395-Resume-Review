from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name="register"),
    path('login/', views.LoginView.as_view(), name="login"),
    path('home/', views.HomePageView.as_view(), name='home'),
    path('', views.BaseView.as_view(), name='base'),
    path('order/', views.OrderPageView.as_view(), name='order'),
    path('order_detail/', views.OrderDetailView.as_view(), name='order_detail'),
    path('user_profile/', views.UserProfileView.as_view(), name='user_profile'),
    path('reviewer_profile/', views.ReviewerCardView.as_view(),
         name='reviewer_profile'),
]
