from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from accounts.models import *
from school.models import *
from comittee.models import *

class UserAdmin(BaseUserAdmin):
    list_display = ("username", "email", "is_active",  "is_staff", "is_admin", "country")  # Columns to display
    search_fields = ("username", "email")  # Enables search
    list_filter = ("is_active",  "is_staff", "is_admin", )  # Enables filtering

class AthleteAdmin(admin.ModelAdmin):  # Inherit from admin.ModelAdmin
    list_display = ("fname", "lname", "id_number", "gender", "classroom", "school", "date_of_birth")
    search_fields = ("fname", "lname", "id_number")  # Use school__name instead of school
    list_filter = ("classroom", "gender")

class NocAdmin(admin.ModelAdmin):  # Inherit from admin.ModelAdmin
    list_display = ("fname", "lname")
    search_fields = ("fname", "lname")  # Use school__name instead of school

# Register your models here.
admin.site.register(Athlete, AthleteAdmin) 

class SchoolAdmin(admin.ModelAdmin):  # Inherit from admin.ModelAdmin
    list_display = ("name","country", )
    search_fields =( "name", "country")  # Use school__name instead of school

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(NOC,NocAdmin)
admin.site.register(Sport)
admin.site.register(Media)
admin.site.register(Official)
admin.site.register(School,SchoolAdmin)
