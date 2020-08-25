from django.contrib import admin
from .models import DatosComentarios

class DatosComentariosAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'perfil',
        'comentario',
        'cantidad_palabras',
        'comentarios_repetidos',
        'insultos',
        'emoticones',
        'multimedia',
        'links',
        'comentarios_raros',
        'label',
    ]
    search_fields = [
        'perfil',
        'comentario',
    ]
    list_editable = [
        'comentario',
    ]

# Register your models here.
admin.site.register(DatosComentarios, DatosComentariosAdmin)
