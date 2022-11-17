from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('course', views.course, name='course'),
    path('course_filter', views.course_filter, name='course_filter'),
    path('course/<slug:slug>', views.course_detail, name='course_detail'),
    path('course/watch/<slug:slug>', views.course_watch, name='course_watch'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
    path('search', views.search, name='search'),
    path('404', views.page_not_found, name='404')

]
