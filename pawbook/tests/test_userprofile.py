from pawbook.tests.test_main import *

class CheckUserProfile(TestCase):

    def test_profile(self):
        register_and_login()
        response = Client.get(reverse('pawbook:userprofile'))
        self.assertTrue(response.context == None)