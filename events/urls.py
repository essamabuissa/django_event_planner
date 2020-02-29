from django.urls import path
from .views import Login, Logout, Signup, home
from events import views

urlpatterns = [
	path('', home, name='home'),
    path('signup/', Signup.as_view(), name='signup'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),

	#Views Urls
	path('create/', views.EventCreate, name='event-create'),
	path('list/', views.EventList, name='event-list'),
	path('detail/<int:event_id>', views.EventDetail, name='event-detail'),
	path('update/<int:event_id>', views.EventUpdate, name='event-update'),
	path('delete/<int:event_id>', views.EventDelete, name='event-delete'),
	path('dashboard/', views.EventDashboard, name='dashboard'),


]
