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
	path('list/', views.EventList, name='list-create'),

]
