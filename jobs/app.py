from flask import flask, render_template
app = flask(_name_)
@app.route("/")
@app.route("/jobs")
def jobs():
    jobs = execute_sql('SELECT job.id, job.title, job.description, job.salary, employer.id as employer_id, employer.name as employer_name FROM job JOIN employer ON employer.id = job.employer_id')
    return render_template('index.html', jobs=jobs)
