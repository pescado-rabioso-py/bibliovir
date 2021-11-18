from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import *
from .formsets import FormsetAutor

urlpatterns = [
	path('inicio_autor/',InicioAutor.as_view(),name='inicio_autor'),
	path('crear_autor/',CrearAutor.as_view(),name='crear_autor'),
	path('listado_autor/',ListadoAutor.as_view(),name='listar_autor'),
	path('editar_autor/<int:pk>',ActualizarAutor.as_view(),name='editar_autor'),
	path('eliminar_autor/<int:pk>',EliminarAutor.as_view(),name='eliminar_autor'),
	path('inicio_libro/',InicioLibro.as_view(),name='inicio_libro'),
	path('crear_libro/',CrearLibro.as_view(),name='crear_libro'),
	path('listado_libros/',ListadoLibros.as_view(),name='listar_libros'),
	path('editar_libros/<int:pk>',ActualizarLibro.as_view(),name='editar_libro'),
	path('eliminar_libros/<int:pk>',EliminarLibro.as_view(),name='eliminar_libro'),
	path('crear_autor_formset',FormsetAutor.as_view(),name='crear_autor_formset'),
]