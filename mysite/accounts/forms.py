from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django_summernote.widgets import SummernoteWidget
from .models import Profile


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30,
                                 widget=forms.TextInput(
                                     attrs={
                                         'class': 'form-control mb-1',
                                         'placeholder': 'Enter First Name'}))
    last_name = forms.CharField(max_length=30,
                                widget=forms.TextInput(
                                    attrs={
                                        'class': 'form-control mb-1',
                                        'placeholder': 'Enter Last Name'}))
    username = forms.CharField(max_length=30,
                               widget=forms.TextInput(
                                   attrs={
                                       'class': 'form-control mb-1',
                                       'placeholder': 'Enter Username'}))
    email = forms.EmailField(max_length=30,
                             widget=forms.TextInput(
                                 attrs={
                                     'class': 'form-control mb-1',
                                     'placeholder': 'Enter your E-Mail'}))
    password1 = forms.CharField(max_length=30,
                                widget=forms.PasswordInput(
                                    attrs={
                                        'class': 'form-control mb-1',
                                        'placeholder': 'Enter password'}))
    password2 = forms.CharField(max_length=30,
                                widget=forms.PasswordInput(
                                    attrs={
                                        'class': 'form-control mb-1',
                                        'placeholder': 'Confirm Password'}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username',
                  'email', 'password1', 'password2',)


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=30, required=True,
                               widget=forms.TextInput(
                                   attrs={
                                       'class': 'form-control mb-1',
                                       'placeholder': 'Username'}))
    password = forms.CharField(max_length=30, required=True,
                               widget=forms.PasswordInput(
                                   attrs={
                                       'class': 'form-control mb-1',
                                       'placeholder': 'Password'}))
    remember_me = forms.BooleanField(required=False)

    class Meta:
        model = User
        fields = ['username', 'password', 'remember_me']


class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=30,
                               required=True,
                               widget=forms.TextInput(
                                   attrs={
                                       'class': 'form-control mb-1',
                                       'placeholder': 'Username'}))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(
                                 attrs={
                                     'class': 'form-control mb-1',
                                     'placeholder': 'Email'}))

    class Meta:
        model = User
        fields = ['username', 'email']


class UpdateProfileForm(forms.ModelForm):
    avatar = forms.ImageField(widget=forms.FileInput(
        attrs={'class': 'form-control mb-1'}))
    bio = forms.CharField(widget=SummernoteWidget(
        attrs={'class': 'form-control mb-1',
               'summernote': {
                   'placeholder': 'Enter text ...',
                   'width': '100%',
                   'height': '300px'}}))

    class Meta:
        model = Profile
        fields = ['avatar', 'bio']
