from flask import Flask, request, Blueprint
from flask_restplus import Resource, fields
from task_endpoint import task
from restplus import api
from log import log

app = Flask(__name__)

def initialize_app(app):
    app.config['RESTPLUS_VALIDATE'] = True
    app.config['ERROR_404_HELP'] = False

    blueprint = Blueprint('api', __name__)
    api.init_app(blueprint)
    app.register_blueprint(blueprint)

    api.add_namespace(task)


def main():
    initialize_app(app)
    log.info(
        '>>>>> Starting development server at http://{}/ <<<<<'.format(app.config['SERVER_NAME']))
    app.run(debug=True)


if __name__ == '__main__':
    main()