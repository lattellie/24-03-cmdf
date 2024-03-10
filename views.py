from flask import Blueprint, render_template, request, jsonify

views = Blueprint(__name__, "views")

@views.route("/")
def home():
    return render_template("index.html")

@views.route("/plots")
def plots():
    return render_template("plots.html")

@views.route("/test")
def tests():
    return render_template("test.html")

@views.route("/base")
def bases():
    return render_template("base.html")