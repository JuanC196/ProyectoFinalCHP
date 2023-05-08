from django import forms
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User 

class UsuarioFormulario(forms.Form):
    nombre= forms.CharField()
    email= forms.EmailField()
    telefono = forms.IntegerField()

class ComentarioFormulario(forms.Form):
    nombre= forms.CharField()
    email = forms.EmailField()
    telefono = forms.IntegerField()
    texto= forms.CharField() 

class VehiculoFormulario(forms.Form):
    marca= forms.CharField()
    tipo = forms.CharField()
    modelo= forms.IntegerField()
    precio= forms.IntegerField()

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

        help_texts = {k:"" for k in fields}