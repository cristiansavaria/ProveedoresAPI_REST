

$(document).ready(function() {

    var nroTotalImagenes = 6;
    var nroColumnasPorFila = 3;
    var selectorTablaHTML = "#lista-perros"
    var url = "https://api.thedogapi.com/v1/images/search?limit="+nroTotalImagenes

    generar_galeria_imagenes(selectorTablaHTML, nroTotalImagenes, nroColumnasPorFila, url,"Ver Detalle");
});

function getBtnActionURL() {
    return "https://api.thedogapi.com/v1/images/search?limit=1";
}