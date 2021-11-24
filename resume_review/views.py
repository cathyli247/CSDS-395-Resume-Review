import logging
from datetime import datetime

from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect, FileResponse
from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import redirect, render
import pytz
# Create your views here.
from django.views import View
from django.views.generic import TemplateView

from resume_review import user_api
from resume_review.forms import RegisterForm, LoginForm, SearchForm, UserProfileForm, OrderDetailForm
from django.views.generic.edit import FormView

from resume_review.models import Account, Comment, Reviewer, Order
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

        user = User.objects.create_user(
            username=username, email=email, password=password)
        Account.objects.create(user=user)
        return super().form_valid(form)


class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = 'home/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        logout(self.request)
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


class HomePageView(FormView):
    template_name = "home.html"
    form_class = SearchForm
    success_url = '/home'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        reviewers = user_api.get_good_reviewer()
        for reviewer in reviewers:
            reviewer.rate = user_api.get_average_rating(reviewer)
            reviewer.save()

        context['reviewer'] = reviewers

        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        reviewers = context['reviewer']
        for reviewer in reviewers:
            reviewer.rate = user_api.get_average_rating(reviewer)
            reviewer.save()

        if not self.request.user.is_authenticated:
            return HttpResponseRedirect('/')
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form, **kwargs)
        else:
            return self.form_invalid(form)

    def form_valid(self, form, **kwargs):
        reviewer = Reviewer.objects.all()
        for r in reviewer:
            r.rate = user_api.get_average_rating(r)
            r.save()

        name = self.request.POST.get('name', '')
        reviewer = reviewer.filter(Q(account__first_name__contains=name) | Q(
            account__last_name__contains=name)) if name is not None else reviewer
        major = self.request.POST.get('major', '')
        reviewer = reviewer.filter(
            account__major=major) if major != 'All' else reviewer

        academic_standing = self.request.POST.get('academic_standing', '')
        reviewer = reviewer.filter(
            account__academic=academic_standing) if academic_standing != 'All' else reviewer

        price = self.request.POST.get('price', '')

        if(price == "1"):
            reviewer = reviewer.filter(price__lte=20)
        elif(price == "2"):
            reviewer = reviewer.filter(Q(price__gte=20) & Q(price__lte=50))
        elif(price == "3"):
            reviewer = reviewer.filter(
                Q(price__gte=50) & Q(price__lte=100))
        elif(price == "4"):
            reviewer = reviewer.filter(price__gte=100)

        data = self.get_context_data(**kwargs)
        data['reviewer'] = reviewer
        return render(self.request, 'home.html', data)

    def form_invalid(self, form):
        response = super().form_invalid(form)
        return response


class OrderPageView(TemplateView):
    template_name = "order.html"

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        if not self.request.user.is_authenticated:
            return HttpResponseRedirect('/')
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        current_account = user_api.get_account_by_user(user)
        user_order = Order.objects.filter(account=current_account)
        current_reviewer = user_api.get_reviewer_by_account(current_account)
        reviewer_order = Order.objects.filter(
            reviewer=current_reviewer) if current_reviewer is not None else None
        context['user_order'] = user_order
        context['reviewer_order'] = reviewer_order
        return context


class OrderDetailView(FormView):
    template_name = "order_detail.html"
    form_class = OrderDetailForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        order_id = self.request.GET.get('order_id')
        if not order_id:
            return context

        order = user_api.get_order(order_id)
        context['order'] = order
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        user = self.request.user
        button = self.request.POST.get('button', '')
        resume = self.request.FILES.get('resume', '')
        order_id = self.request.GET.get('order_id', '')
        order = user_api.get_order(order_id)
        account = Account.objects.get(user=user)
        if button == 'cancel':
            order.state = 'Rejected'
        elif button == 'complete':
            order.state = 'Completed'
        elif button == 'accept':
            order.state = 'Accepted'
        elif button == 'submit_rate':
            rate = self.request.POST.get('rate', '')
            comment = self.request.POST.get('comment', '')

            comment_obj = Comment.objects.create(reviewer=order.reviewer, rate=rate, create_at=datetime.now(
                pytz.timezone('US/Eastern')), account=account)
            print(comment_obj.create_at)
            if comment:
                comment_obj.comment = comment
                comment_obj.save()

        if button == 'download':
            filepath = order.resume.path
            response = FileResponse(open(filepath, 'rb'))
            return response
        if resume and button == 'upload':
            order.resume = resume
        order.save()
        logger.info('save resume to order %s with action %s' %
                    (order.id, button))
        return HttpResponseRedirect(self.request.path_info + '?order_id=' + order_id)


class ReviewerCardView(TemplateView):
    template_name = "reviewer_card.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        reviewer_id = self.request.GET.get('reviewer_id')
        if not reviewer_id:
            return context

        reviewers = Reviewer.objects.filter(id=reviewer_id)
        context['reviewer'] = reviewers[0] if len(reviewers) is not 0 else None
        context['rating'] = user_api.get_average_rating(reviewers[0])
        comments = Comment.objects.filter(reviewer=reviewers[0])
        context['comments'] = comments
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        if not self.request.user.is_authenticated:
            return HttpResponseRedirect('/')
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        print(self.request.POST)
        button = self.request.POST.get('button', '')
        if button == "true":
            current_user = self.request.user
            reviewer_id = self.request.GET['reviewer_id']
            current_reviewer = Reviewer.objects.filter(id=reviewer_id)[0]
            current_account = user_api.get_account_by_user(current_user)
            new_order = Order.objects.create(state='Pending', account=current_account,
                                             reviewer=current_reviewer)
            new_id = new_order.id
            # http://127.0.0.1:8000/order_detail/?order_id=2
            return redirect('http://127.0.0.1:8000/order_detail/?order_id=' + str(new_id))
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)


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
            context['delivery_time'] = ''
        else:
            context['self_intro'] = reviewer.self_intro
            context['reviewer'] = 'true'
            context['price'] = reviewer.price
            context['delivery_time'] = reviewer.delivery_time
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        if not self.request.user.is_authenticated:
            return HttpResponseRedirect('/')
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
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
        delivery_time = self.request.POST.get('delivery_time', '')

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

        reviewer = user_api.get_reviewer_by_account(account=account)
        if reviewer:
            reviewer.self_intro = self_intro
            reviewer.price = price
            reviewer.delivery_time = delivery_time
            reviewer.save()
            logger.info('save reviewer info %s' % user)
        return super().form_valid(form)

    def form_invalid(self, form):
        response = super().form_invalid(form)
        return response
