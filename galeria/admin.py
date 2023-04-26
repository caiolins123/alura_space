from django.contrib import admin
from galeria.models import Fotografia

class ListandoFotografias(admin.ModelAdmin):
    list_display = ("id", "nome", "legenda", "descricao", "categoria", "foto", "publicada")
    list_display_links = ("id", "nome", "legenda", "descricao", "categoria", "foto")
    search_fields = ("nome", "id")
    list_filter = ("categoria",)
    list_editable = ("publicada",)
    list_per_page = 10

admin.site.register(Fotografia, ListandoFotografias)
