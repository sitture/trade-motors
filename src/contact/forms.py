from django import forms
from django.utils.translation import gettext_lazy as _


class ContactForm(forms.Form):
    name = forms.CharField(
        label=_("Name: "),
        required=True, max_length=100,
        error_messages={
            'required': _('Please enter your fullname.')}
        )
    email = forms.EmailField(
        label=_("Email: "),
        required=True, widget=forms.EmailInput,
        error_messages={
            'required': _('Please enter your contact email address.')
            }
        )
    phone = forms.RegexField(
        label=_("Phone: "),
        regex='^\+?1?\d{9,15}$',
        required=True,
        error_messages={
            'required': _('Please enter your phone number.'),
            'invalid': _('Please enter a valid contact number. (Example: +441332409079)')
        })
    query = forms.CharField(
        label=_("Question: "),
        required=True, widget=forms.Textarea,
        error_messages={
            'required': _('Please enter your question in the area provided.')
            }
        )
    topic = forms.CharField(
        required=True, widget=forms.HiddenInput,
        initial='General Enquiry')
