from django.urls import path
from . import views
urlpatterns = [
    path("", views.home, name='home'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.signout, name='signout'),
    path('venues',views.venues,name='venues'),
    path('event',views.event,name='event'),
    path('mlist',views.mlist,name='mlist'),
    path('book',views.booked_events,name='booked_events'),
    path('help',views.help,name='help'),
]