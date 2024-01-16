from flask import Blueprint, request, jsonify
from app.helpers import token_required
from app.models import db,User,Spacesuit,spacesuit_schema,spacesuits_schema

api = Blueprint('api', __name__, url_prefix='/api')

@api.route('/getdata')
@token_required
def getdata(current_user_data):
    return { 'some': 'value'}

@api.route('/spacesuits', methods=['POST'])
@token_required
def create_spacesuit(current_user_token):
    name = request.json['name']
    make = request.json['make']
    model = request.json['model']
    color = request.json['color']
    year = request.json['year']
    price = request.json['price']
    serial_num = request.json['serial_num']
    planet_used_on = request.json['planet_used_on']
    user_token = current_user_token.token
    
    print(f'BIG TESTER: {current_user_token.token}')
    
    spacesuit = Spacesuit(
        name=name,
        make=make,
        model=model,
        color=color,
        year=year,
        price=price,
        planet_used_on=planet_used_on,
        serial_num=serial_num,
        user_token=user_token
    )
    
    db.session.add(spacesuit)
    db.session.commit()
    
    response = spacesuit_schema.dump(spacesuit)
    return jsonify(response)

@api.route('/spacesuits', methods=['GET'])
@token_required
def get_spacesuits(current_user_token):
    a_user = current_user_token.token
    spacesuits = Spacesuit.query.filter_by(user_token = a_user).all()
    response = spacesuits_schema.dump(spacesuits)
    return jsonify(response)

@api.route('/spacesuits/<id>', methods = ['GET'])
@token_required
def get_vehicle(current_user_token, id):
    owner = current_user_token.token
    spacesuit = Spacesuit.query.get(id)
    response = spacesuits_schema.dump(spacesuit)
    return jsonify(response)

@api.route('/spacesuits/<id>', methods = ['POST', 'PUT'])
@token_required
def update_spacesuit(current_user_token,id):
    spacesuit = Spacesuit.query.get(id)
    
    spacesuit.name = request.json['name']
    spacesuit.make = request.json['make']
    spacesuit.model = request.json['model']
    spacesuit.color = request.json['color']
    spacesuit.year = request.json['year']
    spacesuit.price = request.json['price']
    spacesuit.planet_used_on = request.json['planet_used_on']
    spacesuit.serial_num = request.json['serial_num']
    spacesuit.user_token = current_user_token.token
    
    db.session.commit()
    response = spacesuit_schema.dump(spacesuit)
    return jsonify(response)

@api.route('/spacesuits/<id>', methods=['DELETE'])
@token_required
def delete_spacesuit(current_user_token, id):
    spacesuit = Spacesuit.query.get(id)
    db.session.delete(spacesuit)
    db.session.commit()
    response = spacesuit_schema.dump(spacesuit)
    return jsonify(response)