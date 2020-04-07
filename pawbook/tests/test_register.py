from pawbook.tests.test_main import *
from django.urls import reverse


class CheckValidRegistration(TestCase):

    def test_no_double_users(self):
        path=reverse('pawbook:register')
        print(path)
        response = self.client.post(path, valid_registration_details,
                                    content_type='application/x-www-form-urlencoded')
        self.assertTrue(response.context==None, "Registration is malfunctioned, needs fixing")

#        error_msg= "A user with that username already exists."
 #       self.assertTrue(response.context!= None and response.context['registered']==True,error_msg)


    def test_registration_fields_not_null(self):
        pass



