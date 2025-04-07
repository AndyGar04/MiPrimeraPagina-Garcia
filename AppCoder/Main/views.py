# from django.http import HttpResponse
from django.contrib import messages

from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import LoginForm, RegisterForm

"""
    Para crear el login_not_required, podemos optar por crear un archivo llamado decorators, 
sin embargo, utilizare una funcion aqui.
"""


def login_not_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        return view_func(request, *args, **kwargs)
    return _wrapped_view


@login_not_required
def index(request):
    return render(request, "Main/index.html")


@login_not_required
def about(request):
    return render(request, "Main/about.html")


class MiLoginView(LoginView):
    template_name = "Main/login.html"
    authentication_form = LoginForm
    next_page = reverse_lazy("Main:index")

    def form_valid(self, form):
        usuario = form.get_user()
        messages.success(self.request, f"Inicio de sesión exitoso. ¡Bienvenido {usuario.username}!")
        return super().form_valid(form)


class MiRegisterView(CreateView):
    form_class = RegisterForm
    template_name = "Main/register.html"
    success_url = reverse_lazy("Main:login")

    def form_valid(self, form):
        messages.success(self.request, f"Registro exitoso. Ahora puedes iniciar sesión")
        return super().form_valid(form)