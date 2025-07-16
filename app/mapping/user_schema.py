from marshmallow import Schema, fields, post_load
from app.models.user import User

class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    email = fields.Email(required=True)
    phone = fields.Str(allow_none=True)

    @post_load
    def make_user(self, data, **kwargs):
        return User(**data)

