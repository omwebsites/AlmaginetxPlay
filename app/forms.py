# Create your forms here.
# -*- encoding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User

class signup_form(forms.Form):
    username = forms.EmailField(
        label='Email',
        min_length=1,
        widget=forms.EmailInput(attrs={'class': 'form-control'}))
    nickname = forms.CharField(
        label='Nickname',
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
    def clean_email(self):
        """Comprueba que no exista un email igual en la db"""
        nickname = self.cleaned_data['nickname']
        if User.objects.filter(nickname=nickname):
            raise forms.ValidationError('Nickname already exist')
        return nickname
