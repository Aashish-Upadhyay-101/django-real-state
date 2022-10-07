from email.policy import default
from sqlite3 import Time
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _  

from apps.common.models import TimeStampedUUIDModel


class Enquiry(TimeStampedUUIDModel):
    name = models.CharField(verbose_name=_("Your name"), max_length=100)
    phone_number = PhoneNumberField(verbose_name=_("Phone number"), max_length=20, default="+1987654321")
    email =  models.EmailField(verbose_name=_("Email"))
    subject = models.CharField(verbose_name=_("Subject"), max_length=100)
    message = models.CharField(verbose_name=_("Message"), max_length=500)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name_plural = "Enquires"
