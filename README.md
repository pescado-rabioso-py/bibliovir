# #CHANGELOG
## BiblioVir

**17/11/2021**

- Agregados de estilos en plantillas
- Agregados scripts varios
- App Libros terminada (beta)
- Agregado requirements.txt (funcional)

**18/11/2021**

- Corrección de errores multiples de importación en `urls.py` y `views.py` de la app **libros**
- Correción error sobre modelo personalizado `auth`
- Remoción de lógica y modelo de préstamo de libros

**24/11/2021**

- Corrección de modelo `LibroForm`
- Vista de templates completos
- Correción de sintaxis e identación
- Implementación de `django-crispy-form` para maquetación de LoginForm
- Lanzamiento de Release Candidate ***rc241121***


**25/11/2021**

- `FormularioUsuario` migrado a la vista basada en clases `UserCreationForm`
- Los usuarios ya son creados correctamente y pueden acceder al Front-End
- **FormularioUsuario no permite usar mayúsculas al crear usuario ```AttributeError: 'RegistrarUsuario' object has no attribute 'model__name__'```**

###### TODO

- [x] **La implementación del modelo UserManager no está creando correctamente usuarios (URGENTE)**
- [x] Terminar app usuario
- [x] Finalizar templates de apps
- [ ] Relevar datos importantes para el cliente y aplicarlos a la lógica
- [ ] Obtener medios multimedia para el sitio
- [ ] Corregir errores ortográficos
- [ ] Adjuntar documentación sobre modelos, funciones y métodos
- [ ] Depurar modelo de gestión de usuarios, roles y grupos
- [ ] Remover código inflado
- [ ] Evaluar cambiar AwesomeFonts por Boxicons
- [ ] Mover Lógica a Vistas Basadas en Clases
