from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import User


__author__ = "Sidon"
__date__ = "Created by 03/09/2018"
__email__ = "sidoncd@gmail.com"


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Senha', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Password confirmations', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'name',)

    def clean_password2(self):

        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords are not the same.")
        return password2

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(label="Password",
                                         help_text="To change password"
                                                   "use <a href=\"../password/\">this link</a>.")

    class Meta:
        model = User
        fields = (
            'email', 'password', 'name', 'user_permissions', 'is_active', 'is_superuser'
        )

    def clean_password(self):
        return self.initial["password"]
