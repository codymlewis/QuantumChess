from flask import (
    Blueprint, render_template, url_for, redirect, current_app, g, session, request, flash
)
bp = Blueprint("Main", __name__, url_prefix="/")

@bp.route("/")
def index():
    return redirect(url_for("Main.home"))

@bp.route("/home/")
def home():
    return render_template("index.html")
