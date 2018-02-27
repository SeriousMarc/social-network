from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from posts.models import Post

User = get_user_model()
"""
WHY DOESN'T WORK?????
"""
class PostAPITestCase(APITestCase):
    def setUP(self):
        user_obj = User(username="testapiuser", email="test@test.com")
        user_obj.set_password('randompassword')
        user_obj.save()
        post = Post.objects.create(
            user=user_obj,
            title="title1",
            slug="title1",
            content="somecontent1"
        )
        print('Test' + post.pub_date)

    def test_single_user(self):
        user_count = User.objects.count()
        # print(user_count)
        self.assertEqual(user_count, 1)

    def test_single_post(self):
        # user_count = User.objects.count()
        self.assertEqual(Post.objects.count(), 1)
