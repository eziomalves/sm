from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('busca_data', views.busca_data, name='busca_data'),
    path('lista_indice', views.lista_indice, name='lista_indice'),
    path('contato', views.contato, name='contato')
]
