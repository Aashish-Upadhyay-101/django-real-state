from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Profile


class ProfileAdmin(ModelAdmin):
    list_display = ["id", "pkid", "gender", "user", "phone_number", "country", "city"]
    list_filter = ["gender", "country", "city"]
    list_display_links = ["id", "pkid", "user"]


admin.site.register(Profile, ProfileAdmin)
