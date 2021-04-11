from django.shortcuts import render
from django.core.mail import send_mail
from adopt.choices import sex_choices, color_choices, size_choices, area_choices
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from adopt.models import Pet
from caretakers.models import Caretaker
from info.models import Contact
from info.models import Found
from .forms import FoundForm
from django.http import HttpResponseRedirect



def index(request):
    pets = Pet.objects.order_by('arrival_date').filter(is_published=True)[:3] #Ascending order is implied. Display only 3 pets 
    
    context = {
        'pets': pets,
        'sex_choices': sex_choices,
        'color_choices': color_choices,
        'size_choices': size_choices,
        'area_choices': area_choices,
    }

    return render(request, 'info/index.html', context)

def about(request):
    caretakers = Caretaker.objects.order_by('join_date') #get all caretakers by name

    context = {
        'caretakers': caretakers
    }

    return render(request, 'info/about.html', context)

def donate(request):
    return render(request, 'info/donate.html')


def contact(request):
    #form contact
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        phone = request.POST['phone']
        email = request.POST['email']
        message = request.POST['message']

        contact = Contact( first_name = first_name, last_name = last_name,  phone = phone, email=email, message=message )

        contact.save()

        #send an email function
        send_mail(
            'Hi! ' + first_name + ' Thank you for your message', #subject person´s name
            message, #message
            email, #from email
           ['esti.codes@gmail.com'], #to email
        )


        return render(request, 'info/contact.html', {'first_name': first_name})
    
    else:
        return render(request, 'info/contact.html')


def add_found(request):
    # if this is a POST request we need to process the form data
    submitted = False
    if request.method == "POST":
        form = FoundForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/found?submitted=True')
    else:
        form = FoundForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'info/found.html',{'form': form, 'submitted':submitted})


def all_found(request):
    pet_found = Found.objects.order_by('-upload_date')
    paginator = Paginator(pet_found,6) #show 6 pets per page
    page = request.GET.get('page')
    page_found = paginator.get_page(page)
    
    context = {
        'pet_found': page_found
    }
    return render(request, 'info/all_found.html',context)