from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail
# import sendgrid
# import os
# from sendgrid.helpers.mail import *
from .models import Location, Tourney, HighScore, Oldie

# Create your views here.

def index(request):
    locations = Location.objects.all()
    tourney = Tourney.objects.all()
    first_tourney = tourney.first()
    tourney_length = Tourney.objects.count
    high_scores = HighScore.objects.first()
    olds = Oldie.objects.first()
    pics = olds.oldiepic_set.all()
    fisty = olds.oldiepic_set.first()
    # for o in olds:
    #     print(o.oldiepic_set.count)
    first = high_scores.first
    second = high_scores.second
    third = high_scores.third
    machine = high_scores.machine
    scores = '1)' + first + ' ' +  '2)' + second + ' ' +  '3)' + third
    # scores = 'KJA: 300,000' + '   JDS: 200,000' + '   JDS: 200,000'
    print (len(tourney))
    if len(tourney) >= 1:
        yes = True
    else:
        yes = False
        print (True)
    for location in locations:
        print (location.machine_set.count)
    return render(request, "main/machines.html", {'locations': locations, 'tourney': first_tourney, 'yes': yes, 'scores': scores, 'machine': machine, 'pics': pics, 'fisty': fisty})

def send_email(request):
    print('wooooooah')
    description = request.POST.get('problemDescription')
    machine = request.POST.get('probMachine')
    location = request.POST.get('probLocation')
    name = request.POST.get('problemName')
    message = 'machine: ' + machine + '\n' + '\n' + 'location: ' + location + '\n' + '\n' + 'description: ' + description + '\n' + '\n' + 'name: ' + name
    subject = 'Issue with ' + machine
    send_mail(subject, message, 'pinsite@email.com', ['jdstults1@gmail.com'], fail_silently=False)
    # sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
    # from_email = Email("jdstults1@gmail.com")
    # subject = "Hello World from the SendGrid Python Library!"
    # to_email = Email("jdstults1@gmail.com")
    # content = Content("text/plain", "Hello, Email!")
    # mail = Mail(from_email, subject, to_email, content)
    # response = sg.client.mail.send.post(request_body=mail.get())
    return HttpResponseRedirect('/')
