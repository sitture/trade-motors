from django.shortcuts import render

from vehicles.context_processor import global_context_processor
from .forms import ContactForm
from dynamic_preferences.registries import global_preferences_registry
# import settings so send_mail can have access to email settings
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages


def contact_page(request):
    form = ContactForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            data = form.cleaned_data
            sender_name = data['name']
            sender_email = data['email']
            sender_phone = data['phone']
            sender_message = data['query']
            email_subject = data['topic']
            message_to_send = (
                "Name: {0}\n"
                "Email: {1}\n"
                "Phone: {2}\n"
                "Enquiry:\n{3}").format(
                sender_name,
                sender_email,
                sender_phone,
                sender_message
            )
            # instanciate a manager for global preferences
            global_preferences = global_preferences_registry.manager()
            # get default email address from global preferences
            send_to_email = global_preferences.get(
                'general__default_email', None)
            # if for some reason, the email from global preferences is None
            # then get default from settings
            if not send_to_email:
                send_to_email = settings.DEFAULT_EMAIL_ADDRESS
            # email the details
            # send_mail(subject, message, from, to, fail_silently)
            from_email = settings.SERVER_EMAIL or 'info@globaltrademotors.com'
            send_mail(
                email_subject,
                message_to_send,
                from_email, [send_to_email],
                fail_silently=True
            )
            messages.success(
                request,
                "Thank you getting in touch! We'll get back to you shortly."
            )
            form = ContactForm()
        else:
            for key, error in form.errors.items():
                messages.info(request, error.as_data()[0].message)
    form = form.__class__
    context = global_context_processor(locals())

    return render(request, "contact_page.html", context)
