from django.contrib import admin
from webapp.models import Application
from webapp.models import Course
from webapp.models import StudentPreference 
# Register your models here.
admin.site.register(Application)
admin.site.register(Course)
admin.site.register(StudentPreference)