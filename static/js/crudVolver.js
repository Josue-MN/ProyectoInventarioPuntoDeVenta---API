/*-----------------------------------------------------------*/
/* Función para volver desde cualquier CRUD a la página principal según categoría */
function crudVolver(){
  // Obtiene la categoría del usuario desde localStorage
  const categoria = localStorage.getItem("categoria");

  // Si es administrador, lo redirige al panel de admin
  if(categoria == "admin"){
    window.location.href = "/adminhome";
  }
  // Si es usuario normal, lo redirige al panel de home
  else if(categoria == "home"){
    window.location.href = "/home";
  }
}

/*-----------------------------------------------------------*/
/* FUNCIONES DE PRODUCTO */

/* Función para regresar al CRUD de productos según categoría */
function regresarCrudProducto(){
  const categoria = localStorage.getItem("categoria")
  
  if (categoria == "admin") {
    window.location.href = "/adminhome/crud-productos/"
  }
  else if (categoria == "home") {
    window.location.href = "/home/crud-productos/"
  }
}

/*-----------------------------------------------------------*/
/* FUNCIONES DE CATEGORIAS */

/* Función para regresar al CRUD de CATEGORIA según categoría */
function regresarCrudCategoriaProducto(){
  const categoria = localStorage.getItem("categoria")
  
  if (categoria == "admin") {
    window.location.href = "/adminhome/crud-categoriaProducto/"
  }
  else if (categoria == "home") {
    window.location.href = "/home/crud-categoriaProducto/"
  }
}


/*-----------------------------------------------------------*/
/* FUNCIONES DE BODEGA */

/* Función para regresar al CRUD de BODEGA según categoría */
function regresarCrudBodega(){
  const categoria = localStorage.getItem("categoria")
  
  if (categoria == "admin") {
    window.location.href = "/adminhome/crud-bodegas/"
  }
  else if (categoria == "home") {
    window.location.href = "/home/crud-bodegas/"
  }
}


/* FUNCION GLOBAL PARA VOLVER ATRAS EN UN REGISTRO, ACTUALIZAR*/
function regresarAdminOrHome(path){
  const categoria = localStorage.getItem("categoria")
  
  if (categoria == "admin") {
    window.location.href = "/adminhome/" + path;
  }
  else if (categoria == "home") {
    window.location.href = "/home/" + path;
  }
}