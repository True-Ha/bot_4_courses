from django.forms import TextInput, PasswordInput, Form, CharField


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

