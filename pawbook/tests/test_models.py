from django.test import TestCase

from django.contrib.auth.models import User
from pawbook.models import UserProfile


class UserProfileModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        thisUser = User.objects.create(
            username="testUser123",
            first_name="adam",
            last_name="smith",
            email="pawbook_test@mail.com",
            password="adamtest",
        )
        UserProfile.objects.create(
            user=thisUser,
            age=29,
        )

    def test_first_name_max_length(self):
        user = UserProfile.objects.get(id=1)
        max_length = user._meta.get_field('first_name').max_length
        self.assertEquals(max_length, 32)

    def test_object_name_is_last_name_comma_first_name(self):
        user = UserProfile.objects.get(id=1)
        expected_object_name = f'{user.user.username}'
        self.assertEquals(expected_object_name, str(user))

#    def test_get_absolute_url(self):
 #       author = Author.objects.get(id=1)
  #      # This will also fail if the urlconf is not defined.
   #     self.assertEquals(author.get_absolute_url(), '/catalog/author/1')