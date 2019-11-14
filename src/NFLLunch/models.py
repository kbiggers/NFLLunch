from marshmallow import fields, Schema


class HelloWorldRequestSchema(Schema):
    name = fields.String()

# This schema will validate the incoming request's query string
class HelloWorldResponseSchema(Schema):
    hello = fields.String()
