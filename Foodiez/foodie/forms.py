
from django import forms
from django.contrib.auth import get_user_model
from .models import Recipe,Ingrediant,Category

User = get_user_model()

class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username","password","first_name","last_name","email"]
        widgets = {
            "password": forms.PasswordInput(),
        }


# Login Form 
class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput())

