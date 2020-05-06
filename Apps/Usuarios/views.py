from django.shortcuts import render, HttpResponse, redirect
from .forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate, login
from Apps.Reproduccion import views as views_reproduccion
from Apps.Artista import views as views_artista
from Apps.Usuarios.models import User

# Create your views here.

def home(request):
    return render(request, 'main.html')

def loginn(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(views_artista.home)
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
        form = RegisterForm(request.POST, request.FILES)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            fechaNacimiento = form.cleaned_data['fechaNacimiento']
            pais = form.cleaned_data['pais']
            foto = form.cleaned_data['foto']
            isArtist = form.cleaned_data['isArtist']

            user = User.objects.filter(username=username)
            emailUser = User.objects.filter(email=email)

            if(len(user)>0):
                form.add_error('username', 'Este nombre de usuario ya existe.')
                return render(request, 'register.html', {'form':form})

            if(len(emailUser)>0):
                form.add_error('email', 'Esta direccion de correo electronico ya existe.')
                return render(request, 'register.html', {'form':form})

            user = User(
                username = username,
                email = email,
                first_name = name,
                last_name = last_name,
                fechaNacimiento = fechaNacimiento,
                pais = pais,
                foto = foto,
                isArtist = isArtist,
            )
            user.set_password(password)
            user.save()
            form.add_error(None, 'Usuario creado exitosamente.')
            return render(request, 'register.html', {'form':form})

        else:
            return render(request, 'register.html', {'form':form})
    else:
        form = RegisterForm()
        return render(request, 'register.html', {'form':form})