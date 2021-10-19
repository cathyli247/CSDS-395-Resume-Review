from datetime import datetime, timedelta

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.utils import timezone

from resume_review import source_api


class Account(models.Model):
    FRESHMEN = 'Freshmen'
    SOPHOMORE = 'Sophomore'
    JUNIOR = 'Junior'
    SENIOR = 'Senior'
    GRADUATE = 'Graduate'

    ACADEMIC_STANDING = [
        (FRESHMEN, 'Freshmen'),
        (SOPHOMORE, 'Sophomore'),
        (JUNIOR, 'Junior'),
        (SENIOR, 'Senior'),
        (GRADUATE, 'Graduate'),
    ]

    MAJOR = source_api.get_major_list()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    major = models.CharField(max_length=255, choices=MAJOR)
    academic = models.CharField(
        max_length=255, choices=ACADEMIC_STANDING)
    phone = models.CharField(max_length=12)
    create_at = models.DateField(auto_now=True)
    avatar = models.ImageField(
        upload_to='profile_pic', null=True, default='uaddsser.png')


class Reviewer(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    # maxprice 9999.99
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    specialized_field = models.CharField(max_length=255)
    self_intro = models.TextField()
    delivery_time = models.DateTimeField(null=False, default=timezone.now)


class Comment(models.Model):
    reviewer = models.ForeignKey(Reviewer, on_delete=models.CASCADE)
    rate = models.CharField(max_length=255)
    comment = models.TextField(null=True)
    create_at = models.DateTimeField(null=False, default=timezone.now)


class Order(models.Model):
    PENDING = 'P'
    ACCEPT = 'A'
    REJECT = 'R'
    COMPLETE = 'D'

    Order_State = [
        (PENDING, 'Pending'),
        (ACCEPT, 'Accept'),
        (REJECT, 'Reject'),
        (COMPLETE, 'Complete'),
    ]
    account = models.ForeignKey(Account, on_delete=models.PROTECT)
    reviewer = models.ForeignKey(Reviewer, on_delete=models.PROTECT)
    create_at = models.DateTimeField(null=False, default=timezone.now)
    finished_at = models.DateTimeField(null=False, default=timezone.now)
    state = models.CharField(
        max_length=1, choices=Order_State)
    resume = models.TextField(null=True)


class Chat(models.Model):
    account = models.ForeignKey(Account, on_delete=models.PROTECT)
    reviewer = models.ForeignKey(Reviewer, on_delete=models.PROTECT)
    content = models.TextField(null=True)
