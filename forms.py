from django import forms

class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password=forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Password'}))

class CreateUser(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password=forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Password'}))
    name=forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    surname=forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Surname'}))