from rest_framework import serializers
from cuentas_falsas.models import DatosComentarios


class ComentariosTwitterSerializer(serializers.ModelSerializer):
    class Meta:
        model = DatosComentarios
        fields = [
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
