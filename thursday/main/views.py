from . import main
from ..models import Tweet
from flask import render_template


@main.route("/", methods=["GET", "POST"])
def index():
    tweets = Tweet.query.all()
    return render_template("index.html", tweets=tweets, nb=len(tweets))
