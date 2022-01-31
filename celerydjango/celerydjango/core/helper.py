from django.core.mail import send_mail



def send_mail_without_celery():
    send_mail('CELERY WORKED YEAH', 'CELERY IS COOL',
              "lewisspencer555@gmail.com",
               ['lewisspencer555@gmail.com'],
               fail_silently= False               
              )
    return None
