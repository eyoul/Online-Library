from django import forms
from django.forms import ModelForm
from .models import *


# Reference book Form model

class RbookForm(ModelForm):
    class Meta:
        model = Rbook
        fields = "__all__"
# Text book Form model 
class TbookForm(ModelForm):
    class Meta:
        model = Tbook
        fields = "__all__"

# Quiz form Model

class addQuestionform(ModelForm):
    class Meta:
        model = Quiz
        fields = "__all__"