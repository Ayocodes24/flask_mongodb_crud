from flask import request, jsonify
from flask_restful import Resource
from app import mongo
from models.user import User
from utils.validators import validate_user
from werkzeug.security import check_password_hash
import jwt
import datetime
import os

SECRET_KEY = 'your_secret_key_here'

class RegisterResource(Resource):
    def post(self):
        data = request.json
        is_valid, errors = validate_user(data)
        if not is_valid:
            return {'message': 'Validation errors', 'errors': errors}, 400

        new_user = User(data['name'], data['email'], data['password'])
        user_id = mongo.db.users.insert_one({
            'name': new_user.name,
            'email': new_user.email,
            'password_hash': new_user.password_hash
        }).inserted_id
        return {'id': str(user_id)}, 201

class LoginResource(Resource):
    def post(self):
        data = request.json
        user = mongo.db.users.find_one({'email': data['email']})
        if user and check_password_hash(user['password_hash'], data['password']):
            token = jwt.encode({
                'user_id': str(user['_id']),
                'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24)
            }, SECRET_KEY, algorithm='HS256')
            return jsonify({'token': token})
        return {'message': 'Invalid email or password'}, 401
