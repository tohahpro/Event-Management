from django.urls import path
from event.views import home_page, manage_dashboard, create_event

urlpatterns = [
    path('home/',home_page,name='home'),
    path('create-event/',create_event,name='create-event'),
    path('dashboard/',manage_dashboard,name='dashboard'),
]