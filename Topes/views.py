from django.views.generic import ListView
from django.shortcuts import render

from .models import Procedimiento, ObjetoContratacion

# def procedimientos_listado(request):
#     procedimientos = Procedimiento.objects.all()
#     objetos = Objeto.objects.all()
#     return render(request, 'Topes/procedimientos_listado.html', {'objetos': objetos})
#
# # def objetos_listado(request):
# #     objetos = Objeto.objects.all()
# #     return render(request, 'Topes/procedimientos_listado.html', {'objetos': objetos})

class ProcedimientosListado(ListView):
    model =  Procedimiento
    template_name = 'Topes/procedimientos_listado.html'

    def get_queryset(self):
        procedimientos = ObjetoContratacion.objects.all()
        return procedimientos

    def get_context_data(self, **kwargs):
        contexto = super(ProcedimientosListado, self).get_context_data(**kwargs)
        contexto['tipos'] = self.get_queryset()
        return contexto