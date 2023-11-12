from sqlalchemy import create_engine, text

# Connect to the database: These following variable must be set in the .env file. 
# For this project I set these variable here because I used local xaamp as my MYSQL server.
database = 'ki_elements_career_website'
username = "root"
password = "shamim"
host = "localhost"
port = "3306"

db_conn_string = f'mysql+pymysql://{username}:{password}@{host}:{port}/{database}'

engine = create_engine(db_conn_string)


def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM jobs"))
    jobs = []
    
    for row in result.all():
      jobs.append(dict(row))

    return jobs



