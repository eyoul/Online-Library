from django import forms
from django.forms import ModelForm
from .models import Rbook
class RbookForm(ModelForm):
    class Meta:
        model = Rbook
        fields = "__all__"