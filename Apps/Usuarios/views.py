from django.shortcuts import render, HttpResponse, redirect
from .forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate, login
from Apps.Reproduccion import views as views_reproduccion
from django.contrib.auth.models import User

# Create your views here.

def loginn(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(views_reproduccion.home)
            else:
                form.add_error(None, 'Verifica que tus datos sean correctos')
                return render(request, 'login.html', {'form': form})
        else:
            return HttpResponse('Revisa si tu formulario fue llenado correctamente.')
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            nombre = form.cleaned_data['first_name']
            apellido = form.cleaned_data['last_name']

            user, created = User.objects.get_or_create(
                username = username,
                email = email
            )

            if created:
                form.add_error(None, 'Usuario creado exitosamente.')
            else:
                return render(request, 'register.html', {'form':form})    

        else:
            return render(request, 'register.html', {'form':form})
    else:
        form = RegisterForm()
        return render(request, 'register.html', {'form':form})