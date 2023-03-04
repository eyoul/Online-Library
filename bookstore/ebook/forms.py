from django import forms
from django.forms import ModelForm
from .models import *

class RbookForm(ModelForm):
    class Meta:
        model = Rbook
        fields = "__all__"
class TbookForm(ModelForm):
    class Meta:
        model = Tbook
        fields = "__all__"

class addQuestionform(ModelForm):
    class Meta:
        model = Quiz
        fields = "__all__"