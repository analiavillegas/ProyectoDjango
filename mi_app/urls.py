from django.urls import path
from . import views
from .views import formulario_view
from .views import consultas, listado_consultas, modificar_consulta, eliminar_consulta
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.pagina_inicio, name='index'),
    path('consultas/', consultas),
    path('listadoConsultas/', listado_consultas, name='listado_consultas'),
    path('modificarConsulta/<int:consulta_id>/', modificar_consulta, name='modificar_consulta'),
    path('eliminarConsulta/<int:consulta_id>/', eliminar_consulta, name='eliminar_consulta'),
    path('registro/', views.registro, name='registro'),
    path('login/', auth_views.LoginView.as_view(template_name='mi_app/login.html'), name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),  # página después del login
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('formulario/', formulario_view, name='formulario'),
]
