from marshmallow import fields, Schema, post_load
from app.models.product import Product

class ProductSchema(Schema):
    id = fields.Integer(required=False)
    name = fields.String(required=True)
    description = fields.String(required=False, allow_none=True)
    box_id = fields.Integer(required=False, allow_none=True)

    @post_load
    def make_product(self, data, **kwargs):
        return Product(**data)