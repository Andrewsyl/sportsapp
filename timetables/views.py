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
    # Periods.objects.all().delete()
    days = Day.objects.filter(club=club)
    forms = [PeriodCreateForm(request.POST or None, prefix=str(day.name), instance=Periods()) for day in Day.objects.all()]
    if request.POST:
        thing = request.POST.get('fields_Tuesday_3')
        if [cf.is_valid() for cf in forms]:
            for n, k in enumerate(forms):
                start_time = k['start_time'].data
                end_time = k['end_time'].data
                period = Periods(start_time=start_time, end_time=end_time, day=Day.objects.all()[n])
                period.save()

            return redirect('/')

    context = {
        'forms': forms,
        'days': days,
    }
    return render(request, 'timetables/create_timetable_times.html', context)
