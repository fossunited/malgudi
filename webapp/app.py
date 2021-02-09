from flask import Flask, render_template

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