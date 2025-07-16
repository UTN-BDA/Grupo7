from marshmallow import Schema, fields, post_load
from app.models.user import User

class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True)
    password = fields.Str(required=True, load_only=True) 
    email = fields.Email(required=True)
    name = fields.Str(required=True)

    @post_load
    def make_user(self, data, **kwargs):
        return User(**data)

