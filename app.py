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
        'title': 'Working Student Backend Developer',
        'location': 'Remote',
        'salary': '€20/h',
        'technology': 'Python, Django, Flask, PostgreSQL, Redis, MongoDB, PostgreSQL, MySQL'
    },
  
    {
        'id': 2,
        'title': 'Working Student Frontend Developer',
        'location': 'Saarbruken',
        'salary': '€15/h',
        'technology': 'HTML, CSS, Javascript, React, Redux, Node, Express, PostgreSQL, MongoDB'
    },
  
    {
        'id': 3,
        'title': 'Working Student Data Scientist',
        'location': 'Berlin',
        'salary': '€25/h',
        'technology': 'Python, Pandas, Numpy, Matplotlib, Seaborn, scikit-learn'
    },
  
    {
        'id': 4,
        'title': 'Working Student UI/UX',
        'location': 'Wolfsburg',
        'salary': '12/h euro',
        'technology': 'Figma, Photoshop, Illustrator, After Effects, XD'
    },
  
    {
        'id': 5,
        'title': 'Working Student System Administrator',
        'location': 'Munic',
        'salary': '€18/h',
        'technology': 'Linux, Microsoft, SQL, Database Management'
    },
  
    {
        'id': 6,
        'title': 'Working Student Security Analyst',
        'location': 'Frankfurt',
        'salary': '€21/h',
        'technology': 'Application & Network Security, Cryptography, HIPAA, PCI/DSS, ISO 27001, GDPR'
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
