from celery import shared_task
from time import sleep 
from django.core.mail import send_mail
from .models import Book

@shared_task
def sleepy():
    Book.objects.create(Title='bigget').save()
    return None

# def sleepy(duration):
#     # sleep(duration)
#     Book.objects.create(Title='bigget').save()
#     return None


# celery -A <module> -l info -P eventlet


@shared_task
def send_mail_task():
    send_mail('CELERY WORKED YEAH', 'CELERY IS COOL', "lewisspencer555@gmail.com",
              ['lewisspencer555@gmail.com'],
              fail_silently= False)
    print("MAIL FROM CELERY")
    return None