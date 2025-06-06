from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField(unique=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

class Autor(models.Model):
    nombre=models.CharField(max_length=50)
    def __str__(self):
        return self.nombre

class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.ForeignKey(Autor,on_delete=models.CASCADE)  # En clase se cambiará a ForeignKey
    categoria = models.CharField(max_length=30, blank=True, null=True)
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo

class Prestamo(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    fecha_prestamo = models.DateField(auto_now_add=True)
    fecha_devolucion = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.usuario} prestó {self.libro}"
