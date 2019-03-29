# Create your forms here.
# -*- encoding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User
from .models import UserProfile, Track

class signup_form(forms.Form):
    username = forms.EmailField(
        label='Email',
        min_length=1,
        widget=forms.EmailInput(attrs={'class': 'form-control'}))
    nickname = forms.CharField(
        label='Alias',
        min_length=1,
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(
        label='Password',
        min_length=3,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(
        label='Repeat Password',
        min_length=3,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    def clean_username(self):
        """Comprueba que no exista un username igual en la db"""
        username = self.cleaned_data['username']
        if User.objects.filter(username=username):
            raise forms.ValidationError('Email already exist')
        return username
    def clean_nickname(self):
        """Comprueba que no exista un email igual en la db"""
        nickname = self.cleaned_data['nickname']
        if UserProfile.objects.filter(nickname=nickname):
            raise forms.ValidationError('Nickname already exist')
        return nickname
    def clean_password2(self):
        """Comprueba que password y password2 sean iguales."""
        password = self.cleaned_data['password']
        password2 = self.cleaned_data['password2']
        if password != password2:
            raise forms.ValidationError('Make sure your password match')
        return password2

class uploadtrack_form(forms.Form):
    title = forms.CharField(
        label='Audio title',
        widget=forms.Textarea(attrs={'class': 'form-control'}))
    audio = forms.FileField(
        label='Audio')

class updateavatar_form(forms.Form):
    avatar = forms.FileField(
        label='Picture')