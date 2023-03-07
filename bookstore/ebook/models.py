from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Text Book models

class Tbook(models.Model):
    grade = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    desc = models.CharField(max_length=1000)
    uploaded_by = models.CharField(max_length=100, null=True, blank=True)
    pdf = models.FileField(upload_to="ebook/static/ebook/media/tbook/pdfs")
    cover = models.ImageField(
        upload_to="ebook/static/ebook/media/tbook/covers", null=True, blank=True
    )

    def __str__(self):
        return self.grade

    def delete(self, *args, **kwargs):
        self.pdf.delete()
        self.cover.delete()
        super().delete(*args, **kwargs)

# Reference  Book models

class Rbook(models.Model):
    title = models.CharField(max_length=100)
    grade = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    desc = models.CharField(max_length=1000)
    uploaded_by = models.CharField(max_length=100, null=True, blank=True)
    pdf = models.FileField(upload_to="ebook/static/ebook/media/rbook/pdfs")
    cover = models.ImageField(
        upload_to="ebook/static/ebook/media/rbook/covers", null=True, blank=True
    )

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        self.pdf.delete()
        self.cover.delete()
        super().delete(*args, **kwargs)
    
# Quiz models 
class Quiz(models.Model):
    question = models.CharField(max_length=200,null=True)
    op1 = models.CharField(max_length=200,null=True)
    op2 = models.CharField(max_length=200,null=True)
    op3 = models.CharField(max_length=200,null=True)
    op4 = models.CharField(max_length=200,null=True)
    ans = models.CharField(max_length=200,null=True)
    
    def __str__(self):
        return self.question
