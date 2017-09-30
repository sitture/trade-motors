from django.test import TestCase
from contact.forms import ContactForm
from django.core.urlresolvers import reverse


class ContactFormTests(TestCase):

    def setUp(self):
        self.form_data = {
            'name': '',
            'email': '',
            'phone': '',
            'query': '',
            'topic': '',
        }

    def get_response(self):
        return self.client.post(
            reverse('contact'), self.form_data)

    def test_form_is_inavlid_when_all_fields_blank(self):
        form = ContactForm(data=self.form_data)
        self.assertFalse(
            form.is_valid(),
            'The form submitted should not be valid.'
        )

    def test_form_is_valid_when_all_field_present(self):
        self.form_data = {
            'name': 'Test Name',
            'email': 'test@email.com',
            'phone': '01331234134',
            'query': 'This is a test question.',
            'topic': 'General Enquiry',
        }
        form = ContactForm(data=self.form_data)
        self.assertTrue(
            form.is_valid(),
            'The form submitted should be valid.'
        )

    def test_name_field_error_message_in_response_when_blank(self):
        self.assertIn(
            'Please enter your fullname.',
            str(self.get_response())
        )

    def test_email_field_error_message_in_response_when_blank(self):
        self.assertIn(
            'Please enter your contact email address.',
            str(self.get_response())
        )

    def test_phone_field_error_message_in_response_when_blank(self):
        self.assertIn(
            'Please enter your phone number.',
            str(self.get_response())
        )

    def test_query_field_error_message_in_response_when_blank(self):
        self.assertIn(
            'Please enter your question in the area provided.',
            str(self.get_response())
        )

    def test_invalid_phone_error_message(self):
        self.form_data['phone'] = 'inavlidemail'
        self.assertIn(
            'Please enter a valid contact number.',
            str(self.get_response())
        )
