from flask import Flask,render_template
from database import load_jobs_from_db
app = Flask(__name__)


@app.route("/")
def homepage():
  job_list= load_jobs_from_db()
  return render_template("home.html", jobs = job_list)

if __name__ == "__main__":
  app.run(host="0.0.0.0" , debug = True)
