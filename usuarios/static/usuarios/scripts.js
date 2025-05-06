// Función para obtener el token CSRF de la cookie
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// Captura el evento de envío del formulario
document.getElementById('formSaludo').addEventListener('submit', function(event) {
    event.preventDefault();

    const nombre = event.target.nombre.value;
    const csrftoken = getCookie('csrftoken');  // Obtiene el token CSRF

    // Envía los datos usando Fetch API con POST
    fetch('/enviar-nombre/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken  // Se incluye el token CSRF
        },
        body: JSON.stringify({ nombre: nombre })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('resultado').innerText = data.mensaje;
    })
    .catch(error => console.error('Error:', error));
});













function saludar() {
    alert('¡Hola desde un archivo externo!');
}

