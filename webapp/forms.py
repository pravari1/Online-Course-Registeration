from django import forms
from webapp.models import StudentPreference
from django.forms.widgets import RadioSelect
from webapp.models import Application
from webapp.models import Course

class StudentPreferenceForm(forms.ModelForm):
    #program_choices = (('MS','MS'),('PHD','PHD'))
	
	class Meta:
				
		model = StudentPreference
		fields = ['bnumber', 'first_name', 'last_name','program','required_course','instructor_preference','enroll_fulltime','comments','core_prference_1','core_prference_2','core_prference_3','core_prference_4','core_prference_5','prefernce_1','prefernce_2','prefernce_3','prefernce_4','prefernce_5','prefernce_6','prefernce_7','prefernce_8','prefernce_9']
		widgets={
		"bnumber":forms.widgets.TextInput(attrs={'class':"form-group"}),
		"first_name":forms.widgets.TextInput(attrs={'class':"form-group"}),
		"last_name":forms.widgets.TextInput(attrs={'class':"form-group"}),
		"program":forms.widgets.Select(attrs={'class':"dropdown form-group"},choices= (('MS','MS'),('PHD','PHD'))),
		"required_course":forms.widgets.Select(attrs={'class':"dropdown form-group"},choices= (('1','1'),('2','2'),('3','3'),('4','4'))),
		"instructor_preference":forms.widgets.TextInput(attrs={'class':"form-group"}),
		'enroll_fulltime': forms.widgets.Select(attrs={'class':"dropdown form-group"},choices= (('yes','Yes'),('no','No'))),
		"comments":forms.widgets.TextInput(attrs={'class':"form-group"})
		}
		labels={"required_course":"Required Courses-How Many?*",
		"program":"Program*"
		}
		help_texts = {
            'instructor_preference': 'Group to which this message belongs to',
        }