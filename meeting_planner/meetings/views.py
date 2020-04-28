from django.shortcuts import render, get_object_or_404
from .models import Meeting,Room


def detail(request, id):
    # id is the id of the meeting to show on page
    meeting = get_object_or_404(Meeting, pk=id)
    # pk is primary key ->row with this unique id
    return render(request, 'meetings/detail.html', {'meeting': meeting})

def room_list(request):
    return render(request,'meetings/room_list.html',{'rooms':Room.objects.all()})