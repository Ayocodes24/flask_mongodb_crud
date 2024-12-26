from flask import request
from flask_restful import Resource
from flask_pymongo import PyMongo
from flask import jsonify
from models.user import User
from utils.validators import validate_user
from utils.auth_middleware import token_required
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash

def get_mongo():
    from app import mongo
    return mongo
    
class UserListResource(Resource):
    @token_required
    def get(self, current_user):
        mongo=get_mongo();
        users = mongo.db.users.find()
        result = []
        for user in users:
            result.append({
                'id': str(user['_id']),
                'name': user.get('name', ''),
                'email': user('email', ''),
            })
        return jsonify(result)

    @token_required
    def post(self, current_user):
        data = request.json
        is_valid, errors = validate_user(data)
        if not is_valid:
            return {'message': 'Validation errors', 'errors': errors}, 400
        
        new_user = User(data['name'], data['email'], data['password'])
        mongo=get_mongo();
        user_id = mongo.db.users.insert_one({
            'name': new_user.name,
            'email': new_user.email,
            'password_hash': new_user.password_hash
        }).inserted_id
        return {'id': str(user_id)}, 201

class UserResource(Resource):
    @token_required
    def get(self, current_user, user_id):
        mongo=get_mongo();
        user = mongo.db.users.find_one({'_id': ObjectId(user_id)})
        if user:
            return {
                'id': str(user['_id']),
                'name': user['name'],
                'email': user['email']
            }, 200
        return {'message': 'User not found'}, 404

    @token_required
    def put(self, current_user, user_id):
        data = request.json
        is_valid, errors = validate_user(data)
        if not is_valid:
            return {'message': 'Validation errors', 'errors': errors}, 400
        
        mongo=get_mongo();
        mongo.db.users.update_one(
            {'_id': ObjectId(user_id)},
            {'$set': {
                'name': data['name'],
                'email': data['email'],
                'password_hash': generate_password_hash(data['password'])
            }}
        )
        return {'message': 'User updated successfully'}, 200

    @token_required
    def delete(self, current_user, user_id):
        mongo=get_mongo();
        mongo.db.users.delete_one({'_id': ObjectId(user_id)})
        return {'message': 'User deleted successfully'}, 200

