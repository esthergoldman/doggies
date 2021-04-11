from django.shortcuts import render
from datetime import datetime
import calendar
from .models import Event, Location
from .forms import SearchForm


def year(request):
    #get current year
    now = datetime.now()
    current_year = now.year
    return render(request,'partials/_footer.html',{"current_year":current_year})

def events(request):
    one_event = Event.objects.order_by('event_date')
    return render(request,'events/events.html',{"one_event": one_event,})




def search_events(request):
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            events = Event.objects.filter(event_date__icontains=form.cleaned_data['datetime'])


        keywords = request.POST['keywords']
        events = Event.objects.filter(event_date__icontains=keywords)
        
        return render(request,'events/search_events.html',{"keywords": keywords,"events": events,"form":form})
    else: 
        form = SearchForm()

        return render(request,'events/search_events.html',{"form":form})

