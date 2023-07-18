from django.test import TestCase
from .models import PublishedManager, Post
from django.contrib.auth.models import User
from django.urls import reverse
from unittest import skip

# Create your tests here.
class TestView(TestCase):

    def test_post_list(self):
        response = self.client.get(reverse('/'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'list.html')

    def test_post_detail(self):
        response = self.client.get(reverse('/<int:year>/<int:month>/<int:day>/<slug:post>/'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'detail.html')

    def test_post_share(self):
        response = self.client.get(reverse('/<int:post_id>/share/'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'share.html')

class TestModel(TestCase):

    def setUp(self):
        user = User.objects.create_user(username="duyen", email="intern.dlpduyen@sdc.edu.vn", password="123456")
        Post.objects.create(title="lion", slug="roar", author=user, body="", publish="", 
                            created="", updated="", status="")
    
    @skip("Don't want to test")
    def test_get_queryset(self):
        pass

    @skip("Don't want to test")
    def test_string(self):
        pass

    @skip("Don't want to test")
    def test_get_absolute_url(self):
        pass

class TestForm(TestCase):

    @skip("Don't want to test")
    def test_email_post_form(self):
        pass
