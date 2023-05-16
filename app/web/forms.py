from django.forms import TextInput, PasswordInput, Form, CharField
from django import forms

from app.models import MyUser



class LoginForm(Form):
    username = CharField(widget=TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Логин',
        'required': True
    }
    ))
    password = CharField(widget=PasswordInput(attrs={
        'class': 'form-control mt-2',
        'placeholder': 'Пароль',
        'required': True
    }
    ))


# class UserUpdateForm(forms.ModelForm):
#     """
#     Форма обновления данных пользователя
#     """
#
#     class Meta:
#         model = MyUser
#         fields = ('tele_name', 'tele_username', 'email')


class UserUpdateForm(forms.ModelForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = MyUser
        fields = ['username', 'tele_username', 'email']


