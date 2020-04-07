from pawbook.tests.test_main import *


class CheckLoginAndLogoutFunctionality(TestCase):

    def test_login(self):

        response = self.client.post(reverse('pawbook:register'),
                                    valid_registration_details,
                                    content_type='application/x-www-form-urlencoded')

        #response = self.client.post(reverse('pawbook:login'), login(self))

        self.assertTrue(response.context==None)
        self.assertEquals(register_and_login(self), True)


    def test_login_with_incorrect_details(self):
        pass


    def test_logout(self):
        response = self.client.get(reverse('pawbook:login'))
        self.assertEquals(response.context, None)
