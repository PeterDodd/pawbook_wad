from pawbook.tests.test_main import *


class CheckLoginAndLogoutFunctionality(TestCase):

    def test_login(self):
        Client.post(reverse('pawbook:register'),valid_registration_details)
        response = Client.post(reverse('pawbook:login'),login())
        self.assertTrue(response.context==None)
        self.assertTrue(register_and_login())


    # def test_login_with_incorrect_details(self):


    def test_logout(self):
        response = Client.get(reverse('pawbook:login'))
        self.assertTrue(response.context==None)
