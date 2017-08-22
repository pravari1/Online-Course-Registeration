from django.conf.urls import url
from . import views

urlpatterns= [url(r'^$',views.index,name='registerationForm'),
url(r'^ajax/getPreferenceCount/$', views.getPreferenceCount, name='getPreferenceCount'),]
#url(r'^registerationForm$',views.registerationFormSubmit,name="registerationFormSubmit")