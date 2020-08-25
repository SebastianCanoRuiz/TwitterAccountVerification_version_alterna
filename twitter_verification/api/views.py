# api/views.py
from django.shortcuts import render
from rest_framework import generics
from cuentas_falsas.models import DatosComentarios
from .serializers import ComentariosTwitterSerializer

# Create your views here.
class TwitterComentariosAPI(generics.ListCreateAPIView):
    queryset = DatosComentarios.objects.all()
    serializer_class = ComentariosTwitterSerializer