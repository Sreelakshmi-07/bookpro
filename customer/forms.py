from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


class UserRegistrationForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        ]
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "password": forms.PasswordInput(attrs={"class": "form-control"})
        }


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'max-width=300px'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'style': 'max-width=300px'}))


# class PasswordResetForm(forms.Form):
#     old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'style': 'max-width=300px'}))
#     new_password = forms.CharField(
#         widget=forms.PasswordInput(attrs={'class': 'form-control', 'style': 'max-width=300px'}))
#     confirm_password = forms.CharField(
#         widget=forms.PasswordInput(attrs={'class': 'form-control', 'style': 'max-width=300px'}))
#
#     def clean(self):
#         cleaned_data = super().clean()
#         newpassword = cleaned_data.get('newpassword')
#         confirmpassword = cleaned_data.get('confirmpassword')
#         if newpassword != confirmpassword:
#             msg = "Password mismatch"
#             self.add_error("newpassword", msg)

class PasswordRestForm(forms.Form):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'style': 'max-width=300px'}))
    new_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'style': 'max-width=300px'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'style': 'max-width=300px'}))


