from django.contrib import admin
from .models import Enquiry


class EnquiryAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "message", "phone_number", "subject"]


admin.site.register(Enquiry, EnquiryAdmin)
