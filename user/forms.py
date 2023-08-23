from django import forms
from django.forms import widgets
from .models import *


class UserRegisterModelForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ["userid", "username", "password"]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class LoginForm(forms.Form):
    userid = forms.CharField(
        required=True,
        error_messages={
            "required": "账号不能为空"
        }
    )
    password = forms.CharField(
        required=True,
        error_messages={
            "required": "密码不能为空"
        }
    )


class PasswordForm(forms.Form):
    origin_password = forms.CharField(
        label="原密码",
        required=True,
        error_messages={
            "required": "原密码不能为空",
        },
        widget=widgets.PasswordInput()
    )
    new_password = forms.CharField(
        label="新密码",
        required=True,
        error_messages={
            "required": "密码不能为空",
        },
        widget=widgets.PasswordInput()
    )


class ProfileModelForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ["user"]

