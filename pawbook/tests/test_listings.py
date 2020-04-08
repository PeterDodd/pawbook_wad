from pawbook.tests.test_main import *
from pawbook.models import Listing

class TestListing(TestCase):

    def test_create_contact(self):
        register_and_login(self)
        response = Client.post(reverse('pawbook:listings'), valid_add_listing_details,
                               content_type='application/x-www-form-urlencoded')
        self.assertTrue(response.context == None,"")
        listing_breed = Listing.objects.filter(slug=slugify(valid_add_listing_details['breed'])).get()
        listing_petName = Listing.objects.filter(slug=slugify(valid_add_listing_details['petName'])).get()
        listing_description = Listing.objects.filter(slug=slugify(valid_add_listing_details['description'])).get()
        listing_petAge = Listing.objects.filter(slug=slugify(valid_add_listing_details['petAge'])).get()
        listing_cost=Listing.objects.filter(slug=slugify(valid_add_listing_details['cost'])).get()
        listing_petImage=Listing.objects.filter(slug=slugify(valid_add_listing_details['petImage'])).get()
        self.assertTrue(listing_breed==valid_add_listing_details['breed'])
        self.assertTrue(listing_petName==valid_add_listing_details['petName'])
        self.assertTrue(listing_description== valid_add_listing_details['description'])
        self.assertTrue(listing_petAge==valid_add_listing_details['petAge'])
        self.assertTrue(listing_cost == valid_add_listing_details['cost'])
        self.assertTrue(listing_petImage == valid_add_listing_details['petImage'])

