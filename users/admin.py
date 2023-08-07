from django.contrib import admin

from users.models import UserProfile

class UserProfileInline(admin.StackedInline):
    model = UserProfile