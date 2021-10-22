from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from servicio.forms import ArticuloForm
from servicio.models import Articulo


class ArticuloListView(ListView):
    model = Articulo
    template_name = 'articulo/listar.html'

    @method_decorator(csrf_exempt)

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch( request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Articulo'
        context['create_url'] = reverse_lazy('articulo_create')
        return context


class ArticuloCreateView(CreateView):
    model = Articulo
    form_class = ArticuloForm
    template_name = 'articulo/crear.html'
    success_url = reverse_lazy('articulo_list')

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch( request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear Articulo'
        return context


class ArticuloUpdateView(UpdateView):
    model = Articulo
    form_class = ArticuloForm
    template_name = 'articulo/modificar.html'
    success_url = reverse_lazy('articulo_list')


    def dispatch(self, request, *args, **kwargs):
        return super().dispatch( request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar Articulo'
        return context


class ArticuloDeleteView(DeleteView):
    model = Articulo
    template_name = 'articulo/eliminar.html'
    success_url = reverse_lazy('articulo_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar Articulo'
        return context
