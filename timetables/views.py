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
    if len(list(Day.objects.filter(club=club))) > 0:
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
def create_timetable_times(request):
    club = request.user.club
    days = Day.objects.filter(club=club)
    Periods.objects.all().delete()
    PeriodFormSet = modelformset_factory(Periods, form=PeriodCreateForm, extra=0 if len(Periods.objects.all()) > 0 else len(Day.objects.all()))
    form = PeriodFormSet(request.POST or None)
    if form.is_valid():
        for k in form:
            start_time = k.cleaned_data['start_time']
            end_time = k.cleaned_data['end_time']
            period = Periods(start_time=start_time, end_time=end_time)
            period.save()

        return redirect('/')

    context = {
        'form': form,
        'days': days,
    }
    return render(request, 'timetables/create_timetable_times.html', context)
