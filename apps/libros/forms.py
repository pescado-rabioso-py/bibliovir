from django import forms
from django.core.exceptions import ValidationError
from .models import Autor,Libro

class AutorForm(forms.ModelForm):
	class Meta:
		model = Autor
		fields = ['nombre','apellidos']
		labels = {
			'nombre': 'Nombre del autor',
			'apellidos': 'Apellidos del autor',
			'nacionalidad': 'Nacionalidad del autor',
			'descripcion': 'Pequeña descripcion',
		}
		widgets = {
			'nombre': forms.TextInput(
				attrs ={
					'class':'form-control',
					'placeholder':'Ingrese el nombre del autor'
				}
			),
			'apellidos': forms.TextInput(
				attrs = {
					'class':'form-control',
					'placeholder':'Ingrese los apellidos del autor'
				}
			),
			'nacionalidad':forms.TextInput(
				attrs = {
					'class':'form-control',
					'placeholder':'Ingrese una nacionalidad para el autor'
				}
			),
			'descripcion':forms.Textarea(
				attrs = {
					'class':'form-control',
					'placeholder': 'Ingrese una pequeña descripcion para el autor'
				}
			)
		}

class LibroForm(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['autor'].queryset = Autor.objects.filter(estado = True)


	class Meta:
		model = Libro
		fields = ('titulo','autor','fecha_publicacion','descripcion','imagen','cantidad')
		label = {
			'titulo':'Titulo del libro',
			'autor_id':'Autor(es) del libro',
			'fecha_publicacion':'Fecha de publicacion del Libro'
		}
		widgets = {
			'titulo': forms.TextInput(
				attrs = {
					'class': 'form-control',
					'placeholder': 'Ingrese titulo de libro'
				}
			),
			'autor_id': forms.SelectMultiple(
				attrs = {
					'class':'form-control'
				}
			),
			'fecha_publicacion': forms.SelectDateWidget(
				attrs = {
					'class': 'form-control'
				}
			)
		}