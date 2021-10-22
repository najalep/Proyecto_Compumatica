from django.contrib.auth.views import LoginView,LogoutView
from django.shortcuts import render, redirect


# Create your views here.

class LoginFormView(LoginView):
    template_name = 'login.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('index')
        return super().dispatch(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super(LoginFormView, self).get_context_data(**kwargs)
        context['title'] = 'Iniciar sesion'
        return context

