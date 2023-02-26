from django.db import models
from django.contrib.auth.models import User
# from django.contrib.auth.models import AbstractUser
# from django.contrib.auth import get_user_model

# Create your models here.

# class User(AbstractUser):
#     is_admin = models.BooleanField(default=False)
#     is_publisher = models.BooleanField(default=False)
#     is_librarian = models.BooleanField(default=False)
#     is_student  = models.BooleanField(default=False)

#     class Meta:
#         swappable = 'AUTH_USER_MODEL'

class Tbook(models.Model):
    grade = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    desc = models.CharField(max_length=1000)
    uploaded_by = models.CharField(max_length=100, null=True, blank=True)
    pdf = models.FileField(upload_to='ebook/media/tbook/pdfs')
    cover = models.ImageField(upload_to='ebook/media/tbook/covers', null=True, blank=True)

    def __str__(self):
        return self.grade
    
    def delete(self, *args, **kwargs):
        self.pdf.delete()
        self.cover.delete()
        super().delete(*args, **kwargs)

class Rbook(models.Model):
    title = models.CharField(max_length=100)
    grade = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    desc = models.CharField(max_length=1000)
    uploaded_by = models.CharField(max_length=100, null=True, blank=True)
    pdf = models.FileField(upload_to='ebook/media/rbook/pdfs')
    cover = models.ImageField(upload_to='ebook/media/rbook/covers', null=True, blank=True)

    def __str__(self):
        return self.title
    
    def delete(self, *args, **kwargs):
        self.pdf.delete()
        self.cover.delete()
        super().delete(*args, **kwargs)

class Chat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    posted_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return str(self.message) + '|' + str(self.user)

class Deleterequest(models.Model):
    delete_request = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.delete_request

class Feedback(models.Model):
    feedback = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.feedback