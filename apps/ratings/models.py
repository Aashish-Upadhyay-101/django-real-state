from django.db import models
from django.utils.translation import gettext_lazy as _
from real_estate.settings.base import AUTH_USER_MODEL
from apps.common.models import TimeStampedUUIDModel
from apps.profiles.models import Profile


class Range(models.IntegerChoices):
    RATING_1 = 1, _("Poor")
    RATING_2 = 2, _("Fair")
    RATING_3 = 3, _("Good")
    RATING_4 = 4, _("Very Good")
    RATING_5 = 5, _("Excellent")


class Rating(TimeStampedUUIDModel):
    rater = models.ForeignKey(
        AUTH_USER_MODEL,
        verbose_name=_("User Providing the Rating"),
        related_name="rating",
        on_delete=models.SET_NULL,
        null=True,
    )
    agent = models.ForeignKey(
        Profile,
        related_name="agent_review",
        verbose_name=_("Agent being rated"),
        on_delete=models.SET_NULL,
        null=True,
    )
    rating = models.IntegerField(
        verbose_name=_("Rating"),
        choices=Range.choices,
        help_text="1=Port, 2=Fair, 3=Good, 4=Very Good, 5=Excellent",
        blank=True,
        null=True,
    )
    comment = models.TextField(verbose_name=_("Comment"), null=True, blank=True)

    class Meta:
        unique_together = ["rater", "agent"]

    def __str__(self):
        return f"{self.agent} rated at {self.rating}"
