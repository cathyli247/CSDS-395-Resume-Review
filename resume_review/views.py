import logging

from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import View
from django.views.generic import TemplateView

from resume_review import user_api
from resume_review.forms import RegisterForm, LoginForm, UserProfileForm
from django.views.generic.edit import FormView

from resume_review.models import Account

logger = logging.getLogger(__name__)


class RegisterView(FormView):
    template_name = 'register.html'
    form_class = RegisterForm
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        username = self.request.POST.get('username', '')
        email = self.request.POST.get('email', '')
        password = self.request.POST.get('password1', '')

        User.objects.create_user(username=username, email=email, password=password)
        return super().form_valid(form)

class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = '/home'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        username = self.request.POST.get('username')
        password = self.request.POST.get('password')
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return super().form_valid(form)


class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class OrderPageView(TemplateView):
    template_name = "order.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class UserProfileView(FormView):
    template_name = 'user_profile.html'
    form_class = UserProfileForm
    success_url = '/user_profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['user_name'] = user.username if user.is_authenticated else None
        context['email'] = user.email if user.is_authenticated else None
        context['account'] = user_api.get_account_by_user(user)
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        first_name = self.request.POST.get('first_name', '')
        last_name = self.request.POST.get('last_name', '')
        email = self.request.POST.get('email', '')
        phone_number = self.request.POST.get('phone_number', '')
        major = self.request.POST.get('major', '')
        academic_standing = self.request.POST.get('academic_standing', '')

        user = self.request.user
        user.email = email
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        logger.info('save user info %s' % user)

        account,_ = Account.objects.get_or_create(user=user)
        account.first_name = first_name
        account.last_name = last_name
        account.phone = phone_number
        account.major = major
        account.academic = academic_standing
        account.save()
        logger.info('save account info %s' % user)
        response = super().form_valid(form)
        return response

    def form_invalid(self, form):
        response = super().form_invalid(form)
        return response
