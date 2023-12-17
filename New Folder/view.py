from django.core.mail import send_mail
from django.shortcuts import render


def send_email_view(request):
    subject = 'Welcome to Django Email Sender'
    message = 'This is a test email sent using Django'
    from_email = 'sender@example.com'
    recipient_list = ['recipient@example.com']

    send_mail(subject, message, from_email, recipient_list)

    return render(request, 'success.html')
