from django.conf.urls import url
from django.urls.resolvers import URLPattern
from rango import views
from django.urls import path

app_name = 'rango'

urlpatterns = [
    path ('',views.index, name='index'),
    path('about/',views.about, name='about'),
    path('category/<slug:category_name_slug>/',
        views.show_category, name='show_category'),
]