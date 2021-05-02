from flask import jsonify

def test_get_all_planets_with_no_records(client):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []

def test_get_invalid_id_planet(client):
    # Act
    response = client.get("/planets/100")
    #response_body = response.get_json()

    # Assert
    assert response.status_code == 404
    assert response.get_data(as_text=True) == ""


def test_get_one_planet(client, two_saved_planets):
    # Act
    response = client.get("/planets/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "name": "Ocean",
        "description": "watr 4evr"
    }

def test_create_one_planet(client):
    # Act
    planet_data = {"name": "Sea", "description": "the sea"}
    response = client.post('/planets',json=planet_data)
    #response_body = response.get_json()

    # Assert
    
    assert response.status_code == 201
    assert response.get_data(as_text=True) == "Planet Sea successfully created"
