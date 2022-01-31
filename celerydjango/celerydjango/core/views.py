from django.shortcuts import render
from .tasks import  sleepy, send_mail_task
from django.http import HttpResponse
from .helper import send_mail_without_celery
# Create your views here.

#test with sending mail with celery and without

def index(request):
    # sleepy.delay()
    # send_mail_without_celery()
    send_mail_task.delay()
    return HttpResponse("<h1>Hello , from Celery</h1>")


# celery -A <djangoprojectname> worker -l info -P eventlet