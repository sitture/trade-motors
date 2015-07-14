from django.test import TestCase
# import the models to test
from settings.models import ContactDetail, Social


class ContactDetailModelTest(TestCase):

    def test_str_with_no_fullname(self):
        email_address = 'test@sitture.com'
        detail = ContactDetail(email=email_address)
        self.assertEquals(
            str(detail),
            detail.email
        )

    def test_str_with_fullname(self):
        email_address = 'test@sitture.com'
        fullname = 'Sitture'
        expected_result = '{0} ({1})'.format(fullname, email_address)
        detail = ContactDetail(
            full_name=fullname,
            email=email_address
        )
        self.assertEquals(
            str(detail),
            expected_result
        )


class SocialModelTest(TestCase):

    def test_str_representation(self):
        test_url = "http://facebook.com/sitture"
        service = Social(service='Facebook', url=test_url)
        self.assertEquals(
            str(service),
            'Facebook'
        )
