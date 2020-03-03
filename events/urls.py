from django.urls import path
from .views import Login, Logout, Signup, home
from events import views
from event_api import views as apiviews
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response



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
	path('booking/<int:event_id>/<int:total_tickets>', views.Book, name='booking'),

	#API URLS
	path('api/listapi/', apiviews.EventAPIView.as_view(), name='event-list-api'),
	path('api/detailapi/<int:event_id>', apiviews.EventAPIView.as_view(), name='event-detail-api'),
	path('api/user/<int:user_id>', apiviews.EventAPIView.as_view(), name='event-detail-api'),
	path('api/create/', apiviews.EventAPIView.as_view(), name='event-detail-api'),


	#Authentication URLS
	path('api/login/', TokenObtainPairView.as_view(), name='api-login'),
    path('api/register/', apiviews.RegisterAPI.as_view(), name='api-register'),


]
