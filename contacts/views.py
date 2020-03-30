# -*- coding: utf-8 -*-
from __future__ import unicode_literals
  
from django.contrib import messages
from django.core.mail import BadHeaderError, send_mail
from django.shortcuts import render, redirect
from contacts.models import Contact
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
    

        #send email
        send_mail(
            'Portfolio message',
            message,
            [email],
            ['bilal92390@gmail.com'],
            fail_silently=False,
        )  
        
        messages.success(request, "Michel will get back to you soon")
        return redirect('index')

