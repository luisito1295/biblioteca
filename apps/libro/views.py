from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import View,TemplateView,ListView,UpdateView,CreateView,DeleteView
from django.urls import reverse_lazy
from apps.libro.models import Autor, Libro
from apps.libro.forms import AutorForm,LibroForm
from django.db.models import Q

class Inicio(TemplateView):
    """Clase que renderiza el index del sistema"""
    template_name = 'index.html'

class ListadoAutor(ListView):
    model = Autor
    form_class = AutorForm
    template_name = 'libro/autor/listar_autor.html'

    def get_queryset(self):
        return self.model.objects.filter(estado = True)

    def get_context_data(self, **kwargs):
        contexto = {}
        contexto['autores'] = self.get_queryset()   #agregamos la consulta al contexto
        contexto['form'] = self.form_class
        return contexto

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())

class CrearAutor(CreateView):
    """Contiene la lógica para crear un Autor
    :parámetro model: Modelo a utilizarse
    :type model: Model
    :parámetro form_class: Form de Django referente a model
    :type form_class: DjangoForm
    :parámetro template_name: Template a utilizarse en la clase
    :type template_name: str
    :parámetro success_url: Url de redireccionado al actualizar
    :type success_url: URL"""
    model = Autor
    form_class = AutorForm
    template_name = 'libro/autor/crear_autor.html'
    success_url = reverse_lazy('libro:listar_autor')

class ActualizarAutor(UpdateView):
    """Contiene la lógica para edición de un Autor
    :parámetro model: Modelo a utilizarse
    :type model: Model
    :parámetro form_class: Form de Django referente a model
    :type form_class: DjangoForm
    :parámetro template_name: Template a utilizarse en la clase
    :type template_name: str
    :parámetro success_url: Url de redireccionado al actualizar
    :type success_url: URL
    """
    model = Autor
    form_class = AutorForm
    template_name = 'libro/autor/autor.html'
    success_url = reverse_lazy('libro:listar_autor')

class EliminarAutor(DeleteView):
    model = Autor

    def post(self,request,pk,*args,**kwargs):
        object = Autor.objects.get(id = pk)
        object.estado = False
        object.save()
        return redirect('libro:listar_autor')

class CrearLibro(CreateView):
    model = Libro
    form_class = LibroForm
    template_name = 'libro/libro/crear_libro.html'
    success_url = reverse_lazy('libro:listado_libros')

class ListadoLibros(View):
    model = Libro
    form_class = LibroForm
    template_name = 'libro/libro/listar_libro.html'

    def get_queryset(self):
        return self.model.objects.filter(estado = True)

    def get_context_data(self,**kwargs):
        contexto = {}
        contexto['libros'] = self.get_queryset()
        contexto['form'] = self.form_class
        return contexto

    def get(self,request,*args,**kwargs):
        return render(request,self.template_name,self.get_context_data())


class ActualizarLibro(UpdateView):
    model = Libro
    form_class = LibroForm
    template_name = 'libro/libro/libro.html'
    success_url = reverse_lazy('libro:listado_libros')

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['libros'] = Libro.objects.filter(estado = True)
        return context

class EliminarLibro(DeleteView):
    model = Libro

    def post(self,request,pk,*args,**kwargs):
        object = Libro.objects.get(id = pk)
        object.estado = False
        object.save()
        return redirect('libro:listado_libros')
