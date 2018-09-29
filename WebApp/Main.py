from . import Functions
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
        sp = request.form["sp"]
        return "success" if Functions.evalQubit(sp) else "fail"
    return render_template("index.html")
