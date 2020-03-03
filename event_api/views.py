from django.shortcuts import render
from events.models import Event , Booking
from rest_framework.permissions import IsAuthenticated
from datetime import datetime
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import status

from .serializers import (EventSerializer ,
EventCreateSerializer,
RegisterSerializer)
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView

from datetime import datetime
# Create your views here.

class EventAPIView(APIView):
    def get(self , request, event_id= None , user_id = None):
        self.permission_classes = [IsAuthenticated]
        self.check_permissions(request)

        if event_id:
            event_id_obj = Event.objects.get(id =event_id)
            serializer = EventSerializer(event_id_obj)
            return Response(serializer.data)

        if user_id:
            user_obj = User.objects.get(id = user_id)
            event_list_obj = Event.objects.filter(organizer = user_obj)
            serializer = EventSerializer(event_list_obj , many = True)
            return Response(serializer.data)

        event_date_obj = Event.objects.filter(date__gt = datetime.today().date())
        serializer = EventSerializer(event_date_obj , many = True)
        return Response(serializer.data)

    def post(self,request):
        self.permission_classes = [IsAuthenticated]
        self.check_permissions(request)
        serializer_class = EventCreateSerializer(data = request.data)

        if serializer_class.is_valid():
            serializer_class.save(organizer = request.user)
            return Response(serializer_class.data,status=status.HTTP_201_CREATED)
        return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)

class RegisterAPI(CreateAPIView):
    serializer_class = RegisterSerializer
