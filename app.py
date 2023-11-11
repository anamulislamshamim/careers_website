from flask import Flask, render_template, jsonify

app = Flask(__name__)


JOBS = [
  
  {
    'id': 1,
    'title' : 'Backend Developer',
    'location': 'Remote',
    'salary': '19/h euro'
  },
  
  {
    'id': 2,
    'title' : 'Frontend Developer',
    'location': 'Germany',
    'salary': '15/h euro'
  },
  
  {
    'id': 3,
    'title' : 'Data Scientist',
    'location': 'Germany',
    'salary': '17/h euro'
  },
  
]

@app.route('/')
def hello_world():
  return render_template('home.html', jobs=JOBS, company_name = "Ki:Elements")


@app.route('/api/jobs')
def jobs():
  return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8080, debug=True)
