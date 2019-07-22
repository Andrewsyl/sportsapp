from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Club
from .forms import TimetableCreateForm
from users.forms import ClubCreateForm
from django.contrib import auth, messages
from django.contrib.auth import logout as django_logout
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required(login_url='/login/')
def create_timetable(request):
    club = request.user.club
    form = TimetableCreateForm(request.POST or None)
    template_name = ''
    if form.is_valid():
        instance = form.save(commit=False)
        instance.club = club
        instance.save()
        return redirect('timetables/create_timetable.html')
    context = {
        'form': form,
    }
    return render(request, 'timetables/create_timetable.html', context)
