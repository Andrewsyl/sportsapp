from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('create_timetable_days/', views.create_timetable_days, name='create_timetable_days'),
    path('create_timetable_times/', views.create_timetable_times, name='create_timetable_times'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
