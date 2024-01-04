from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

class CustomUser(AbstractUser):
    # Add custom fields to store additional user details
    email = models.EmailField(unique=True)
    # Add other fields as needed
    class Meta:
        db_table = 'custom_user'

    # Define related names for groups and user_permissions
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_users_groups',  # Custom related_name for groups
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_users_permissions',  # Custom related_name for user_permissions
        blank=True,
        help_text='Specific permissions for this user.',
    )

    def __str__(self):
        return self.username


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    api_key = models.CharField(max_length=100, unique=True)
    # Add other profile-related fields as needed

    def __str__(self):
        return self.user.username

