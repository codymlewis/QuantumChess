from . import Board
from bleach import clean
from flask import (
    Blueprint, render_template, url_for, redirect, current_app, g, session, request, flash
)
bp = Blueprint("Main", __name__, url_prefix="/")

@bp.route("/")
def index():
    return redirect(url_for("Main.home"))

@bp.route("/home", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        sp = True if request.form["sp"] == "checked" else False
        colour = clean(request.form["colour"])
        start = clean(request.form["start"])
        end = clean(request.form["end"])
        Board.play(start, end, colour, sp)
    return render_template("index.html")
