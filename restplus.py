import traceback
from log import log
from flask_restplus import Api

api = Api(version='1.0', title='Task API',
          description='A demonstration of Flask RestPlus')

@api.errorhandler
def default_error_handler(e):
    message = 'An unhandled exception occurred.'
    log.exception(message)
    return {'message': message}, 500
