let consultaIdAEliminar = null;

document.addEventListener('DOMContentLoaded', () => {
    const eliminarBtns = document.querySelectorAll('.eliminar-btn');
    const modal = new bootstrap.Modal(document.getElementById('confirmarEliminarModal'));
    const confirmarBtn = document.getElementById('confirmarEliminarBtn');

    eliminarBtns.forEach(btn => {
      btn.addEventListener('click', () => {
        consultaIdAEliminar = btn.getAttribute('data-id');
        modal.show();
      });
    });

    confirmarBtn.addEventListener('click', () => {
      if (consultaIdAEliminar) {
        fetch(`/eliminarConsulta/${consultaIdAEliminar}/`, {
          method: 'GET',
          headers: {
            'X-Requested-With': 'XMLHttpRequest'
          }
        })
        .then(response => response.json())
        .then(data => {
          if (data.success) {
            const row = document.getElementById(`consulta-${consultaIdAEliminar}`);
            if (row) row.remove();
          }
          modal.hide();
        })
        .catch(error => {
          console.error("Error al eliminar:", error);
          modal.hide();
        });
      }
    });
});

