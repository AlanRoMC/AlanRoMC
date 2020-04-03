from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, min_length=5, label='Usuario',required=True, widget=forms.TextInput(attrs={'placeholder':'Ingresa tu usuario', 'class':'form-control'}))
    password = forms.CharField(max_length=50, min_length=5, label='Contraseña',required=True, widget=forms.PasswordInput(attrs={'placeholder':'Ingresa tu contraseña', 'class':'form-control'}))

class RegisterForm(ModelForm):
    class Meta:
        model = User
        fields = ['username','password','email','first_name','last_name']
        widgets = {
            'username' : forms.TextInput(attrs={'class':'form-control','placeholder':'Ingresa el nombre de usuario deseado.'}),
            'password' : forms.PasswordInput(attrs={'class':'form-control','placeholder':'Ingresa una contraseña con minimo 8 caracteres.'}),
            'email' : forms.TextInput(attrs={'class':'form-control','placeholder':'****@****.com'}),
            'first_name' : forms.TextInput(attrs={'class':'form-control'}),
            'last_name' : forms.TextInput(attrs={'class':'form-control'})
        }
        help_texts = {
            'username' : 'Maximo 150 caracteres',
            'password' : 'Minimo 8 caracteres'
        }