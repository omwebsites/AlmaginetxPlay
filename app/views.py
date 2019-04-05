# Create your view here.
from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.http import HttpResponseBadRequest, HttpResponse, HttpRequest, HttpResponseRedirect
from django.core import serializers
from django.shortcuts import redirect
from django.core.urlresolvers import reverse, reverse_lazy
from django.views import generic
from django.conf import settings
from .forms import signup_form, uploadtrack_form, updateavatar_form
from .models import *
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.utils import timezone
import re
from django.db.models import Q
from django.core.context_processors import csrf
from django import forms 
from django.middleware.csrf import CsrfViewMiddleware, get_token
from django.utils.decorators import available_attrs, decorator_from_middleware
from django.template import RequestContext

def login_view(request):
    # Si el usuario esta ya logueado, lo redireccionamos a index_view
    if request.user.is_authenticated():
        return redirect(reverse('app.welcome'))
    message = ''
    userprofile = UserProfile.objects.all().order_by('-create_at')
    track = Track.objects.all().order_by('-create_at')
    now = timezone.now()
    template = 'app/login.html'
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect(reverse('app.login'))
            else:
                # Redireccionar informando que la cuenta esta inactiva
                # Lo dejo como ejercicio al lector :)
                pass
        message = 'Invalid Email or Password. Try again'
    return render_to_response(template,locals(),context_instance=RequestContext(request))

def signup_view(request):
    # Si el usuario esta ya logueado, lo redireccionamos a index_view
    if request.user.is_authenticated():
        return redirect(reverse('app.login'))
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(signup_view, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        return context
    if request.method == 'POST':
        # Si el method es post, obtenemos los datos del formulario
        form = signup_form(request.POST, request.FILES)
        # Comprobamos si el formulario es valido
        if form.is_valid():
            # En caso de ser valido, obtenemos los datos del formulario.
            cleaned_data = form.cleaned_data
            username = cleaned_data.get('username')
            password = cleaned_data.get('password')
            password2 = cleaned_data.get('password2')
            nickname = cleaned_data.get('nickname')
            # E instanciamos un objeto User, con el username y password
            user_model = User.objects.create_user(username=username, password=password)
            # Y guardamos el objeto, esto guardara los datos en la db.
            user_model.save()
            # Ahora, creamos un objeto UserProfile
            user_profile = UserProfile()
            # Al campo user le asignamos el objeto user_model
            user_profile.user = user_model
            user_profile.nickname = nickname
            user_profile.password2 = password2
            user_profile.save()
            # Ahora, redireccionamos a la pagina
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect(reverse('app.welcome'), {'nickname': nickname})
                else:
                    # Redireccionar informando que la cuenta esta inactiva
                    pass
                message = 'Usuario incorrecto'
                return render(request, 'app/signup.html', {'message': message})
    else:
        # Si el mthod es GET, instanciamos un objeto RegistroUserForm vacio
        form = signup_form()
    # Creamos el contexto
    context = {'form': form}
    context['userprofile'] = UserProfile.objects.all()
    # Y mostramos los datos
    return render(request, 'app/signup.html', context)

@login_required
def welcome_view(request):
    track = Track.objects.all().order_by('-create_at')
    userprofile = UserProfile.objects.all().order_by('-create_at')
    template = 'app/welcome.html'
    return render_to_response(template,locals(),context_instance=RequestContext(request))

def us_view(request):
    template = 'app/us.html'
    return render_to_response(template,locals(),context_instance=RequestContext(request))

def logout_view(request):
    logout(request)
    messages.success(request, 'Ingresa para continuar')
    return redirect(reverse('app.login'))

@login_required
def uploadtrack_view(request):
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(uploadtrack_view, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        return context
    if request.method == 'POST':
        # Si el method es post, obtenemos los datos del formulario
        form = uploadtrack_form(request.POST, request.FILES)
        # Comprobamos si el formulario es valido
        if form.is_valid():
            # En caso de ser valido, obtenemos los datos del formulario.
            cleaned_data = form.cleaned_data
            title = cleaned_data.get('title')
            audio = cleaned_data.get('audio')
            # E instanciamos un objeto User, con el username y password
        #    user_model = User.objects.create_user(username=username, password=password)
            # Y guardamos el objeto, esto guardara los datos en la db.
        #    user_model.save()
            # Ahora, creamos un objeto UserProfile
            track = Track()
            # Al campo user le asignamos el objeto user_model
           #track user_profile.user = user_model
            track.title = title
            track.audio = audio
            track.user = request.user
            track.save()
            message = 'Audio upload success'
            return redirect(reverse('app.welcome'), {'message': message})
            # Ahora, redireccionamos a la pagina
            #user = authenticate(username=username, password=password)
            #if user is not None:
             #   if user.is_active:
              #      login(request, user)
               #     return redirect(reverse('app.welcome'), {'nickname': nickname})
                #else:
                    # Redireccionar informando que la cuenta esta inactiva
                 #   pass
                #message = 'Usuario incorrecto'
    else:
        # Si el mthod es GET, instanciamos un objeto RegistroUserForm vacio
        form = uploadtrack_form()
    # Creamos el contexto
    context = {'form': form}
    context['userprofile'] = UserProfile.objects.all()
    # Y mostramos los datos
    return render(request, 'app/uploadtrack.html', context)

def track_view(request, slug):
    template = 'app/track.html'
    track = Track.objects.get(slug = slug)
    return render_to_response(template,locals(),context_instance=RequestContext(request))

def userprofile_view(request, slug):
    template = 'app/userprofile.html'
    userprofile = UserProfile.objects.get(slug = slug)
    track = Track.objects.all().order_by('-create_at')
    return render_to_response(template,locals(),context_instance=RequestContext(request))

@login_required
def updateavatar_view(request, slug):
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context['userprofile'] = UserProfile.objects.get(slug=slug)
        context = super(updateavatar_view, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        return context
    if request.method == 'POST':
        # Si el method es post, obtenemos los datos del formulario
        form = updateavatar_form(request.POST, request.FILES)
        # Comprobamos si el formulario es valido
        if form.is_valid():
            # En caso de ser valido, obtenemos los datos del formulario.
            cleaned_data = form.cleaned_data
            avatar = cleaned_data.get('avatar')
            request.user.userprofile.avatar = avatar
            request.user.userprofile.save()
            message = 'Picture update success'
            return redirect(reverse('app.welcome'), {'message': message})
    else:
        # Si el mthod es GET, instanciamos un objeto RegistroUserForm vacio
        form = updateavatar_form()
    # Creamos el contexto
    context = {'form': form}
    context['userprofile'] = UserProfile.objects.get(slug=slug)
    # Y mostramos los datos
    return render(request, 'app/updateavatar.html', context)