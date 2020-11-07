from django.urls import path
from .views import Home, carreras_view,carreras_detail, instalaciones, noticias

app_name = 'cole'

urlpatterns = [
    path('', Home, name='home'),
    path('carreras/',carreras_view, name='carreras'), 
    path('carreras/view/<int:carrera_id>',carreras_detail, name='detail'),
    path('instalaciones/',instalaciones, name='instalaciones'), 
    path('noticias/',noticias, name='noticias'), 
]
