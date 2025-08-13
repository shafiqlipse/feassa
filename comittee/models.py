from django.db import models

# Create your models here.

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
            ("Secretariat", "Secretariat"),
            ("Executive committee", "Executive committee"),
            ("Government official", "Government official"),
            ("Sports coordinators", "Sports coordinators"),


        ),
        max_length=50,
    )
    lname = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    photo = models.ImageField(upload_to="off_photos/")
    gender = models.CharField(
        max_length=10,
        choices=[("Male", "Male"), ("Female", "Female")],
        null=True,
        blank=True,
    )

    class Meta:
        ordering = ["-fname"]

    def __str__(self):
        return f"{self.fname} {self.lname}"
    
    

class Media(models.Model):
    fname = models.CharField(max_length=50)
    media_type = models.CharField(
        choices=(
            ("NewsPaper ", "NewsPaper "),
            ("Radio ", "Radio "),
            ("Online", "Online"),
            ("Streaming platform", "Streaming platform"),
            ("Television", "Television"),
            ("Tabloid", "Tabloid"),
            ("Blog", "Blog"),

        ),
        max_length=50,
    )
    role = models.CharField(
        choices=(
            ("Photographer ", "Photographer "),
            ("Editor ", "Editor "),
            ("Writer", "Writer"),
            ("Video Journalist", "Video Journalist"),
            ("Journalist", "Journalist"),
            ("Reporter", "Reporter"),
            ("Radio Journalist", "Radio Journalist"),
            ("Presenter", "Presenter"),
            ("Other", "Other"),

        ),
        max_length=50,
    )
    lname = models.CharField(max_length=50)
    media_house = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    photo = models.ImageField(upload_to="media_photos/")

    class Meta:
        ordering = ["-fname"]

    def __str__(self):
        return f"{self.fname} {self.lname}"
    
    