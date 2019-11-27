from flask import redirect, render_template, request, url_for
from app import app, db
from app.builds.models import Build

@app.route("/builds", methods=["GET"])
def builds_index():
	return render_template("builds/list.html", builds = Build.query.all())

@app.route("/builds/new/")
def builds_form():
	return render_template("builds/new.html")

@app.route("/builds/", methods=["POST"])
def builds_create():
	b = Build(request.form.get("name"))

	db.session().add(b)
	db.session().commit()

	return redirect(url_for("builds_index"))
