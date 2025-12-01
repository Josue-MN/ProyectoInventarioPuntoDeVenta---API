// Espera a que todo el DOM esté cargado antes de ejecutar el código.
// Esto garantiza que los elementos HTML ya estén disponibles en el documento.
document.addEventListener("DOMContentLoaded", function () {

    // Obtiene el checkbox que permite indicar si se desea cambiar la contraseña.
    // Este elemento tiene el ID "id_CambiarPassword" definido en la plantilla.
    const checkbox = document.getElementById("id_CambiarPassword");

    // Obtiene el contenedor que agrupa los campos de nueva contraseña
    // (Password y ConfirmarPassword). Este contenedor tiene el ID "password-fields".
    const campos = document.getElementById("password-fields");

    // Medida de seguridad: si cualquiera de los dos elementos NO existe,
    // el script finaliza para evitar errores en consola.
    // Esto es útil porque este mismo script se carga también en la vista de registro,
    // donde no existe el checkbox ni el contenedor.
    if (!checkbox || !campos) return;

    // Configura el estado inicial de los campos al cargar la página.
    // Si el checkbox está marcado (p. ej., tras un POST fallido con errores),
    // se muestran los campos de contraseña.
    // Si no está marcado, se ocultan.
    campos.style.display = checkbox.checked ? "block" : "none";

    // Evento que se activa cada vez que el usuario marca o desmarca el checkbox.
    // "this.checked" devuelve true si el checkbox está marcado, false si no lo está.
    // Según ese valor, se muestran u ocultan los campos de contraseña.
    checkbox.addEventListener("change", function () {
        campos.style.display = this.checked ? "block" : "none";
    });
});
