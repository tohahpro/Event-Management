from django.shortcuts import render, redirect
from Events.event_from import EventModelFrom, CategoryModelForm
from django.contrib import messages
from django.db.models import Count
from Events.models import Events, Participant
from datetime import date

# Create your views here.
def home_page(request):

    type = request.GET.get('type','all')
    base_query = Events.objects.select_related('category') 
    events = base_query.all()

    return render(request, 'home/event.html', {"events": events})

def manage_dashboard(request):

    type = request.GET.get('type','all')
    base_query = Events.objects.select_related('category')    
    
    today = date.today()
    previous_events = Events.objects.filter(due_date__lt=today)
    next_events = Events.objects.filter(due_date__gt=today)

    # For count ----
    pastEvent = previous_events.count()
    upcomingEvent = next_events.count()

    if type == 'upcoming':
        events = base_query.filter(due_date__gt=today)
        eventCount= events.count()
    elif type == 'past':
        events = base_query.filter(due_date__lt=today)
        eventCount= events.count()

    elif type == 'all':
        events = base_query.all()
        eventCount= events.count()
    
    counts = Events.objects.aggregate(        
        total_event= Count('id')        
    )

    participantCount = Participant.objects.aggregate(
        total_participantCount= Count('id')
    )

    context = {
        "counts": counts,
        "participantCount":participantCount,
        "pastEvent":pastEvent,
        "upcomingEvent":upcomingEvent,
        "events":events,
        "eventCount":eventCount,
    }

    return render(request,'dashboard/manage_dashboard.html', context)

def create_event(request):
    event_form = EventModelFrom()
    event_category_form = CategoryModelForm()
    if request.method == "POST":
        event_form = EventModelFrom(request.POST)       
        event_category_form = CategoryModelForm(request.POST)

        if event_form.is_valid() and event_category_form.is_valid():
            event = event_form.save()
            event_category = event_category_form.save(commit=False)
            event_category.category = event
            event_category.save()

            messages.success(request, "Event Created Successfully.")
            return redirect('create-event')
    return render(request, "create_event.html", {'event_form':event_form, 'event_category':event_category_form})