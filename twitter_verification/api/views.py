# api/views.py
from django.shortcuts import render
from cuentas_falsas.models import DatosComentarios
from .serializers import ComentariosTwitterSerializer

import os
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import viewsets
from django.http import JsonResponse

from pandas import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.cluster import KMeans
#import matplotlib.pyplot as plt

# Create your views here.


class TwitterComentariosAPI(generics.ListCreateAPIView):
    queryset = DatosComentarios.objects.all()
    serializer_class = ComentariosTwitterSerializer


def generarKmeans(*args, **kwargs):
    perfil = 'jsh7590cr'
    comentario = 'el peluca sabpeeee :3'
    cant_palabras = 4.0
    comentarios_repetidos = 0.0
    insultos = 0.0
    emoticones = 1.0
    multimedia = 0.0
    links = 0.0
    comentarios_raros = 0.0

    # Dataframe de una linea para testear el etiquetado
    df = pd.read_csv(r'Z:/datos2.csv')

    nuevoDF = pd.DataFrame([[perfil, comentario, cant_palabras, comentarios_repetidos,
                            insultos, emoticones, multimedia, links, comentarios_raros]])
    nuevoDF = nuevoDF.rename(columns={0: 'perfil', 1: 'comentario', 2: 'cant_palabras', 3: 'comentarios_repetidos',
                                    4: 'insultos', 5: 'emoticones', 6: 'multimedia', 7: 'links', 8: 'comentarios_raros'})

    # Se agregan al dataset original para normalizar (Bueno, se crea una copia)
    df_n = df.append(nuevoDF)

    # Normalizar la copia del dataframe
    df_n = df_n.drop('perfil', 1)
    df_n = df_n.drop('comentario', 1)
    df_n = df_n.drop('label', 1)
    df_n = df_n.reset_index(drop=True)

    #  Normalización dataset de prueba para nuevos datos
    min_max_scaler = preprocessing.MinMaxScaler()
    df_escalado_nuevo = min_max_scaler.fit_transform(df_n)
    # Hay que convertir a DF el resultado.
    df_escalado_nuevo = pd.DataFrame(df_escalado_nuevo)
    df_escalado_nuevo = df_escalado_nuevo.rename(
        columns={0: 'cant_palabras', 1: 'comentarios_repetidos', 2: 'insultos', 3: 'emoticones', 4: 'multimedia', 5: 'links', 6: 'comentarios_raros'})

    #  datos normalizados
    cant_palabras_n = df_escalado_nuevo['cant_palabras'][2603]
    comentarios_repetidos_n = df_escalado_nuevo['comentarios_repetidos'][2603]
    insultos_n = df_escalado_nuevo['insultos'][2603]
    emoticones_n = df_escalado_nuevo['emoticones'][2603]
    multimedia_n = df_escalado_nuevo['multimedia'][2603]
    links_n = df_escalado_nuevo['links'][2603]
    comentarios_raros_n = df_escalado_nuevo['comentarios_raros'][2603]

    #  Tupla nueva
    X_new = np.array([[cant_palabras_n, comentarios_repetidos_n, insultos_n,
                    emoticones_n, multimedia_n, links_n, comentarios_raros_n]])

    kmeans = KMeans(n_clusters=2).fit(df_escalado_nuevo)
    centroids = kmeans.cluster_centers_

    new_labels = kmeans.predict(X_new)

    data = list({new_labels})
    return JsonResponse(data, safe=False)
