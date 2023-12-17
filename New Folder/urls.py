from view import send_email_view
from django.urls import path


urlpatterns = [
    path('amir13.asghari81@gmail.com', send_email_view, name='send_email')
]
