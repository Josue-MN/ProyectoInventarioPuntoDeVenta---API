from django.shortcuts import render, redirect
from CrudBodegasApp.models import Bodegas
from . import forms
from django.contrib import messages
from AuditoriaApp.views import RegistrarAuditoriaBodega
from LoginApp.decorators import login_requerido

# Vista para mostrar todas las bodegas registradas
@login_requerido
def bodegasData(request):
    bodegas = Bodegas.objects.all()  # Obtiene todas las bodegas de la base de datos
    data = {'Bodegas': bodegas}      # Crea un diccionario con los datos
    return render(request, 'templateCrudBodega/bodegas-models.html', data)  # Envía los datos al template


# Vista para registrar una nueva bodega
@login_requerido
def bodegasRegistracionView(request):
    form = forms.BodegaRegistracionForm()  # Crea un formulario vacío por defecto

    # Si se envía el formulario (método POST)
    if request.method == 'POST':
        form = forms.BodegaRegistracionForm(request.POST)  # Carga los datos enviados
        if form.is_valid():  # Verifica si los datos son válidos según las reglas del formulario
            print("FORM VALIDO")
            # Muestra los datos en consola (solo para depuración)
            print("NOMBRE: ", form.cleaned_data['NombreBodega'])
            print("UBICACION: ", form.cleaned_data['UbicacionBodega'])
            print("ESTADO DE LA BODEGA: ", form.cleaned_data['EstadoBodega'])
            print("OBSERVACIONES: ", form.cleaned_data['ObservacionesBodega'])
            
            nueva_bodega = form.save()  # Guarda la nueva bodega en la base de datos
            RegistrarAuditoriaBodega(request, nueva_bodega, "REGISTRAR") #AUDITORIA REGISTRAR
            messages.success(request, "Producto registrado correctamente")  # Muestra mensaje de éxito

            # ========================================================================
            # METODO DE REDIRECCION MEDIANTE USUARIO LOGGEADO
            # ========================================================================
            UsuarioLogeado = request.session.get('Usuario_Username')
            if UsuarioLogeado == "Admin":
                #Accede a la ruta nombrada de urls_admin.py, nombrada como name='admin-crud-producto'
                return redirect('admin-crud-bodega')
            else:
                return redirect('crud-bodega')
            # ========================================================================
        else:
            messages.error(request, "Corrige los errores en el formulario antes de continuar")  # Mensaje de error

    # Se envía al template el formulario (vacío o con errores)
    data = {'form': form}
    return render(request, 'templateCrudBodega/registro-bodega.html', data)


# Vista para actualizar (editar) una bodega existente
@login_requerido
def actualizarBodega(request, IdBodega):
    bodega = Bodegas.objects.get(IdBodega=IdBodega)  # Busca la bodega por su ID
    form = forms.BodegaRegistracionForm(instance=bodega)  # Carga los datos actuales en el formulario

    if request.method == 'POST':
        form = forms.BodegaRegistracionForm(request.POST, instance=bodega)  # Actualiza con los datos enviados

        if form.is_valid():  # Si los datos son válidos
            actualizar_bodega = form.save()  # Guarda los cambios en la base de datos
            RegistrarAuditoriaBodega(request, actualizar_bodega, "ACTUALIZAR")
            messages.success(request, "Producto actualizado correctamente")

            # ========================================================================
            # METODO DE REDIRECCION MEDIANTE USUARIO LOGGEADO
            # ========================================================================
            UsuarioLogeado = request.session.get('Usuario_Username')
            if UsuarioLogeado == "Admin":
                #Accede a la ruta nombrada de urls_admin.py, nombrada como name='admin-crud-producto'
                return redirect('admin-crud-bodega')
            else:
                return redirect('crud-bodega')
            # ========================================================================
        else:
            messages.error(request, "Corrige los errores en el formulario antes de continuar")

    # Devuelve el formulario (ya sea editado o con errores)
    data = {'form': form}
    return render(request, 'templateCrudBodega/registro-bodega.html', data)


# Vista para mostrar la página de confirmación de eliminación
@login_requerido
def confirmarEliminar(request, IdBodega):
    bodega = Bodegas.objects.get(IdBodega=IdBodega)  # Busca la bodega a eliminar
    data = {'bod': bodega}  # Envía los datos al template
    return render(request, 'templateCrudBodega/confirmar-eliminar.html', data)


# Vista para eliminar una bodega de la base de datos
@login_requerido
def eliminarBodega(request, IdBodega):
    bodega = Bodegas.objects.get(IdBodega=IdBodega)  # Busca la bodega a eliminar
    if request.method == 'POST':  # Solo permite eliminar con método POST (por seguridad)
        RegistrarAuditoriaBodega(request, bodega, "ELIMINAR")
        bodega.delete()  # Elimina la bodega de la base de datos
        messages.success(request, f"La Bodega '{bodega.NombreBodega}' fue eliminada correctamente.")
        
        # ========================================================================
        # METODO DE REDIRECCION MEDIANTE USUARIO LOGGEADO
        # ========================================================================
        UsuarioLogeado = request.session.get('Usuario_Username')
        if UsuarioLogeado == "Admin":
            #Accede a la ruta nombrada de urls_admin.py, nombrada como name='admin-crud-producto'
            return redirect('admin-crud-bodega')
        else:
            return redirect('crud-bodega')
        # ========================================================================
    else:
        messages.error(request, "Método no permitido para eliminar usuarios.")  # Evita eliminación con GET


# Vista para mostrar el detalle de una bodega específica
@login_requerido
def detalleBodega(request, IdBodega):
    bodega = Bodegas.objects.get(IdBodega=IdBodega)  # Busca la bodega por ID
    data = {'bod': bodega}  # Envía los datos al template
    return render(request, 'templateCrudBodega/detalle-bodega.html', data)