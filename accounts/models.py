from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    is_games = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
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


class Championship(models.Model):
    name = models.CharField(max_length=245)
    thumbnail = models.ImageField(upload_to="sportImages/", blank=True, null=True)

    class Meta:
        ordering = ["-name"]

    def __str__(self):
        return self.name


class School(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=245)
    country = models.CharField(max_length=245)
    badge = models.ImageField(upload_to="badge/", blank=True, null=True)

    class Meta:
        ordering = ["-name"]

    def __str__(self):
        return self.name


class Athlete(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    classroom = models.CharField(max_length=50, null=True, blank=True)

    gender = models.CharField(
        choices=(("Male", "Male"), ("Female", "Female")), max_length=50
    )
    date_of_birth = models.DateField(auto_now=False, auto_now_add=False)
    photo = models.ImageField(upload_to="athlete_photos/")
    id_number = models.CharField(max_length=50)

    class Meta:
        ordering = ["-fname"]

    def __str__(self):
        return f"{self.fname} {self.lname}"


class NOC(models.Model):
    fname = models.CharField(max_length=50)
    comittee = models.CharField(
        choices=(
            ("Technical ", "Technical "),
            ("Welfare ", "Welfare "),
            ("Protocol", "Protocol"),
            ("Finance", "Finance"),
            ("Competitions", "Competitions"),
            ("Medical /Health", "Medical /Health"),
            ("Security and Safety", "Security and Safety"),
            ("Transport", "Transport"),
            ("Corporate Relations", "Corporate Relations"),
            ("Media", "Media"),
            ("Secretariat", "Secretariat"),
        ),
        max_length=50,
    )
    lname = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    photo = models.ImageField(upload_to="off_photos/")

    class Meta:
        ordering = ["-fname"]

    def __str__(self):
        return f"{self.fname} {self.lname}"
