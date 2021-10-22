from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from servicio.forms import ClientForm
from servicio.models import Client




class ClientListView(ListView):
    model = Client
    template_name = 'cliente/listar.html'

    @method_decorator(csrf_exempt)

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch( request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Cliente'
        context['create_url'] = reverse_lazy('client_create')
        return context


class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    template_name = 'cliente/crear.html'
    success_url = reverse_lazy('client_list')

    # def post(self, request, *args, **kwargs):
    #     form = ClientForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return HttpResponseRedirect(self.success_url)
    #     self.object = None
    #     context = self.get_context_data(**kwargs)
    #     context['form'] = form
    #     return render(request,self.template_name,context)

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch( request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear Cliente'
        return context


class ClientUpdateView(UpdateView):
    model = Client
    form_class = ClientForm
    template_name = 'cliente/modificar.html'
    success_url = reverse_lazy('client_list')


    def dispatch(self, request, *args, **kwargs):
        return super().dispatch( request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar Cliente'
        return context


class ClientDeleteView(DeleteView):
    model = Client
    template_name = 'cliente/eliminar.html'
    success_url = reverse_lazy('client_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar Cliente'
        return context
