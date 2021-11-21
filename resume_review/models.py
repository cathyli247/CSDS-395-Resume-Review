from datetime import datetime, timedelta

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.utils import timezone

from resume_review import source_api
from datetime import datetime


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
        upload_to='profile_pic', null=True, default='user.png')


class Reviewer(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    # maxprice 9999.99
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    specialized_field = models.CharField(max_length=255)
    self_intro = models.TextField()
<<<<<<< HEAD
    delivery_time = models.DateTimeField(null=False, default=timezone.now)

    def get_name(self):
        return self.account.first_name


=======
    DELIVERY_TIME_CHOICES = [
        ('delivery_1', 'One week'),
        ('delivery_2', 'Two weeks'),
        ('delivery_3', 'Three weeks'),
        ('delivery_4', 'Four weeks or more'),
    ]
    delivery_time = models.CharField(
        max_length=255, choices=DELIVERY_TIME_CHOICES, default='delivery_1')
        
>>>>>>> 8ca2a9230c30bf349ef37384f299e4434e7d0d7c
class Comment(models.Model):
    reviewer = models.ForeignKey(Reviewer, on_delete=models.CASCADE)
    rate = models.CharField(max_length=255)
    comment = models.TextField(null=True)
    create_at = models.DateTimeField(null=False, default=timezone.now)


class Order(models.Model):
    PENDING = 'Pending'
    ACCEPT = 'Accepted'
    REJECT = 'Rejected'
    COMPLETE = 'Completed'

    Order_State = [
        (PENDING, 'Pending'),
        (ACCEPT, 'Accepted'),
        (REJECT, 'Rejected'),
        (COMPLETE, 'Completed'),
    ]
    account = models.ForeignKey(Account, on_delete=models.PROTECT)
    reviewer = models.ForeignKey(Reviewer, on_delete=models.PROTECT)
    create_at = models.DateTimeField(null=False, default=timezone.now)
    finished_at = models.DateTimeField(null=True, default=None)
    state = models.CharField(
        max_length=100, choices=Order_State, default=PENDING)
    resume = models.FileField(upload_to='resumes', null=True)


class Room(models.Model):
    name = models.CharField(max_length=1000)
    account = models.ForeignKey(Account, on_delete=models.PROJECT)
    reviewer = models.ForeignKey(Reviewer, on_delete=models.PROTECT)


class Message(models.Model):
    value = models.CharField(max_length=1000)
    date = models.DateTimeField(default=datetime.now, blank=True)
    account = models.ForeignKey(Account, on_delete=models.PROTECT)
    room = models.ForeignKey(Room, on_delete=models.PROTECT)
