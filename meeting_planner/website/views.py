from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from meetings.models import Meeting


def welcome(request):
    return render(request, 'website/welcome.html',
                  {"num_meetings": Meeting.objects.count()})


def date(request):
    return HttpResponse("This page was running at the:" + str(datetime.now()))


def about(request):
    return HttpResponse("I am Andrei and I want to learn Django!")
