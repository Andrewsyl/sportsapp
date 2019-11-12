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
import datetime


def get_weekdays():
    today = datetime.date.today()
    date = today - datetime.timedelta(days=-(today.weekday() - 1))
    return date.strftime('%Y-%m-%d')


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
    club = request.user.club
    events = Periods.objects.filter(day__club=club)
    # context = {'stuff': events}
    # return render(request, 'timetables/timetable_display.html', context)

    # if filters applied then get parameter and filter based on condition else return object
    if request.GET:
        # event_arr = []
        # for i in periods:
        #     event_sub_arr = {}
        #     event_sub_arr['title'] = i.event_name
        #     start_date = datetime.datetime.strptime(str(i.start_date.date()), "%Y-%m-%d").strftime("%Y-%m-%d")
        #     end_date = datetime.datetime.strptime(str(i.end_date.date()), "%Y-%m-%d").strftime("%Y-%m-%d")
        #     event_sub_arr['start'] = start_date
        #     event_sub_arr['end'] = end_date
        #     event_arr.append(event_sub_arr)
        return HttpResponse()

    date = get_weekdays()
    context = {
        'date': date,
        "events": events,
        # "get_event_types": get_event_types,

    }
    return render(request, 'timetables/timetable_display.html', context)


@login_required(login_url='/login/')
def delete_timetable(request):
    Periods.objects.all().delete()
    return redirect('/')


@login_required(login_url='/login/')
def create_timetable_times(request):
    club = request.user.club
    # Day.objects.all().delete()
    if Periods.objects.filter(club=club):
        return redirect('/timetables/display_timetable')
    days = Day.objects.filter(club=club)
    forms = [PeriodCreateForm(request.POST or None, prefix=str(day), instance=Periods()) for day in Day.objects.all()]
    # periods = Periods.objects.filter(day__club=club)
    if request.POST:
        for day_num, d in enumerate(days):
            for num in range(10):
                day_name = d.name
                if num == 0:
                    field_number = ''
                else:
                    field_number = '_' + str(num)
                try:
                    start_time = datetime.datetime.strptime(
                        request.POST.get(day_name + '-start_time' + field_number, None).split(' ')[0], '%H:%M')
                    end_time = datetime.datetime.strptime(
                        request.POST.get(day_name + '-end_time' + field_number, None).split(' ')[0], '%H:%M')
                except Exception as e:
                    break
                if not start_time or not end_time:
                    break
                period = Periods(start_time=start_time, end_time=end_time, club=club,
                                 day=d, day_number=day_num)
                period.save()

        return redirect('/timetables/display_timetable')
    Periods.objects.all().delete()
    context = {
        'forms': forms,
        'days': days,
    }
    return render(request, 'timetables/create_timetable_times.html', context)
