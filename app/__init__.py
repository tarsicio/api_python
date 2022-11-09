from flask import Flask

from .models import db
from .models.task import Task

from .views import api_v1

app = Flask(__name__)

def create_app(enviroment):
	app.config.from_object(enviroment)
	# este nos permite registrar todas nuestras URL
	app.register_blueprint(api_v1)

	with app.app_context():
		# Iniciamos nuestra conexión a la base de datos
		db.init_app(app)
		# Se crean todas nuestras tablas la primera Vez.
		db.create_all()	
	return app