from django.contrib import admin
from .models import Account, Reviewer, Room, Message

# Register your models here.

admin.site.register(Room)
admin.site.register(Message)
admin.site.register(Account)
admin.site.register(Reviewer)
