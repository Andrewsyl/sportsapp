from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Day, Periods
from .forms import TimetableCreateForm, PeriodCreateForm
from django.forms import modelformset_factory
from users.forms import ClubCreateForm
from django.contrib import auth, messages
from django.contrib.auth import logout as django_logout
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required(login_url='/login/')
def create_timetable_days(request):
    club = request.user.club
    # Day.objects.all().delete()
    form = TimetableCreateForm(request.POST or None)
    if Day.objects.filter(club=club):
        return redirect('/timetables/create_timetable_times')
    if form.is_valid():
        for item in form['Days']:
            if item.data['selected']:
                day = Day(name=item.data['label'], club=club)
                day.save()
        return redirect('/timetables/create_timetable_times')
    context = {
        'form': form,
    }
    return render(request, 'timetables/create_timetable_days.html', context)


@login_required(login_url='/login/')
def display_timetable(request):
    return redirect('/')


@login_required(login_url='/login/')
def create_timetable_times(request):
    club = request.user.club
    if Periods.objects.filter(club=club):
        return redirect('/timetables/display_timetable')
    days = Day.objects.filter(club=club)
    forms = [PeriodCreateForm(request.POST or None, prefix=str(day.name), instance=Periods()) for day in
             Day.objects.all()]
    # periods = Periods.objects.filter(day__club=club)
    if request.POST:
        for d in days:
            for num in range(10):
                day_name = d.name
                if num == 0:
                    field_number = ''
                else:
                    field_number = '_' + str(num)
                start_time = request.POST.get(day_name + '-start_time' + field_number, None)
                end_time = request.POST.get(day_name + '-end_time' + field_number, None)
                if not start_time or not end_time:
                    break
                period = Periods(start_time=start_time, end_time=end_time, club=club,
                                 day=list(Day.objects.filter(club=club))[0])
                period.save()

        return redirect('/')
    Periods.objects.all().delete()
    context = {
        'forms': forms,
        'days': days,
    }
    return render(request, 'timetables/create_timetable_times.html', context)
