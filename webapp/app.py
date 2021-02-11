from flask import Flask, abort, request, render_template, jsonify, url_for
from . import db

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/sketches/new")
def new_sketch():
    sketch = {
        "title": "New Sketch",
        "mode": "python",
        "code": 'print("Hello, world!")'
    }
    return render_template("sketches/edit.html", sketch=sketch)

def save_new_sketch():
    return save_sketch()

@app.route("/sketches/<int:id>")
def sketch(id):
    s = db.get_sketch(id)
    if not s:
        abort(404)
    return render_template("sketches/edit.html", sketch=s)

@app.route("/sketches/<int:id>", methods=["POST"])
@app.route("/sketches/new", methods=["POST"])
def save_sketch(id=None):
    if id is not None:
        s = db.get_sketch(id)
        if not s:
            abort(404)
    if not request.is_json:
        abort(400)
    d = request.json
    if id is None:
        id = db.new_sketch(mode=d['mode'], title=d['title'], code=d['code'])
    else:
        db.save_sketch(id=id, mode=d['mode'], title=d['title'], code=d['code'])

    return jsonify({"ok": True,
        "id": id,
        "path": url_for("sketch", id=id)
    })