from django.urls import path
from .views import crear_usuario, listar_usuarios, obtener_usuario, actualizar_usuario, eliminar_usuario

urlpatterns = [
    path('usuarios/', listar_usuarios, name = 'listar_usuarios'),
    path('usuarios/crear/', crear_usuario, name  = 'crear_usuario'),
    path('usuarios/<str:usuario_id>/', obtener_usuario),
    path('usuarios/<str:usuario_id>/actualizar/', actualizar_usuario),
    path('usuarios/<str:usuario_id>/eliminar/', eliminar_usuario),
]

