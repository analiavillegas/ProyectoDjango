document.addEventListener("DOMContentLoaded", function () {
    const formulario = document.getElementById("id_FormConsultas"); // Capturar formulario
    const resultado = document.getElementById("resultado"); // Capturar contenedor de respuetas
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    if (formulario && resultado) {
        formulario.addEventListener("submit", function (event) {
            event.preventDefault();
            let formData = new FormData(formulario);

            fetch("", {
                method: "POST",
                body: formData,
                headers: {
                    "X-CSRFToken": "{{ csrf_token }}"
                }
            })
            .then(response => response.json())
            .then(data => {
                resultado.innerHTML = "";
                resultado.classList.remove("alert-success", "alert-danger");

                if (data.success) {
                    resultado.classList.add("alert-success");
                    resultado.innerText = data.message;
                }
                else {
                    resultado.classList.add("alert-danger");

                    if (data.errors) {
                        for (let campo in data.errors) {
                            resultado.innerHTML += `<p>${data.errors[campo].join(", ")}</p>`;
                        }
                    } else {
                        resultado.innerText = "Error al modificar la consulta";
                    }
                }
            })
            .catch(error => {
                resultado.classList.add("alert-danger");
                resultado.innerText = "Error de conexión";
                console.error("Error en la solicitud:", error);
            });
        }
    }
});

