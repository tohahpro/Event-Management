from django.shortcuts import render, redirect
from event.event_from import EventModelFrom, CategoryModelForm
from django.contrib import messages

# Create your views here.
def home_page(request):
    return render(request, 'home/event.html')

def manage_dashboard(request):
    return render(request,'dashboard/manage_dashboard.html')

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