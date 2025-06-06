from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.index, name='index'),
      path('login/', LoginView.as_view(template_name='biblioteca/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),

    path('accounts/login/', login_view, name='login'),
    path('accounts/logout/', LogoutView.as_view(next_page='login'), name='logout'),

    path('usuarios/', views.lista_usuarios, name='lista_usuarios'),
    path('usuarios/nuevo/', views.nuevo_usuario, name='nuevo_usuario'),

    path('libros/', views.lista_libros, name='lista_libros'),
    path('libros/nuevo/', views.nuevo_libro, name='nuevo_libro'),

    path('prestamos/', views.lista_prestamos, name='lista_prestamos'),
    path('prestamos/nuevo/', views.nuevo_prestamo, name='nuevo_prestamo'),

    path('autores/', views.lista_autores, name='lista_autores'), 
    path('autores/nuevo/', views.nuevo_autor, name='nuevo_autor'),

    path('libros/<int:pk>editar/', views.editar_libro, name='editar_libro'),
    path('libros/<int:pk>/eliminar/', views.eliminar_libro, name='eliminar_libro'),

    path('autores/<int:pk>editar/', views.editar_autor, name='editar_autor'),
    path('autores/<int:pk>/eliminar/', views.eliminar_autor, name='eliminar_autor'),

    path('usuarios/<int:pk>editar/', views.editar_usuario, name='editar_usuario'),
    path('usuarios/<int:pk>/eliminar/', views.eliminar_usuario, name='eliminar_usuario'),

    path('prestamos/<int:pk>editar/', views.editar_prestamo, name='editar_prestamo'),
    path('prestamos/<int:pk>/eliminar/', views.eliminar_prestamo, name='eliminar_prestamo'),
]
