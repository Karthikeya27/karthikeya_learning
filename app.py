from flask import Flask,render_template,jsonify,request
from database import load_jobs_from_db,add_data_into_db,load_job_from_db
app = Flask(__name__)





@app.route("/")
def homepage():
  job_list= load_jobs_from_db()
  return render_template("home.html", jobs = job_list)

@app.route("/job/<id>")
def job_info(id):
  info = load_job_from_db(id)
  return render_template("job_page.html",job=info)

@app.route("/job/<id>/apply", methods = ["post"])

def apply_to_jobs(id):
  data = request.form
  job = load_job_from_db(id)
  add_data_into_db(id , data)
  return render_template("application_submitted.html", data = data, job = job)
  
  
  
  

if __name__ == "__main__":
  app.run(host="0.0.0.0" , debug = True)
