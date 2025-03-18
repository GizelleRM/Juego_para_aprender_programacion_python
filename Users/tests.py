import pytest
import json
from django.urls import reverse
from Users.models import Users

@pytest.mark.django_db
def test_crear_usuario(client):
    """ Prueba crear un usuario exitosamente """
    url = reverse('crear_usuario')  # Asegúrate de que la ruta esté en urls.py
    data = {
        "nombre": "Juan Pérez",
        "nickName": "Juanito123"
    }
    
    response = client.post(url, data=json.dumps(data), content_type="application/json")
    
    assert response.status_code == 201
    assert Users.objects.count() == 1
    assert Users.objects.first().nickName == "Juanito123"


@pytest.mark.django_db
def test_crear_usuario_nickname_repetido(client):
    """ Prueba que no se pueda crear un usuario con un nickName ya existente """
    Users.objects.create(nombre="Carlos", nickName="Juanito123")  # Usuario ya registrado
    
    url = reverse('crear_usuario')
    data = {
        "nombre": "Pedro Ramírez",
        "nickName": "Juanito123"
    }
    
    response = client.post(url, data=json.dumps(data), content_type="application/json")
    
    assert response.status_code == 400
    assert response.json()["error"] == "El nickName ya esta en uso, elige otro."


@pytest.mark.django_db
def test_listar_usuarios(client):
    """ Prueba obtener la lista de usuarios """
    Users.objects.create(nombre="Juan", nickName="Juanito123")
    Users.objects.create(nombre="Pedro", nickName="Pedro456")
    
    url = reverse('listar_usuarios')
    response = client.get(url)

    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2
    assert data[0]["nickName"] == "Juanito123"
    assert data[1]["nickName"] == "Pedro456"
