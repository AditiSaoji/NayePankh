from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Campaign, Donation

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']

class CampaignForm(forms.ModelForm):
    class Meta:
        model = Campaign
        fields = ['title', 'description', 'goal_amount', 'current_amount']

class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = ['campaign', 'amount']
