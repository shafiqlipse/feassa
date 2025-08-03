from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    is_games = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_media = models.BooleanField(default=False)
    country = models.CharField(
        choices=(
            ("Uganda", "Uganda"),
            ("Kenya", "Kenya"),
            ("Tanzania", "Tanzania"),
            ("Rwanda", "Rwanda"),
            ("Burundi", "Burundi"),
            ("Zanzibar", "Zanzibar"),
            ("South Sudan", "South Sudan"),
        ),
        max_length=50,
    )

class Sport(models.Model):
    name = models.CharField(max_length=245)

    thumbnail = models.ImageField(upload_to="sportImages/", blank=True, null=True)

    class Meta:
        ordering = ["-name"]

    def __str__(self):
        return self.name

