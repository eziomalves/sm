from django.contrib import admin
from .models import Concentracao, Indice
# Register your models here.
@admin.register(Concentracao)
class ConcentracaoAdmin(admin.ModelAdmin):
    list_display = ['data', 'c_mp10', 'c_mp25']

@admin.register(Indice)
class indiceAdmin(admin.ModelAdmin):
    list_display = ['data', 'indice_mp25', 'indice_mp10','classificacao']
