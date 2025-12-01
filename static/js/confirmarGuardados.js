// Espera a que todo el contenido HTML esté completamente cargado antes de ejecutar el código
document.addEventListener('DOMContentLoaded', function() {

    // Selecciona los distintos botones del formulario en el panel de administración de Django
    // Estos botones son los que se usan al guardar o eliminar un registro

    // Botón principal de "Guardar"
    const BotonDeGuardado = document.querySelector('input[name="_save"]');

    // Botón "Guardar y agregar otro"
    const BotonDeGuardado1 = document.querySelector('input[name="_addanother"]');

    // Botón "Guardar y continuar editando"
    const BotonDeGuardado2 = document.querySelector('input[name="_continue"]');

    // Botón de "Eliminar" dentro de un formulario cuya acción termina con "delete/"
    const BotonDeGuardado3 = document.querySelector('form[action$="delete/"] input[type="submit"]');


    // ===== Confirmación antes de guardar =====
    if (BotonDeGuardado) {
        BotonDeGuardado.addEventListener('click', function(e) {
            // Muestra un mensaje de confirmación antes de guardar los cambios
            if (!confirm('¿Seguro que deseas guardar esta edición?')) {
                e.preventDefault();  // Si el usuario cancela, se detiene el envío del formulario
            }
        });
    }

    // ===== Confirmación antes de guardar y agregar otro registro =====
    if (BotonDeGuardado1) {
        BotonDeGuardado1.addEventListener('click', function(e) {
            // Muestra confirmación personalizada para esta acción
            if (!confirm('¿Seguro que deseas guardar y agregar otra edición?')) {
                e.preventDefault();  // Cancela la acción si el usuario presiona "Cancelar"
            }
        });
    }

    // ===== Confirmación antes de guardar y continuar editando =====
    if (BotonDeGuardado2) {
        BotonDeGuardado2.addEventListener('click', function(e) {
            // Muestra confirmación antes de seguir editando
            if (!confirm('¿Seguro que deseas guardar y seguir editando esta edición?')) {
                e.preventDefault();  // Detiene la acción si se cancela
            }
        });
    }

    // ===== Confirmación antes de eliminar un registro =====
    if (BotonDeGuardado3) {
        BotonDeGuardado3.addEventListener('click', function(e) {
            // Muestra una advertencia antes de eliminar definitivamente
            if (!confirm('¿Seguro que deseas eliminar esta edición?')) {
                e.preventDefault();  // Cancela la eliminación si el usuario elige "Cancelar"
            }
        });
    }
});
