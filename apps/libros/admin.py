from django.contrib import admin
from .models import Autor,Libro
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.
class AutorResource(resources.ModelResource):
	class Meta:
		model = Autor

class AutorAdmin(ImportExportModelAdmin,admin.ModelAdmin):
	search_fields = ('nombre','apellidos','nacionalidad')
	list_display = ('nombre','apellidos','nacionalidad','estado')
	resource_class = AutorResource
	actions = ['eliminacion_logica_autores','activacion_logica_autores']

	def eliminacion_logica_autores(self,request,queryset):
		for autor in queryset:
			autor.estado = False
			autor.save()

	def activacion_logica_autores(self,request,queryset):
		for autor in queryset:
			autor.estado = True
			autor.save()

admin.site.register(Autor, AutorAdmin)
admin.site.register(Libro)