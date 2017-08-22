from django.db import models
from django.forms import ModelForm

# Create your models here.
class Application(models.Model):
	term = models.CharField(max_length=20)
	major = models.CharField(max_length=20)
	active = models.BooleanField(default=False)
	
class Course(models.Model):
	course_id =  models.CharField(max_length=20)
	course_name = models.CharField(max_length=50)
	major = models.CharField(max_length=20)
	offered_in_term = models.CharField(max_length=20)
	long_prog = models.BooleanField(default=False)
	core = models.BooleanField(default=False)
	professor_name = models.CharField(max_length=50)

class StudentPreference(models.Model):
	bnumber =  models.CharField(max_length=10, primary_key=True)
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	program =  models.CharField(max_length=20)
	required_course =  models.IntegerField()
	instructor_preference =  models.CharField(max_length=50)
	enroll_fulltime = models.BooleanField(default=False)
	comments =  models.CharField(max_length=200)
	core_prference_1 = models.CharField(max_length=20)
	core_prference_2 = models.CharField(max_length=20)
	core_prference_3 = models.CharField(max_length=20)
	core_prference_4 = models.CharField(max_length=20)
	core_prference_5 = models.CharField(max_length=20)
	prefernce_1 = models.CharField(max_length=20)
	prefernce_2 = models.CharField(max_length=20)
	prefernce_3 = models.CharField(max_length=20)
	prefernce_4 = models.CharField(max_length=20)
	prefernce_5 = models.CharField(max_length=20)
	prefernce_6 = models.CharField(max_length=20)
	prefernce_7 = models.CharField(max_length=20)
	prefernce_8 = models.CharField(max_length=20)
	prefernce_9 = models.CharField(max_length=20)
	
