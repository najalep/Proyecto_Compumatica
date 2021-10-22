
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from servicio.forms import *
from servicio.models import *
from django.db.models import Q


class FacturaCreateView(CreateView):
    model = Factura
    form_class = FacturaForm
    template_name = 'factura/create.html'
    success_url = reverse_lazy('index')

    # def post(self, request, *args, **kwargs):
    #     form = ClientForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return HttpResponseRedirect(self.success_url)
    #     self.object = None
    #     context = self.get_context_data(**kwargs)
    #     context['form'] = form
    #     return render(request,self.template_name,context)
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch( request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'search_maint':
                data=[]
                m= Articulo.objects.filter(code__icontains= request.POST['term'])[0:10]
                for i in m:
                    item = i.toJSON()
                    item['value']= i.code
                    data.append(item)


            elif action == 'search_cliente':
                data=[]
                m= Client.objects.filter(cedula__icontains= request.POST['term'])[0:10]
                for i in m:
                    item = i.toJSON()
                    item['value']= i.cedula
                    data.append(item)
            else:
                data['error'] = 'No ha ingresada ninguna opcion'
        except Exception as e:
            data['error']= str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear una factura'
        return context





































