from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Day, Periods
from .forms import TimetableCreateForm, PeriodCreateForm
from django.forms import formset_factory
from users.forms import ClubCreateForm
from django.contrib import auth, messages
from django.contrib.auth import logout as django_logout
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required(login_url='/login/')
def create_timetable_days(request):
    club = request.user.club
    form = TimetableCreateForm(request.POST or None)
    if len(list(Day.objects.filter(club=club))) > 0:
        return redirect('/timetables/create_timetable_times')
    if form.is_valid():
        for item in form['Days']:
            if item.data['selected']:
                day = Day(name=item.data['label'], club=club)
                day.save()
        return redirect('timetables/create_timetable_times')
    context = {
        'form': form,
    }
    return render(request, 'timetables/create_timetable_days.html', context)


@login_required(login_url='/login/')
def create_timetable_times(request):
    club = request.user.club
    form = PeriodCreateForm()
    days = Day.objects.filter(club=club)
    form = formset_factory(PeriodCreateForm, extra=2)
    if request.method == 'POST':
        if form.is_valid():
            for num in range(len(days)):
                for time in range(len(form['start_time'])):
                    if form['start_time'][time].data['selected']:
                        start = form['start_time'][time].data['label']
                        end = form['end_time'][time].data['label']
                        period = Periods(
                            day=days[num],
                            start_time=start,
                            end_time=end
                        )
                        period.save()
            return redirect('timetables/create_timetable_days.html')
    context = {
        'form': form,
        'days': days
    }
    return render(request, 'timetables/create_timetable_times.html', context)
