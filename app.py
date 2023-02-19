from flask import Flask, render_template
import data

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")

@app.route("/project/<val>")
def project(val):
    proj = data.get(val)
    return render_template("project.html", proj=proj)

if __name__ == "__main__":
    app.run(debug=True)