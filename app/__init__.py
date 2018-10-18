#  Creation of application factory

from flask import Flask
from flask import Blueprint
from flask_restplus import Api

from instance.config import config_environment


def create_app(config_name):
    """
    App creation function
    :param config_name:
    :return: Flask object
    """
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config_environment[config_name])

    # import the namespaces
    from .api.controller.products import api as product_ns

    # create a blueprint instance
    blueprint = Blueprint('api', __name__)

    # Initialize API with the blueprint
    api = Api(blueprint,
              title='Store Manager API',
              version='1.0',
              description='store manager api')

    # add product namespace to the namespaces and define a prefix url
    api.add_namespace(product_ns, path='/api/v1')
    app.register_blueprint(blueprint)

    return app
