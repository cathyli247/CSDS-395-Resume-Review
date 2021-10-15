import logging

from django.db.models import Q
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import redirect, render

# Create your views here.
from django.views import View
from django.views.generic import TemplateView

from resume_review import user_api
from resume_review.forms import RegisterForm, LoginForm, SearchForm, UserProfileForm
from django.views.generic.edit import FormView

from resume_review.models import Account, Comment, Reviewer
from resume_review.models import Account, Reviewer
from django.urls import reverse

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

        User.objects.create_user(
            username=username, email=email, password=password)
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
    form_class = SearchForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviewer'] = user_api.get_good_reviewer()
        return context

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        reviewer = Reviewer.objects.all()
        name = self.request.POST.get('name', '')
        reviewer = reviewer.filter(Q(account__first_name__contains=name) | Q(
            account__last_name__contains=name)) if name is not None else reviewer
        major = self.request.POST.get('major', '')
        reviewer = reviewer.filter(
            account__major=major) if major is not None else reviewer

        academic_standing = self.request.POST.get('academic_standing', '')
        reviewer = reviewer.filter(
            account__academic=academic_standing) if academic_standing is not None else reviewer

        price = self.request.POST.get('price', '')
        reviewer = reviewer.filter(
            price__gte=price) if price is not None else reviewer

        return redirect(reverse('home', kwargs={"reviewer": reviewer}))

    def form_invalid(self, form):
        response = super().form_invalid(form)
        return response


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
        account = user_api.get_account_by_user(user)
        reviewer = user_api.get_reviewer_by_account(account)
        if not reviewer:
            context['self_intro'] = ''
            context['reviewer'] = 'false'
            context['price'] = ''
        else:
            context['self_intro'] = reviewer.self_intro
            context['reviewer'] = 'true'
            context['price'] = reviewer.price
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        print(self.request.POST)
        if self.request.POST.get('unlock', '') == 'true':
            account = user_api.get_account_by_user(user=self.request.user)
            reviewer, _ = Reviewer.objects.get_or_create(account=account)
            return HttpResponseRedirect(self.get_success_url())

        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        first_name = self.request.POST.get('first_name', '')
        last_name = self.request.POST.get('last_name', '')
        phone_number = self.request.POST.get('phone_number', '')
        major = self.request.POST.get('major', '')
        academic_standing = self.request.POST.get('academic_standing', '')
        avatar = self.request.FILES.get('avatar', '')
        self_intro = self.request.POST.get('self_intro', '')
        price = self.request.POST.get('price', '')

        user = self.request.user
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        logger.info('save user info %s' % user)

        account, _ = Account.objects.get_or_create(user=user)
        account.first_name = first_name
        account.last_name = last_name
        account.phone = phone_number
        account.major = major
        account.academic = academic_standing
        if avatar:
            account.avatar = avatar
        account.save()
        logger.info('save account info %s' % user)
        response = super().form_valid(form)

        reviewer = user_api.get_reviewer_by_account(account=account)
        if reviewer:
            reviewer.self_intro = self_intro
            reviewer.price = price
            reviewer.save()
            logger.info('save reviewer info %s' % user)
        return response

    def form_invalid(self, form):
        response = super().form_invalid(form)
        return response
