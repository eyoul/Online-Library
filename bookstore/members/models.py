from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.contrib.auth import get_user_model


# User = get_user_model
class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_publisher = models.BooleanField(default=False)
    is_librarian = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)

    class Meta:
        swappable = 'AUTH_USER_MODEL'

# User('1','user1','user123', False, True, False).save()