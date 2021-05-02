from app import db
from app.models.planet import Planet
from flask import request, Blueprint, make_response, jsonify

planets_bp = Blueprint("planets", __name__)

@planets_bp.route("/planets", methods=["GET", "POST", "PUT", "DELETE"])
def planets():
    if request.method == "GET":
        name_query = request.args.get("name")
        if name_query:
            planets = Planet.query.filter_by(name=name_query)
        else:
            planets = Planet.query.all()
            
        planets_response = []
        for planet in planets:
            planets_response.append({
                "id": planet.id,
                "name": planet.name,
                "description": planet.description
            })
        return jsonify(planets_response)
    elif request.method == "POST":
        request_body = request.get_json()
        new_planet = Planet(
            name=request_body["name"],
            description=request_body["description"]
        )

        db.session.add(new_planet)
        db.session.commit()

        return make_response(f"Planet {new_planet.name} successfully created", 201)

@planets_bp.route("/planets/<planet_id>", methods=["GET", "PUT", "DELETE"])
def planet(planet_id):
    planet = Planet.query.get(planet_id)
    if planet is None:
        return make_response("", 404)
    elif request.method == "GET":
        return {
            "id": planet.id,
            "name": planet.name,
            "description": planet.description
        }
    elif request.method == "PUT":
        form_data = request.get_json()

        planet.name = form_data["name"]
        planet.description = form_data["description"]

        db.session.commit()

        return make_response(f"Planet #{planet.id} successfully updated")

    elif request.method == "DELETE":
        db.session.delete(planet)
        db.session.commit()
        return make_response(f"Book #{planet.id} successfully deleted")