from django.conf.urls import url


from .views import *

urlpatterns = (
    # url(r'^$', views.procedimientos_listado, name='procedimientos_listado'),
    url(r'^$', ProcedimientosListado.as_view(), name='procedimientos_listado'),
)