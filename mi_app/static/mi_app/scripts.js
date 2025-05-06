document.addEventListener("DOMContentLoaded", function () {
    const formulario = document.getElementById("id_FormConsultas"); // Capturar formulario
    const resultado = document.getElementById("resultado"); // Capturar contenedor de respuetas
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    formulario.addEventListener("submit", function (event) {
        event.preventDefault(); // Evita recargar la página al enviar el formulario
        const formData = new FormData(formulario); // Capturar datos cargados en el formulario
        fetch("/consultas/", {
            method: "POST",
            body: formData,
            headers: {
                "X-CSRFToken": csrfToken
            }
        })
        .then(response => response.json())
        .then(data => {

            // Limpiar resultados previos
            resultado.innerHTML = "";
            resultado.classList.remove("error", "exito");

            if (data.success) {
                resultado.classList.add("exito"); // Asignar clase 'éxito' para luego aplicar estilo
                resultado.innerText = data.message; // Mostrar mensaje en contenedor de respuestas
            }
            else {
                resultado.classList.add("error"); // Asignar clase 'error' para luego aplicar estilo

                // Si existen errores específicos
                if (data.errors) {
                    for (let campo in data.errors) {
                        // Mostrar alerta error + detalle de errores en contenedor de respuestas
                        resultado.innerHTML += `<p>${data.errors[campo].join(", ")}</p>`;
                    }
                }
                // Sino, mostrar mensaje genérico en contenedor de respuestas
                else {
                    resultado.innerText = data.message || "Ocurrió un error al enviar la consulta.";
                }
            }
        })
        //Mostrar error en consola
        .catch(error => console.error("Error en la solicitud:", error));
    });

//    document.querySelectorAll(".eliminar-btn").forEach(button => {
//        button.addEventListener("click", function () {
//            let consultaId = this.getAttribute("data-id");
//
//            if (confirm("¿Seguro que deseas eliminar esta consulta?")) {
//                fetch(`/eliminarConsulta/${consultaId}/`, { method: "POST", headers: { "X-CSRFToken": "{{ csrf_token }}" } })
//                .then(response => response.json())
//                .then(data => {
//                    if (data.success) {
//                        document.getElementById(`consulta-${consultaId}`).remove();
//                    } else {
//                        alert("Error al eliminar la consulta");
//                    }
//                });
//            }
//        });
//    });


//    document.getElementById("form-modificar").addEventListener("submit", function (event) {
//        event.preventDefault();
//        let formData = new FormData(this);
//
//        fetch("", { method: "POST", body: formData, headers: { "X-CSRFToken": "{{ csrf_token }}" } })
//        .then(response => response.json())
//        .then(data => {
//            let resultado = document.getElementById("resultado");
//            resultado.innerHTML = "";
//            resultado.classList.remove("alert-success", "alert-danger");
//
//            if (data.success) {
//                resultado.classList.add("alert-success");
//                resultado.innerText = data.message;
//            } else {
//                resultado.classList.add("alert-danger");
//                resultado.innerText = "Error al modificar la consulta";
//            }
//        });
//    });

});
