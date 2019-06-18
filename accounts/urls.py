from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path('login/', login, name='login'),
    # path('logout/', logout, name='logout'),
    path('registration/', views.registration, name='registration'),
    # path('', views.home, name='home'),
    path('users/', views.users, name='users'),
    # path('student_list/', student_list, name='student_list'),
    # path('student_details/<int:id>', student_details, name='student_details'),
    # path('student_details/<int:id>/delete', student_delete, name='student_delete'),
    # path('student_edit/<int:id>', student_edit, name='student_edit'),
    # path('student_create/', student_create, name='student_details'),
    # path('club_create/', club_create, name='club_create'),
    # path('team_create/', team_create, name='team_create'),
    # path('team_list/', team_list, name='team_list'),
    # path('team_details/<int:id>', team_details, name='team_details'),
    # path('team_edit/<int:id>', team_edit, name='team_edit'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
