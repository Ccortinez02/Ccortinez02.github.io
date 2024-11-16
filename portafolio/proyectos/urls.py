from django.urls import path
from .views import lista_proyectos

urlpatterns = [
    path('', lista_proyectos, name='lista_proyectos'),
]