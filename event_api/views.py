from django.shortcuts import render
from events.models import Event , Booking
from .serializers import EventSerializer , EventDetailSerializer
from rest_framework.generics import ListAPIView , RetrieveAPIView
from datetime import datetime
# Create your views here.


class EventListApi(ListAPIView):
    queryset = Event.objects.filter(date__gt = datetime.today())
    serializer_class = EventSerializer

class EventDetailApi(RetrieveAPIView):
    queryset = Event.objects.all()
    serializer_class = EventDetailSerializer
    lookup_field = "id"
    lookup_url_kwarg = "event_id"
