from django.conf.urls import url
from .views import TwitterComentariosAPI

urlpatterns = [
    url(r'^dataset/$', TwitterComentariosAPI.as_view()),
]
