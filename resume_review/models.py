from datetime import datetime

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Account(models.Model):
    FRESHMEN = 'F'
    SOPHOMORE = 'S'
    JUNIOR = 'J'
    SENIOR = 'C'
    GRADUTAE = 'G'

    ACADEMIC_STANDING = [
        (FRESHMEN, 'Freshmen'),
        (SOPHOMORE, 'Sophomore'),
        (JUNIOR, 'Junior'),
        (SENIOR, 'Senior'),
        (GRADUTAE, 'Graduate'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    major = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    academic = models.CharField(
        max_length=1, choices=ACADEMIC_STANDING)
    phone = models.CharField(max_length=12)
    create_at = models.DateField(auto_now=True)


class Reviewer(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    # maxprice 9999.99
    price = models.DecimalField(max_digits=6, decimal_places=2)
    specialized_field = models.CharField(max_length=255)
    self_intro = models.TextField()
    comment = models.TextField(null=True)
    rate = models.SmallIntegerField(null=True)


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
    order_id = models.CharField(null=False, max_length=150, default='')
    create_at = models.DateTimeField(null=False, default=datetime.now())
    finished_at = models.DateTimeField(null=False, default=datetime.now())
    state = models.CharField(
        max_length=1, choices=Order_State)
    resume = models.TextField(null=True)


class Chat(models.Model):
    account = models.ForeignKey(Account, on_delete=models.PROTECT)
    reviewer = models.ForeignKey(Reviewer, on_delete=models.PROTECT)
    content = models.TextField(null=True)
