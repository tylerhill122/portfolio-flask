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
    skills = proj['skills']
    return render_template("project.html", proj=proj, skills=skills)

if __name__ == "__main__":
    app.run(debug=True)