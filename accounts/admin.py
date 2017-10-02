from django.contrib import admin

from accounts.models import UserProfile, Friend

admin.site.register(UserProfile)
admin.site.register(Friend)
