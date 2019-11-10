from flask import Flask
from flask_rebar import errors, Rebar
from marshmallow import fields, Schema


rebar = Rebar()

# All handler URL rules will be prefixed by '/v1'
registry = rebar.create_handler_registry(prefix='/v1')

class HelloWorldRequestSchema(Schema):
    name = fields.String()

# This schema will validate the incoming request's query string
class HelloWorldResponseSchema(Schema):
    hello = fields.String()


@registry.handles(
    rule='/hello',
    method='POST',
    request_body_schema=HelloWorldRequestSchema(),
    response_body_schema=HelloWorldResponseSchema(),
)
def post_hello_world():
    """
    We're saying hello!
    """
    # The query string has already been validated by `query_string_schema`
    name = rebar.validated_body.get('name')

    ...

    # Errors are converted to appropriate HTTP errors
    # raise errors.Forbidden()

    ...

    # The response will be marshaled by `marshal_schema`
    return {"hello": name}


def create_app(name):
    app = Flask(name)
    rebar.init_app(app)
    return app


if __name__ == '__main__':
    create_app(__name__).run()
