from flask import Flask, render_template

app = Flask(__name__)

class_roster = [("Chris", "A", "Junior"),("John", "B", "Freshman"), ("Jennifer", "A-", "Junior"), ("Tom", "B-", "Sophomore"),
("David", "B", "Senior"), ("Christian", "B", "Freshman", ("Francesca", "C", "Sophomore"))]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/welcome/<string:student_name>")
def welcome(student_name):
    return render_template("welcome.html", student_name=student_name)

@app.route("/roster/<int:grade_view>")
def roster(grade_view):
    return render_template("roster.html", class_roster=class_roster, grade_view=grade_view)
