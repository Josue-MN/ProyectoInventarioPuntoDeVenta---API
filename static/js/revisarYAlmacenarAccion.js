// Función para registrar una acción cuando se registra un empleado
function registrarEmpleadosAccion() {
    // Obtiene la fecha y hora actual del sistema
    let fechaRegistro = new Date();
    // Convierte la fecha a un formato legible según la configuración local
    let fechaLocalRegistro = fechaRegistro.toLocaleDateString();
    // Convierte la hora a un formato legible según la configuración local
    let horaRegistro = fechaRegistro.toLocaleTimeString();

    // Crea un objeto que representa la acción realizada
    let accion = {
        tipo: "Registrar Empleado", // Tipo de acción
        fecha: fechaLocalRegistro,  // Fecha en formato local
        hora: horaRegistro          // Hora en formato local
    }

    // Verifica si en localStorage no existe el array "Acciones"
    if (!localStorage.getItem("Acciones")) {
        // Si no existe, lo inicializa como un array vacío
        localStorage.setItem("Acciones", JSON.stringify([]));
    }

    // Recupera el array de acciones almacenadas en localStorage
    let acciones = JSON.parse(localStorage.getItem("Acciones"))

    // Agrega la nueva acción al array
    acciones.push(accion);

    // Guarda nuevamente el array actualizado en localStorage
    localStorage.setItem("Acciones", JSON.stringify(acciones))
}


//Función para registrar una acción cuando se registra un usuario
function registrarUsuariosAccion() {
    let fechaRegistro = new Date(); // Obtiene fecha y hora actual
    let fechaLocalRegistro = fechaRegistro.toLocaleDateString(); // Fecha en formato local
    let horaRegistro = fechaRegistro.toLocaleTimeString(); // Hora en formato local

    let accion = {
        tipo: "Registrar Usuarios", // Define el tipo de acción
        fecha: fechaLocalRegistro,
        hora: horaRegistro
    }

    if (!localStorage.getItem("Acciones")) { // Si no existe el array "Acciones"
        localStorage.setItem("Acciones", JSON.stringify([])); // Lo crea vacío
    }

    let acciones = JSON.parse(localStorage.getItem("Acciones")) // Recupera el array de acciones
    acciones.push(accion); // Agrega la nueva acción
    localStorage.setItem("Acciones", JSON.stringify(acciones)) // Guarda el array actualizado
}


//Función para registrar una acción cuando se registra un producto
function registrarProductosAccion() {
    let fechaRegistro = new Date(); // Obtiene fecha y hora actual
    let fechaLocalRegistro = fechaRegistro.toLocaleDateString(); // Fecha en formato local
    let horaRegistro = fechaRegistro.toLocaleTimeString(); // Hora en formato local

    let accion = {
        tipo: "Registrar Productos", // Tipo de acción
        fecha: fechaLocalRegistro,
        hora: horaRegistro
    }

    if (!localStorage.getItem("Acciones")) { // Si no existe "Acciones"
        localStorage.setItem("Acciones", JSON.stringify([])); // Lo inicializa
    }

    let acciones = JSON.parse(localStorage.getItem("Acciones")) // Recupera las acciones existentes
    acciones.push(accion); // Inserta la nueva
    localStorage.setItem("Acciones", JSON.stringify(acciones)) // Guarda en localStorage
}


//Función para registrar una acción cuando se registra una categoría
function registrarCategoriaAccion() {
    let fechaRegistro = new Date(); // Fecha y hora actual
    let fechaLocalRegistro = fechaRegistro.toLocaleDateString(); // Fecha en formato local
    let horaRegistro = fechaRegistro.toLocaleTimeString(); // Hora en formato local

    let accion = {
        tipo: "Registrar Categoria", // Tipo de acción registrada
        fecha: fechaLocalRegistro,
        hora: horaRegistro
    }

    if (!localStorage.getItem("Acciones")) { // Si no existe "Acciones"
        localStorage.setItem("Acciones", JSON.stringify([])); // Crea array vacío
    }

    let acciones = JSON.parse(localStorage.getItem("Acciones")) // Obtiene array actual
    acciones.push(accion); // Agrega acción nueva
    localStorage.setItem("Acciones", JSON.stringify(acciones)) // Guarda cambios
}


// Función para registrar una acción cuando se agrega un producto a bodega
function registrarProductoABodegaAccion() {
    let fechaRegistro = new Date(); // Obtiene fecha y hora actual
    let fechaLocalRegistro = fechaRegistro.toLocaleDateString(); // Fecha en formato local
    let horaRegistro = fechaRegistro.toLocaleTimeString(); // Hora en formato local

    let accion = {
        tipo: "Registrar Producto a Bodega", // Tipo de acción específica
        fecha: fechaLocalRegistro,
        hora: horaRegistro
    }

    if (!localStorage.getItem("Acciones")) { // Si "Acciones" no existe en localStorage
        localStorage.setItem("Acciones", JSON.stringify([])); // Lo inicializa vacío
    }

    let acciones = JSON.parse(localStorage.getItem("Acciones")) // Recupera array actual
    acciones.push(accion); // Añade la acción
    localStorage.setItem("Acciones", JSON.stringify(acciones)) // Guarda de nuevo en localStorage
}
