from django import forms

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