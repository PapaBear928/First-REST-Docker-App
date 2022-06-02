from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):
    '''Testing models'''

    def test_create_user_with_email_successful(self):
        email = 'test@test.com'
        password = 'testtest'
        user = get_user_model().objects.create_user(
            email=email,
            password=password,

        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Testing normalized email for new users"""

        sample_emails = [
            ['test1@EXAMPLE.com', 'test1@example.com'],
            ['Test2@Example.com', 'Test2@example.com'],
            ['TEST3@EXAMPLE.com', 'TEST3@example.com'],
            ['test4@example.COM', 'test4@example.com'],
        ]

        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(email, 'sample221')
            self.assertEqual(user.email, expected)


    def test_new_user_whitout_email(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', 'bobofrut')


    def test_create_superuser(self):
        user = get_user_model().objects.create_superuser(
            'test@test.com',
            'test223',
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
