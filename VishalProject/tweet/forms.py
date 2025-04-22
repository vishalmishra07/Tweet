from django import forms
from .models import Tweet
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Tweetform(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['text', 'photo']
        widgets = {
            'text': forms.Textarea(attrs={
                'class': 'form-control form-control-sm bg-dark text-light border border-secondary rounded-3 shadow-sm',
                'rows': 3,
                'placeholder': "What's on your mind?"
            }),
            'photo': forms.ClearableFileInput(attrs={
                'class': 'form-control form-control-sm bg-dark text-light border border-secondary rounded-3 shadow-sm'
            }),
        }
        
class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('username','email','password1','password2')