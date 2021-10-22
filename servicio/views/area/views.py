from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from servicio.forms import AreaForm
from servicio.models import Area




class AreaListView(ListView):
    model = Area
    template_name = 'area/listar.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch( request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Areas'
        context['create_url'] = reverse_lazy('area_create')
        return context


class AreaCreateView(CreateView):
    model = Area
    form_class = AreaForm
    template_name = 'area/crear.html'
    success_url = reverse_lazy('area_list')



    def dispatch(self, request, *args, **kwargs):
        return super().dispatch( request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear Area'
        return context


class AreaUpdateView(UpdateView):
    model = Area
    form_class = AreaForm
    template_name = 'area/modificar.html'
    success_url = reverse_lazy('area_list')


    def dispatch(self, request, *args, **kwargs):
        return super().dispatch( request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar Area'
        return context


class AreaDeleteView(DeleteView):
    model = Area
    template_name = 'area/eliminar.html'
    success_url = reverse_lazy('area_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar Area'
        return context
