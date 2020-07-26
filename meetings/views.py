from django.shortcuts import render, redirect
from .models import Meeting
from .forms import MeetingForm


def meetings(request):
    template = 'meetings/meetings.html'
    all_meetings = Meeting.objects.all()
    return render(request, template, {'meetings': all_meetings})


def meeting(request, id):
    template = 'meetings/meeting.html'
    meeting_obj = Meeting.objects.get(pk=id)
    return render(request, template, {'meeting': meeting_obj})


def new_meeting(request):
    template = 'meetings/new.html'
    if request.method == 'POST':
        form = MeetingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('website:home')
    else:
        form = MeetingForm()
    return render(request, template, {'form': form})
