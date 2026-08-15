from django.db import models
from django.contrib.auth.models import AbstractUser
import qrcode
from django.urls import reverse
from io import BytesIO
from django.core.files.base import ContentFile
from django.core.files import File
from accounts.models import *

# Create your models here.

class School(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=245)
    level = models.CharField(
            choices=(
                ("Primary ", "Primary "),
                ("Secondary", "Secondary "),
                ("National Team", "National Team"),
                ("Other", "Other"),
    
            ),
            max_length=50,blank=True, null=True
        )
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
    qr_code = models.ImageField(upload_to='qr_codes/', blank=True, null=True)
    
    def get_absolute_url(self):
        return reverse("athlete", args=[str(self.id)])

    def save(self, *args, **kwargs):
        # Save instance first to get a primary key (for URL generation)
        if not self.id:
            super().save(*args, **kwargs)

        # Generate QR code data (e.g., a URL to the athlete's detail page)
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr_data = f"https://feassa.org{self.get_absolute_url()}"  # Use your actual domain
        qr.add_data(qr_data)
        qr.make(fit=True)

        # Convert QR code image to binary
        img = qr.make_image(fill_color="black", back_color="white")
        buffer = BytesIO()
        img.save(buffer, format="PNG")
        filename = f"athlete_{self.pk}_qr.png"

        # Save to the qr_code field
        self.qr_code.save(filename, ContentFile(buffer.getvalue()), save=False)

        # Save model with the updated QR code
        super().save(*args, **kwargs)
    def __str__(self):
        return f"{self.fname} {self.lname}"

class Official(models.Model):
    fname = models.CharField(max_length=100, null=True, blank=True, default="")
    lname = models.CharField(max_length=100, null=True, blank=True, default="")
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE, null=True)
    email = models.EmailField(null=True, blank=True, default="")
    nin = models.CharField(max_length=20, null=True, blank=True, default="")
    gender = models.CharField(
        max_length=10,
        choices=[("Male", "Male"), ("Female", "Female")],
        null=True,
        blank=True,
    )
    role = models.CharField(
        max_length=250,
        choices=[
            ("Coach", "Coach"),
            ("Games teacher", "Games teacher"),
            ("Head of delegation", "Head of delegation"),
            ("Field of play officer", "Field of play officer"),
            ("Medical", "Medical"),
            ("Security", "Security"),
            ("Young reporter", "Young reporter"),
            ("Press", "Press"),
            ("Volunteer", "Volunteer"),
            ("President", "President"),
            ("Secretary General", "Secretary General"),
            ("Treasurer", "Treasurer"),
            ("Sports coordinators", "Sports coordinators"),
            ("Matron", "Matron"),
            ("Patron", "Patron"),
            ("Chaperone", "Chaperone"),
            ("Sight guide", "Sight guide"),
            ("Sign language interpreter", "Sign language interpreter"),
            ("Team Manager", "Team Manager"),
            ("Other", "Other"),
        ],
        null=True,
        blank=True,
        

    )
    photo = models.ImageField(
        upload_to="photos/",
        blank=True,
        null=True,
        default="/images/profile.png",
    )

    def __str__(self):
        return f"{self.fname} {self.lname}"



class Position(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)

    gender = models.CharField(
        choices=(("Male", "Male"), ("Female", "Female")), max_length=50
    )
    position = models.IntegerField()

    class Meta:
        unique_together = ("school", "sport", "gender")

    def __str__(self):
        return f"{self.school} - {self.sport} - {self.gender} - Position {self.position}"



# 