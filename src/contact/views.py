from django.shortcuts import render_to_response, RequestContext
from vehicles.context_processor import global_context_processor
from .forms import ContactForm
from dynamic_preferences import global_preferences_registry
# import settings so send_mail can have access to email settings
from django.conf import settings
from django.core.mail import send_mail


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
            send_mail(
                email_subject,
                message_to_send,
                sender_email, [send_to_email],
                fail_silently=not settings.DEBUG
            )
            form = ContactForm()

    return render_to_response(
        "contact_page.html", locals(),
        context_instance=RequestContext(
            request, processors=[global_context_processor]
        )
    )
