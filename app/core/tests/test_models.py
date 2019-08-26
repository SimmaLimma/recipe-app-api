from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_sucessful(self):
        """Test creating new user with email and checking success"""
        email = "test@abc.com"
        password = "abc123"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test if the email for a new user is normalized"""
        email = 'test@ABC.COM'
        user = get_user_model().objects.create_user(email, 'ExamplePW')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""

        # Everything within the 'with' keyword should raise the provided 
        #   error (ValueError)
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'ExamplePW')

    def test_create_new_superuser(self):
        """Test creating a new super user """
        user = get_user_model().objects.create_superuser(
            'test@abc.com',
            'ExPW'
        )

        # Field .is_superuser is included in PermissionMixin
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)