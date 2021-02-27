from django.shortcuts import render, reverse, HttpResponseRedirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages


def contact_us(request):
    """ View to connect and return the contact us page """
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message_subject = request.POST['message-subject']
        message_text = request.POST['message-text']

        """send the email
        Example from Codemy Youtube channel:
        https://www.youtube.com/watch?v=xNqnHmXIuzU"""
        send_mail(
            (message_name + " - " + message_subject),
            message_text,
            message_email,
            [settings.DEFAULT_FROM_EMAIL],
        )

        messages.success(request, f'Thank you {message_name}! \
        Your message was received and we will get in touch on  \
        your email {message_email}.')

        return HttpResponseRedirect(reverse('contact_us'))

    else:
        return render(request, 'contact/contact_us.html')
