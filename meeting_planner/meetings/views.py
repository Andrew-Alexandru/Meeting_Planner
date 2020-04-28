from django.shortcuts import render
from .models import Meeting


def detail(request, id):
    # id is the id of the meeting to show on page
    meeting = Meeting.objects.get(pk=id)
    # pk is primary key ->row with this unique id
    return render(request, 'meetings/detail.html', {'meeting': meeting})
