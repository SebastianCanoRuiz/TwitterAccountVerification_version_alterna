from django.conf.urls import url
from .views import TwitterComentariosAPI, generarKmeans

#Contiene las urls de consulta de la API
urlpatterns = [
    url(r'^dataset/$', TwitterComentariosAPI.as_view()),
    url(r'^datos-twitter/(?P<cantidad_palabras>[^/]+)/(?P<comentarios_repetidos>[^/]+)/(?P<insultos>[^/]+)/(?P<emoticones>[^/]+)/(?P<multimedia>[^/]+)/(?P<links>[^/]+)/(?P<comentarios_raros>[^/]+)$', generarKmeans),
    
    
    #url(r'^songs-genre-mood/(?P<genre>[^/]+)/(?P<mood>[^/]+)/$', getGenreMoodData),
]
