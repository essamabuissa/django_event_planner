from rest_framework.permissions import BasePermission
from events.models import Event

class OrganizerUpdateEvent(BasePermission):
    def has_object_permession(self,request,view,obj):
        if request.user == obj.organizer:
            return True
        return False    
