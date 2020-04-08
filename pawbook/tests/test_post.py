from pawbook.tests.test_main import *
from pawbook.models import Post

class TestPost(TestCase):

    def test_create_post(self):
        register_and_login(self)
        response = Client.post(reverse('pawbook:posts'), valid_post_detail,
                               content_type='application/x-www-form-urlencoded')
        self.assertTrue(response.context == None,"")
        post_title = Post.objects.filter(slug=slugify(valid_post_detail['postTitle'])).get()
        post_description = Post.objects.filter(slug=slugify(valid_post_detail['postDescription'])).get()
        self.assertTrue(post_description==valid_post_detail['postDescription'])
        self.assertTrue(post_title==valid_post_detail['postTitle'])