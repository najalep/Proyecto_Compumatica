from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from servicio.forms import CategoriaForm
from servicio.models import Categoria




class CategoriaListView(ListView):
    model = Categoria
    template_name = 'categoria/listar.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch( request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Categoria'
        context['create_url'] = reverse_lazy('categoria_create')
        return context


class CategoriaCreateView(CreateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'categoria/crear.html'
    success_url = reverse_lazy('categoria_list')



    def dispatch(self, request, *args, **kwargs):
        return super().dispatch( request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear Categoria'
        return context


class CategoriaUpdateView(UpdateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'categoria/modificar.html'
    success_url = reverse_lazy('categoria_list')


    def dispatch(self, request, *args, **kwargs):
        return super().dispatch( request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar Categoria'
        return context


class CategoriaDeleteView(DeleteView):
    model = Categoria
    template_name = 'categoria/eliminar.html'
    success_url = reverse_lazy('categoria_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar Categoria'
        return context
