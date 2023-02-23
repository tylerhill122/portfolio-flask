from flask import Flask, render_template, request, redirect, url_for
import data
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('localhost', 27017)

db = client.portfolio
Projects = db.projects

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/projects")
def projects():
    projects = data.projects
    return render_template("projects.html", data=data, projects=projects)

@app.route("/project/<val>")
def project(val):
    proj = data.get(val)
    skills = proj['skills']
    return render_template("project.html", proj=proj, skills=skills)

# Input form routing for eventual insertion of projects into MongoDB
@app.route('/form')
def form():
    return render_template('form.html')
 
@app.route('/data', methods = ['POST', 'GET'])
def formData():
    if request.method == 'GET':
        return f"The URL /data is accessed directly. Try going to '/form' to submit form"
    if request.method == 'POST':
        form_data = request.form
        print(form_data.to_dict())
        Projects.insert_one(form_data.to_dict())
        return render_template('data.html',form_data = form_data)

if __name__ == "__main__":
    app.run(debug=True)