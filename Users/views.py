from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404

# Create your views here.
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Users
import json
from bson import ObjectId


# Crear usuario
@csrf_exempt
def crear_usuario(request):
    if request.method == 'POST':
        try:
            datos = json.loads(request.body)

            # Verificar si el nickName ya existe
            if Users.objects.filter(nickName=datos['nickName']).exists():
                return JsonResponse({'error': 'El nickName ya esta en uso, elige otro.'}, status=400)

            # Crear usuario si el nickName no está ocupado
            usuario = Users.objects.create(
                nombre=datos['nombre'],
                nickName=datos['nickName'],
            )
            return JsonResponse({'mensaje': 'Usuario creado', 'id': str(usuario.id)}, status=201)

        except KeyError as e:
            return JsonResponse({'error': f'Falta el campo {str(e)}'}, status=400)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'JSON mal formado'}, status=400)

    return JsonResponse({'error': 'Método no permitido'}, status=405)

# Obtener todos los usuarios
def listar_usuarios(request):
    usuarios = Users.objects.all().values()

    # Convertir ObjectId a string para que sea serializable en JSON
    usuarios_serializables = []
    for usuario in usuarios:
        usuario["id"] = str(usuario["id"])  # Convertir el id de ObjectId a string
        usuarios_serializables.append(usuario)

    return JsonResponse(usuarios_serializables, safe=False)


# Obtener un usuario por ID
def obtener_usuario(request, usuario_id):
    try:
        usuario = Users.objects.get(id=usuario_id)
        return JsonResponse({'nombre': usuario.nombre, 'nickName': usuario.nickName})
    except Users.DoesNotExist:
        return JsonResponse({'error': 'Usuario no encontrado'}, status=404)

# Actualizar usuario
@csrf_exempt
def actualizar_usuario(request, usuario_id):
    try:
        usuario = Users.objects.get(id=usuario_id)
        if request.method == 'PUT':
            datos = json.loads(request.body)
            usuario.nombre = datos.get('nombre', usuario.nombre)
            usuario.nickName = datos.get('nickName', usuario.nickName)
            usuario.save()
            return JsonResponse({'mensaje': 'Usuario actualizado'})
    except Users.DoesNotExist:
        return JsonResponse({'error': 'Usuario no encontrado'}, status=404)

# Eliminar usuario
@csrf_exempt
def eliminar_usuario(request, usuario_id):
    try:
        usuario = Users.objects.get(id=usuario_id)
        usuario.delete()
        return JsonResponse({'mensaje': 'Usuario eliminado'})
    except Users.DoesNotExist:
        return JsonResponse({'error': 'Usuario no encontrado'}, status=404)
