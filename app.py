from flask import Flask, render_template, jsonify
# from database import load_jobs_from_db 

app = Flask(__name__)

"""
In real world industrial project we will fetch the data from the database using load_jobs_from_db
JOBS = load_jobs_from_db() 
"""
# since in this project I used local mysql server xaamp so I just used some dummy data 
JOBS = [
    {
        'id': 1,
        'title': 'Backend Developer',
        'location': 'Remote',
        'salary': '19/h euro'
    },
    {
        'id': 2,
        'title': 'Frontend Developer',
        'location': 'Germany',
        'salary': '15/h euro'
    },
    {
        'id': 3,
        'title': 'Data Scientist',
        'location': 'Germany',
        'salary': '17/h euro'
    },
]


@app.route('/')
def hello_world():
  return render_template('home.html', jobs=JOBS, company_name="Ki:Elements")


@app.route('/api/jobs')
def jobs():
  return jsonify(JOBS)


# @app.route('/job/<int:job_id>')
# def show_job():
#   # todo load job from db
#   return render_template('job.html', job=JOBS[job_id - 1])

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8080, debug=True)
