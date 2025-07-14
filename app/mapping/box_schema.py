from marshmallow import Schema, fields, post_load

from app.models.box import Box


class BoxSchema(Schema):

    id = fields.Integer(required=False)
    user_id = fields.Integer(required=False,allow_none=True)
    name =fields.String(required=False)
    created_at = fields.DateTime(required=False)

    @post_load
    def make_box(self, data, **kwargs):
        return Box(**data)