from django import forms
from django.forms import widgets as widget
from .models import *


class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content"]