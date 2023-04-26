from django import forms

class UsuarioFormulario(forms.Form):
    nombre= forms.CharField()
    email= forms.EmailField()
    telefono = forms.IntegerField()