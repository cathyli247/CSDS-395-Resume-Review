from django.contrib.auth.models import User
from django.test import TestCase

# Create your tests here.
from resume_review import user_api
from resume_review.models import Account, Reviewer


class UserAPITestCase(TestCase):
    def test_is_reviewer(self):
        user = User.objects.create(username='aaa')
        res = user_api.is_reviewer(user)
        self.assertFalse(res)

        account = Account.objects.create(user=user)
        res = user_api.is_reviewer(user)
        self.assertFalse(res)

        reviewer = Reviewer.objects.create(account=account)
        res = user_api.is_reviewer(user)
        self.assertTrue(res)

    def test_get_account(self):
        user = User.objects.create(username='aaa')
        res = user_api.get_account_by_user(user)
        self.assertEqual(res, None)

        account = Account.objects.create(user=user)
        res = user_api.get_account_by_user(user)
        self.assertTrue(res is not None)