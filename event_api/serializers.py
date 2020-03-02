from events.models import Event , Booking
from rest_framework import serializers
class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        exclude = ['description']

class EventDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'
