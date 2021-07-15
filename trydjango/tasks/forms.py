# from .models import UserLogin
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



# class UserLoginForm(AuthenticationForm):
#     # username = forms.CharField(label = 'email', widget = forms.EmailInput)  
#     class Meta:
#         model = User
#         fields = ['email']

class UserSignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','last_name' ]

        labels = { 'last_name':'address', 'password confirmation': 'Confirm Password'}
        # widgets = {'password':forms.PasswordInput(render_value=True) }


