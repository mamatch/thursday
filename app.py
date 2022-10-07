from flask import Flask
from thursday import create_app, db
from flask_migrate import Migrate

app = create_app("dev")
migrate = Migrate(app, db)
