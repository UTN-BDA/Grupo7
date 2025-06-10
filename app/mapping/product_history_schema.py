from marshmallow import fields, Schema, post_load

class ProductHistorySchema(Schema):
    id = fields.Integer(required=False)
    product_id = fields.Integer(required=False)
    box_id_before = fields.Integer(required=False, allow_none=True)
    box_id_after = fields.Integer(required=False, allow_none=True)
    timestamp = fields.DateTime(required=False)
