# api/views.py
from django.shortcuts import render
from cuentas_falsas.models import DatosComentarios
from .serializers import ComentariosTwitterSerializer

from rest_framework.response import Response
from rest_framework import generics
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import viewsets
from django.http import JsonResponse

# from pandas import pandas as pd
# import numpy as np
# from sklearn import preprocessing 
# from sklearn.cluster import KMeans
# import matplotlib.pyplot as plt

# Create your views here.
class TwitterComentariosAPI(generics.ListCreateAPIView):
    queryset = DatosComentarios.objects.all()
    serializer_class = ComentariosTwitterSerializer

def generarKmeans(*args, **kwargs):
    # def getMoodData(*args, **kwargs):
    # #numberMood = switch(kwargs.get('mood'))
    # mood = kwargs.get('mood')
    # queryset = NewVideo.objects.filter(labeled__exact=True).filter(predicted_moods__iexact=mood)
    # data = list(queryset.values("video_id", "video_title", "predicted_moods", "video_type"))

    dicc = {2,'dos', 'ocho',  4}
    data = list( dicc)
    return JsonResponse(data, safe=False)