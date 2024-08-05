from django.contrib import admin

# Register your models here.
from accounts.models import *



# Register your models here.
admin.site.register(User)
admin.site.register(Athlete)
admin.site.register(Sport)
