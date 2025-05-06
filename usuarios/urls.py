from django.urls import path
from . import views
from .views import saludo                         # Importar vista de plantilla saludo
from .views import contacto                         # Importar vista de plantilla saludo


urlpatterns = [
    path('', views.pagina_inicio, name='index'),  # Enrutar plantilla inicio.html (Visualización http://127.0.0.1:8000/)
    path('saludo/', saludo),                      # Enrutar plantilla saludo.html (Visualización http://127.0.0.1:8000/saludo)
    path('contacto/', contacto),                    # Enrutar plantilla saludo.html (Visualización http://127.0.0.1:8000/saludo)
    path('enviar-nombre/', views.enviar_nombre, name='enviar_nombre'),
]


# mi_proyecto/
# │-- mi_proyecto/
# │-- static /                  --> Directorio de Recursos Estáticos globales del proyecto
# │   │-- css /
# │       │-- globalStyles.css
# │   │-- js /
# │       │-- globalScripts.css
# │-- templates /               --> Directorio de Plantillas globales del proyecto
# │   │-- base.html
# │   │-- footer.html
# │   │-- header.html
# │-- app1/
# │   │-- migrations /
# │   │-- static /              --> Directorio de Recursos Estáticos específicos de la aplicación App1
# │        │-- app1/
# │            │-- scripts.js
# │            │-- styles.css
# │   │-- templates /           --> Directorio de Plantillas específicas de la aplicación App1
# │       │-- app1 /
# │           │-- index.html
# │           │-- saludos.html
# │           │-- contacto.html


# │-- manage.py
