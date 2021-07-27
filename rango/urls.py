from django.conf.urls import url
from django.urls.resolvers import URLPattern
from rango import views
from django.urls import path

app_name = 'rango'

urlpatterns = [
    path ('',views.index, name='index'),
    path('about/',views.about, name='about'),
]