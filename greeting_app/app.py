from flask import Blueprint, render_template, request, flash, redirect, url_for
from greeting_app.models.visitor_model import Visitor

bp = Blueprint("index", __name__, url_prefix="/")


@bp.route("/", methods=("GET", "POST"))
def home():
    if request.method == "POST":
        visitor_name = request.form['name'].strip()
        if visitor_name == "":
            flash("Поле не може бути пустим", "is-warning")
            return redirect(url_for("index.home"))

        if Visitor.already_greeted(visitor_name):
            return render_template("greet.html", message="Вже бачились", name=visitor_name)
        Visitor.add_greeted_name(visitor_name)
        return render_template("greet.html", message="Привіт", name=visitor_name)

    return render_template("home.html")


@bp.route("/all-greetings", methods=("GET",))
def all_greetings():
    all_visitors = Visitor.get_all_visitors()
    return render_template("all_greetings.html", visitors=all_visitors)