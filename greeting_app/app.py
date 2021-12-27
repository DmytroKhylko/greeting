from flask import Blueprint, render_template, request

bp = Blueprint("index", __name__, url_prefix="/")

names = []

@bp.route("/", methods=("GET", "POST"))
def home():
    if request.method == "POST":
        names.append(request.form['name'])
        return render_template("greet.html", name=request.form['name'])

    return render_template("home.html", names=names)


@bp.route("/all-greetings", methods=("GET",))
def all_greetings():
    return render_template("all_greetings.html", names=names)