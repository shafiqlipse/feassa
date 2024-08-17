from django.db import models
from accounts.models import *


# Create your models here.


class SchoolTeam(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, null=True)
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE, null=True)

    gender = models.CharField(
        max_length=10,
        choices=[("Male", "Male"), ("Female", "Female")],
    )

    athletes = models.ManyToManyField(Athlete)

    def __str__(self):
        return f"{self.school} {self.sport}"


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
            ("Organising Secretary", "Organising Secretary"),
            ("Vice President(ADM)", "Vice President(ADM)"),
            ("Vice President (Tech)", "Vice President (Tech)"),
            ("Asst Secretary General", "Asst Secretary General"),
            ("Publicity Secretary", "Publicity Secretary"),
            ("Member", "Member"),
            ("Co-Opted Member", "Co-Opted Member"),
            ("Secretariat", "Secretariat"),
            ("Sports coordinators", "Sports coordinators"),
            ("Referee", "Referee"),
            ("Umpires", "Umpires"),
            ("Matron", "Matron"),
            ("Patron", "Patron"),
            ("OR-TAMISEM Sports  coordinator", "OR-TAMISEM Sports  coordinator"),
            ("MOSCASMoEST", "MOSCASMoEST"),
            ("MoEST", "MoEST"),
            ("UMISSETA/UMITASHUMTA chairperson", "UMISSETA/UMITASHUMTA chairperson"),
            (
                "UMISSETA/UMITASHUMTA vice chairperson",
                "UMISSETA/UMITASHUMTA vice chairperson",
            ),
            ("UMISSETA secretary", "UMISSETA secretary"),
            ("UMISSETA Treasury.", "UMISSETA Treasury"),
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


class UserActivityLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity = models.CharField(max_length=255)
    timestamp = models.DateTimeField()

    def __str__(self):
        return f"{self.user} - {self.activity} at {self.timestamp}"
