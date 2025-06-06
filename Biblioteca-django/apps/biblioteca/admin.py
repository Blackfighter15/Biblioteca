from django.contrib import admin
from .models import Usuario, Libro, Prestamo,Autor

admin.site.register(Usuario)
admin.site.register(Libro)
admin.site.register(Prestamo)
admin.site.register(Autor)