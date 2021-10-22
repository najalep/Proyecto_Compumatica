from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from servicio.forms import MarcaForm
from servicio.models import Marca


class MarcaListView(ListView):
    model = Marca
    template_name = 'marca/listar.html'

    @method_decorator(csrf_exempt)

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch( request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Marca'
        context['create_url'] = reverse_lazy('marca_create')
        return context


class MarcaCreateView(CreateView):
    model = Marca
    form_class = MarcaForm
    template_name = 'marca/crear.html'
    success_url = reverse_lazy('marca_list')

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch( request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear Marca'
        return context


class MarcaUpdateView(UpdateView):
    model = Marca
    form_class = MarcaForm
    template_name = 'marca/modificar.html'
    success_url = reverse_lazy('marca_list')


    def dispatch(self, request, *args, **kwargs):
        return super().dispatch( request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar Marca'
        return context


class MarcaDeleteView(DeleteView):
    model = Marca
    template_name = 'marca/eliminar.html'
    success_url = reverse_lazy('marca_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar Marca'
        return context
