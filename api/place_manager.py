from flask import request, jsonify, abort, Blueprint
from model.place import Place
from persistence.DataManager import DataManager


place_manager_blueprint = Blueprint('place_manager', __name__)
data_manager = DataManager()


@place_manager_blueprint.route('/places', methods=['POST'])
def create_place():
    if not request.json:
        abort(400, description="Missing required fields")

    data = request.json
    place = Place(
        name=data.get('name'),
        description=data.get('description'),
        address=data.get('address'),
        city_id=data.get('city_id'),
        latitude=data.get('latitude'),
        longitude=data.get('longitude'),
        host_id=data.get('host_id'),
        number_of_rooms=data.get('number_of_rooms'),
        number_of_bathrooms=data.get('number_of_bathrooms'),
        price_per_night=data.get('price_per_night'),
        max_guests=data.get('max_guests'),
        amenity_ids=data.get('amenity_ids')
    )

    data_manager.save(place)
    return jsonify(place.to_dict()), 201


@place_manager_blueprint.route('/places', methods=['GET'])
def get_places():
    places = [place.to_dict()
              for place in data_manager.storage.get('Place', {}).values()]
    return jsonify(places), 200


@place_manager_blueprint.route('/places/<place_id>', methods=['GET'])
def get_place(place_id):
    place = data_manager.get(place_id, 'Place')
    if not place:
        abort(404, description="Place not found")
    return jsonify(place.to_dict()), 200


@place_manager_blueprint.route('/places/<place_id>', methods=['PUT'])
def update_place(place_id):
    place = data_manager.get(place_id, 'Place')
    if not place:
        abort(404, description="Place not found")

    if not request.json:
        abort(400, description="Missing required fields")

    data = request.json
    place.name = data.get('name', place.name)
    place.description = data.get('description', place.description)
    place.address = data.get('address', place.address)
    if 'city_id' in data:
        place.city_id = data['city_id']
        if not data_manager.get(place.city_id, 'City'):
            abort(400, description="Invalid city_id")
    place.latitude = data.get('latitude', place.latitude)
    place.longitude = data.get('longitude', place.longitude)
    place.host_id = data.get('host_id', place.host_id)
    place.number_of_rooms = data.get('number_of_rooms', place.number_of_rooms)
    place.number_of_bathrooms = data.get(
        'number_of_bathrooms', place.number_of_bathrooms)
    place.price_per_night = data.get('price_per_night', place.price_per_night)
    place.max_guests = data.get('max_guests', place.max_guests)
    place.amenity_ids = data.get('amenity_ids', place.amenity_ids)

    data_manager.update(place)
    return jsonify(place.to_dict()), 200


@place_manager_blueprint.route('/places/<place_id>', methods=['DELETE'])
def delete_place(place_id):
    place = data_manager.get(place_id, 'Place')
    if not place:
        abort(404, description="Place not found")
    data_manager.delete(place_id, 'Place')
    return '', 204
