from marshmallow import Schema, fields


class BoxSchema(Schema):

    id = fields.Integer(required=False)
    user_id = fields.Integer(required=False,allow_none=True)
    name =fields.String(required=False)
    created_at = fields.DateTime(required=False)
