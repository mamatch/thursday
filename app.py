from flask import Flask
from thursday import create_app, db
from flask_migrate import Migrate
from thursday.models import Tweet

app = create_app("dev")
migrate = Migrate(app, db)


@app.shell_context_processor
def make_shell():
    return dict(db=db, Tweet=Tweet)
