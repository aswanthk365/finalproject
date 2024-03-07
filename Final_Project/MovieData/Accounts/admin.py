from django.contrib import admin
from Accounts.models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class AccountInline(admin.StackedInline):
    model   = Profile
    verbose_name = 'profile_image'
    verbose_name_plural = 'profile_images'

class CustomizesedUser(UserAdmin):
    inlines = (AccountInline,)
admin.site.unregister(User)
admin.site.register(User,CustomizesedUser)
admin.site.register(Profile)