from cerberus import Validator

user_schema = {
    'name': {'type': 'string', 'minlength': 1, 'maxlength': 50, 'required': True},
    'email': {'type': 'string', 'regex': '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$', 'required': True},
    'password': {'type': 'string', 'minlength': 6, 'maxlength': 20, 'required': True},
}

def validate_user(data):
    v = Validator(user_schema)
    return v.validate(data), v.errors
