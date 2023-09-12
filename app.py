from flask import Flask,render_template

app = Flask(__name__)

Jobs= [
  {
    "id" : "1",
    "Job_title" : "Full Stack Developer",
    "Job_Location" : "USA",
    "Salary" : "$100000"
  },
  {
    "id" : "2",
    "Job_title" : "Flask Developer",
    "Job_Location" : "USA",
    "Salary" : "1500000$"
  },
  {
    "id" : "3",
    "Job_title" : "Flutter Developer",
    "Job_Location" : "USA",
    "Salary" : "1500000$"
  }
]

@app.route("/")
def homepage():
  return render_template("home.html", jobs = Jobs)

if __name__ == "__main__":
  app.run(host="0.0.0.0" , debug = True)
