from django.shortcuts import render, redirect,get_object_or_404
from .models import Usuario, Libro, Prestamo,Autor
from .forms import UsuarioForm, LibroForm, PrestamoForm,AutorForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login

def login_view(request):
    if request.method == 'POST':
        # Mostrar el header Origin para debug
        print("Origin header recibido:", request.META.get('HTTP_ORIGIN'))

        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('index')  # Cambia 'index' por la url que uses después del login
    else:
        form = AuthenticationForm()

    return render(request, 'biblioteca/login.html', {'form': form})


def index(request):
    return render(request, 'biblioteca/index.html')


def lista_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'biblioteca/lista_usuarios.html', {'usuarios': usuarios})

@login_required
def nuevo_usuario(request):
    form = UsuarioForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_usuarios')
    return render(request, 'biblioteca/formulario.html', {'form': form, 'titulo': 'Nuevo Usuario'})


def lista_libros(request):
    libros = Libro.objects.all()
    print(type({'libros': libros}))
    return render(request, 'biblioteca/lista_libros.html', {'libros': libros})


def nuevo_libro(request):
    form = LibroForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_libros')
    return render(request, 'biblioteca/formulario.html', {'form': form, 'titulo': 'Nuevo Libro'})


def lista_prestamos(request):
    prestamos = Prestamo.objects.all()
    return render(request, 'biblioteca/lista_prestamos.html', {'prestamos': prestamos})


def nuevo_prestamo(request):
    form = PrestamoForm(request.POST or None)
    if form.is_valid():
        prestamo = form.save(commit=False)
        libro = prestamo.libro
        if libro.disponible:
            libro.disponible = False  # Cambia estado del libro
            libro.save()
            prestamo.save()
            return redirect('lista_prestamos') 
    return render(request, 'biblioteca/formulario.html', {'form': form, 'titulo': 'Nuevo Préstamo'})


def lista_autores(request):
    autores = Autor.objects.all()  
    return render(request, 'biblioteca/lista_autores.html', {'autores': autores})


def nuevo_autor(request):
    form = AutorForm(request.POST or None)  
    if request.method == 'POST':  
        if form.is_valid(): 
            form.save()  
            return redirect('lista_autores') 
        else:
            print(form.errors)  
    return render(request, 'biblioteca/formulario.html', {'form': form, 'titulo': 'Nuevo Autor'})


def editar_libro(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    form = LibroForm(request.POST or None, instance=libro)
    if form.is_valid():
        form.save()
        return redirect('lista_libros')
    return render(request, 'biblioteca/formulario.html', {'form': form, 'titulo': 'Editar Libro'})


def eliminar_libro(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    if request.method == 'POST':
        libro.delete()
        return redirect('lista_libros')
    return render(request, 'biblioteca/confirmar_eliminar_libro.html', {'objeto': libro})


def editar_autor(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    form = AutorForm(request.POST or None, instance=autor)
    if form.is_valid():
        form.save()
        return redirect('lista_autores')
    return render(request, 'biblioteca/formulario.html', {'form': form, 'titulo': 'Editar Autor'})

@login_required
def eliminar_autor(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    if request.method == 'POST':
        autor.delete()
        return redirect('lista_autores')
    return render(request, 'biblioteca/confirmar_eliminar_autor.html', {'objeto': autor})


def editar_usuario(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    form = UsuarioForm(request.POST or None, instance=usuario)
    if form.is_valid():
        form.save()
        return redirect('lista_usuarios')
    return render(request, 'biblioteca/formulario.html', {'form': form, 'titulo': 'Editar usuario'})


def eliminar_usuario(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    if request.method == 'POST':
        usuario.delete()
        return redirect('lista_usuarios')
    return render(request, 'biblioteca/confirmar_eliminar_usuario.html', {'objeto': usuario})


def editar_prestamo(request, pk):
    prestamo = get_object_or_404(Prestamo, pk=pk)
    form = PrestamoForm(request.POST or None, instance=prestamo)
    if form.is_valid():
        form.save()
        return redirect('lista_prestamos')
    return render(request, 'biblioteca/formulario.html', {'form': form, 'titulo': 'Editar Prestamo'})


def eliminar_prestamo(request, pk):
    prestamo = get_object_or_404(Prestamo, pk=pk)
    if request.method == 'POST':
        prestamo.delete()
        return redirect('lista_prestamos')
    return render(request, 'biblioteca/confirmar_eliminar_prestamo.html', {'objeto': prestamo})