from django.shortcuts import render
from django.http import HttpResponse
from webapp.models import Application
from webapp.models import Course
from webapp.models import StudentPreference
from django.http import JsonResponse
#from .forms import StudentPreferenceForm

# Create your views here.
def index(request):
	
	if request.method == 'POST':
		for name in request.POST:
			print(name+"="+request.POST[name])
		
		studentPrefObj = StudentPreference(bnumber=request.POST['bnumber'],
			first_name=request.POST['first_name'],
			last_name=request.POST['last_name'],
			program=request.POST['program'],
			required_course=request.POST['required_course'],
			comments = request.POST['comments'],
			enroll_fulltime=request.POST['enroll_fulltime'],
			core_prference_1=request.POST['core_prference_1'],
			core_prference_2=request.POST['core_prference_2'],
			core_prference_3=request.POST['core_prference_3'],
			#core_prference_4=request.POST['core_prference_4'], forfuture requirement
			#core_prference_5=request.POST['core_prference_5'],
			prefernce_1=request.POST['prefernce_1'],
			prefernce_2=request.POST['prefernce_2'],
			prefernce_3=request.POST['prefernce_3'],
			prefernce_4=request.POST['prefernce_4'],
			#prefernce_5=request.POST['prefernce_5'],
			#prefernce_6=request.POST['prefernce_6'],
			#prefernce_7=request.POST['prefernce_7'],
			#prefernce_8=request.POST['prefernce_8'],
			#prefernce_9=request.POST['prefernce_9'],
			
			)		
		studentPrefObj.save()
		print ("hiiii")
	
		
		
	#form  = StudentPreferenceForm()
	applications = Application.objects.all()
	term = "Fall"
	for app in applications:
		if app.active == True:
			term = app.term
			break
			
	print(term)
	#courseDic = {'courses':list(Course.objects.all())}
	otherCourse = list(Course.objects.filter(offered_in_term__contains = term,core=False))
	longProgCourseStr =""
	for course in otherCourse:
		longProgCourseStr = longProgCourseStr + course.course_id + ","
	
	if longProgCourseStr:
		longProgCourseStr = longProgCourseStr[:-1]
	

	courseDic = {
					'requiredCourses':list(Course.objects.filter(offered_in_term__contains = term,core=True)),'otherCourse':list(Course.objects.filter(offered_in_term__contains = term,core=False)),'longProgCourseList': longProgCourseStr,'term':term}
					
	#mylist = courseDic['courses']
	#for cou in mylist:
		#print (cou.course_name)
	return render(request,'webapp/registration.html', courseDic)
	
	
def getPreferenceCount(request):
	courseName = request.GET.get('courseName', None)
	print("Inide getPreferenceCount")
	core = request.GET.get('core', None)
	term = request.GET.get('term',None)
	preference = request.GET.get('preference',None)
	count = 0;
	if core == "True":
		if preference == 1:
			count = StudentPreference.objects.filter().count(core_prference_1__iexact=courseName).count()
		elif preference == 2:
			count = StudentPreference.objects.filter().count(core_prference_2__iexact=courseName).count()
		elif preference == 3:
			count = StudentPreference.objects.filter().count(core_prference_3__iexact=courseName).count()
	else :
		if preference == 1:
			count = StudentPreference.objects.filter().count(prefernce_1__iexact=courseName).count()
		elif preference == 2:
			count = StudentPreference.objects.filter().count(prefernce_2__iexact=courseName).count()
		elif preference == 3:
			count = StudentPreference.objects.filter().count(prefernce_3__iexact=courseName).count()
		elif preference == 4:
			count = StudentPreference.objects.filter().count(prefernce_4__iexact=courseName).count()
	print ("Count="+str(count))
	data = {
	
		'count': str(count)
	}
	return JsonResponse(data)
