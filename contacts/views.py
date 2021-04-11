from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from contacts.models import Contact


def contact2(request):
    if request.method == 'POST':
        pet_id = request.POST['pet_id']
        pet = request.POST['pet']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        
        contact = Contact( pet_id=pet_id, pet =pet,  name=name, email=email, phone=phone, message=message )

        contact.save()
         #send an email function
        send_mail(
            'Hi! ' + name + ' Thank you for your message', #subject person´s name
            'We´ll be in touch shortly!', #message
            email, #from email
           ['esti.codes@gmail.com'], #to email
        )

        messages.success(request, 'Thank you for your message! We´ll be in touch shortly! ')
        return redirect('index')

