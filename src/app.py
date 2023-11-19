from flask import Flask

from flask_cors import CORS

from config import config

# routes
from routes import UserRoutes,PredictRoutes


app = Flask(__name__)


def pageNotFound(error):
    return "<h1>Pagina no encontrada</h1>", 404


if __name__ == '__main__':

    app.config.from_object(config['development'])

    # bluePrints
    app.register_blueprint(UserRoutes.main, url_prefix='/api/v1/users')
    app.register_blueprint(PredictRoutes.main, url_prefix='/api/v1/predict')

    # error handlers
    app.register_error_handler(404, pageNotFound)
    CORS(app)

    app.run()
