from flask import Flask
from flask_pymongo import PyMongo
from flask_restful import Api
from flask_swagger_ui import get_swaggerui_blueprint
from config import Config




app = Flask(__name__)
app.config.from_object(Config)

mongo = PyMongo(app) 
api = Api(app)

# Swagger UI setup
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(SWAGGER_URL, API_URL, config={'app_name': "Flask MongoDB CRUD"})
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

# Import and add the resources
from resources.user import UserListResource, UserResource
from resources.auth import RegisterResource, LoginResource

api.add_resource(UserListResource, '/users')
api.add_resource(UserResource, '/users/<string:user_id>')
api.add_resource(RegisterResource, '/register')
api.add_resource(LoginResource, '/login') 

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
