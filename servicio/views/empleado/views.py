from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from servicio.forms import EmpleadoForm
from servicio.models import Empleado


class EmpleadoListView(ListView):
    model = Empleado
    template_name = 'empleado/listar.html'

    @method_decorator(csrf_exempt)

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch( request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Empleado'
        context['create_url'] = reverse_lazy('empleado_create')
        return context


class EmpleadoCreateView(CreateView):
    model = Empleado
    form_class = EmpleadoForm
    template_name = 'empleado/crear.html'
    success_url = reverse_lazy('empleado_list')

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch( request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear Empleado'
        return context


class EmpleadoUpdateView(UpdateView):
    model = Empleado
    form_class = EmpleadoForm
    template_name = 'empleado/modificar.html'
    success_url = reverse_lazy('empleado_list')


    def dispatch(self, request, *args, **kwargs):
        return super().dispatch( request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar Empleado'
        return context


class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = 'empleado/eliminar.html'
    success_url = reverse_lazy('empleado_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar Empleado'
        return context
