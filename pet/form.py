from django import forms
from django.forms import widgets as widget
from .models import *


class PetModelForm(forms.ModelForm):
    class Meta:
        model = Pet
        exclude = ["adopt_status"]

        widgets = {
            "sex": widget.RadioSelect(),
            "neutered": widget.RadioSelect(),
            "birthday": widget.TextInput(attrs={"id": "date"})
        }


class PetImageModelForm(forms.ModelForm):
    class Meta:
        model = PetImage
        fields = "__all__"
