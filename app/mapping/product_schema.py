from marshmallow import fields, Schema, post_load

class ProductSchema(Schema):
    id = fields.Integer(required=False)
    name = fields.String(required=True)
    description = fields.String(required=False, allow_none=True)
    box_id = fields.Integer(required=False, allow_none=True)