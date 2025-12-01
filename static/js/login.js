/*------------------------------------------------------------
FUNCION PRINCIPAL: login()
------------------------------------------------------------*/
function login(){

/*--------------------------- BLOQUE 1: Usuario ---------------------------*/

    // Obtiene el elemento del input donde el usuario escribe su nombre
    let ElementoNombreDeUsuario = document.getElementById("NombreDeUsuario")

    // Obtiene el valor escrito en el input (lo que el usuario ingresó)
    let ValorNombreDeUsuario = ElementoNombreDeUsuario.value

    // Obtiene el span donde se mostrarán los errores de nombre de usuario
    let eErrorNombreUsuario = document.getElementById("eErrorNombreUsuario")

/*--------------------------- BLOQUE 2: Password ---------------------------*/

    // Obtiene el elemento del input donde el usuario escribe la contraseña
    let ElementoPassword = document.getElementById("Password")
    
    // Obtiene el valor escrito en el input (la contraseña ingresada)
    let ValorPassword = ElementoPassword.value

    // Obtiene el span donde se mostrarán los errores de la contraseña
    let eErrorPassword = document.getElementById("eErrorPassword")

/*--------------------------- BLOQUE 3: Validaciones ---------------------------*/

    // Llama a la función que valida el nombre de usuario
    // Devuelve 0 si vacío, 1 si admin, 3 si bodeguero
    let validarNombreDeUsuario = verificarNombreDeUsuario(ElementoNombreDeUsuario, ValorNombreDeUsuario, eErrorNombreUsuario)
    
    // Llama a la función que valida la contraseña
    // Devuelve 0 si vacío, 1 si coincide con admin, 3 si coincide con bodeguero
    let validarPassword = verificarPasswordUsuario(ElementoPassword, ValorPassword, eErrorPassword)

/*--------------------------- BLOQUE 4: Condiciones de acceso ---------------------------*/

    // ✅ Caso 1: Usuario admin (nombre=admin y password=123)
    if (validarNombreDeUsuario == 1 && validarPassword == 1) {
        // Limpia los inputs
        ElementoNombreDeUsuario.value = ""
        ElementoPassword.value = ""
        // Restaura colores de los inputs
        ElementoNombreDeUsuario.style.backgroundColor = "white"
        ElementoNombreDeUsuario.style.color = "black"
        ElementoPassword.style.backgroundColor = "white"
        ElementoPassword.style.color = "black"
        // Borra los mensajes de error
        eErrorPassword.innerText = ""
        eErrorNombreUsuario.innerText = ""
        // Guarda en localStorage que la categoría del usuario es "admin"
        localStorage.setItem("categoria", "admin");
        // Redirige al home de administrador
        window.location.href = "adminhome/"
    } 

    // ✅ Caso 2: Usuario bodeguero (nombre=bodeguero y password=12345)
    if (validarNombreDeUsuario == 3 && validarPassword == 3) {
        // Limpia los inputs
        ElementoNombreDeUsuario.value = ""
        ElementoPassword.value = ""
        // Restaura colores de los inputs
        ElementoNombreDeUsuario.style.backgroundColor = "white"
        ElementoNombreDeUsuario.style.color = "black"
        ElementoPassword.style.backgroundColor = "white"
        ElementoPassword.style.color = "black"
        // Borra los mensajes de error
        eErrorPassword.innerText = ""
        eErrorNombreUsuario.innerText = ""
        // Guarda en localStorage que la categoría del usuario es "home"
        localStorage.setItem("categoria", "home");
        // Redirige al home de bodeguero
        window.location.href = "home/"
    }

}

/*------------------------------------------------------------
FUNCION verificarNombreDeUsuario()
Valida si el nombre de usuario ingresado es válido.
------------------------------------------------------------*/
function verificarNombreDeUsuario(elementoNombreUsuario, valorNombreUsuario, eErrorNombreUsuario){
    if (valorNombreUsuario.length == 0){ // Si el usuario no ingresó nada
        return 0
    }
    else if (valorNombreUsuario == "admin"){ // Si ingresó "admin"
        return 1
    }
    else if (valorNombreUsuario == "bodeguero"){ // Si ingresó "bodeguero"
        return 3
    }
}

/*------------------------------------------------------------
FUNCION verificarPasswordUsuario()
Valida si la contraseña ingresada es válida.
------------------------------------------------------------*/
function verificarPasswordUsuario(elementoPassword, valorPassword, eErrorPassword){
    if (valorPassword.length == 0){ // Si la contraseña está vacía
        return 0
    }
    else if (valorPassword == "123"){ // Contraseña de admin
        return 1
    }
    else if (valorPassword == "12345"){ // Contraseña de bodeguero
        return 3
    }
}
