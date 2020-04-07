from pawbook.tests.test_main import *
from pawbook.models import Contact

class TestContactUs(TestCase):

    def test_create_contact(self):
        register_and_login()
        response = Client.post(reverse('pawbook:listing'),valid_add_listing_details)
        self.assertTrue(response.context == None,"")
        contact_firstName = Contact.objects.filter(slug=slugify(valid_contact_us_detail['first_name'])).get()
        contact_lastName = Contact.objects.filter(slug=slugify(valid_contact_us_detail['last_name'])).get()
        contact_email = Contact.objects.filter(slug=slugify(valid_contact_us_detail['email'])).get()
        contact_message = Contact.objects.filter(slug=slugify(valid_contact_us_detail['message'])).get()
        self.assertTrue(contact_firstName==valid_contact_us_detail['first_name'])
        self.assertTrue(contact_lastName==valid_contact_us_detail['last_name'])
        self.assertTrue(contact_email== valid_contact_us_detail['email'])
        self.assertTrue(contact_message==valid_contact_us_detail['message'])
