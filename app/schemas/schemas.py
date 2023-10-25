from app import ma
from marshmallow import fields


class ShowUsersBasicSchema(ma.Schema):
    username = fields.String()


class UserSchema(ShowUsersBasicSchema):
    id = fields.Integer(dump_only=True)
    password_hash = fields.String()
    is_admin = fields.Boolean()

class CategorySchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String()