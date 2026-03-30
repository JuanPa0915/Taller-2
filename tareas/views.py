from django.shortcuts import render, redirect, get_object_or_404
from .models import Tarea
from .forms import TareaForm

# 1. Leer (Listar todas las tareas)
def lista_tareas(request):
    tareas = Tarea.objects.all()
    return render(request, 'tareas/lista.html', {'tareas': tareas})

# 2. Crear (Guardar una nueva)
def crear_tarea(request):
    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_tareas')
    else:
        form = TareaForm()
    return render(request, 'tareas/formulario.html', {'form': form})

# 3. Editar (Actualizar una existente)
def editar_tarea(request, id):
    tarea = get_object_or_404(Tarea, id=id)
    if request.method == 'POST':
        form = TareaForm(request.POST, instance=tarea)
        if form.is_valid():
            form.save()
            return redirect('lista_tareas')
    else:
        form = TareaForm(instance=tarea)
    return render(request, 'tareas/formulario.html', {'form': form})

# 4. Eliminar
def eliminar_tarea(request, id):
    tarea = get_object_or_404(Tarea, id=id)
    tarea.delete()
    return redirect('lista_tareas')
