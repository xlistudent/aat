from flask import Flask, jsonify, request
import mysql.connector

app = Flask(__name__)

# Database connection information
mydb = mysql.connector.connect(
  host="localhost",
  user="cs595",
  password="hAlp3yGyMmZLog8S",
  database="ResumeManagement"
)

# Endpoint to add a new resume project
@app.route('/resume_projects', methods=['POST'])
def add_resume_project():
    data = request.get_json()
    cursor = mydb.cursor()
    query = "INSERT INTO ResumeProject (title, started, ended, responsibilityDetails) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (data['title'], data['started'], data['ended'], data['responsibilityDetails']))
    mydb.commit()
    return jsonify({'message': 'Resume project added successfully'})

# Endpoint to add a new resume project technology
@app.route('/resume_project_technologies', methods=['POST'])
def add_resume_project_technology():
    data = request.get_json()
    cursor = mydb.cursor()
    query = "INSERT INTO ResumeProjectTechnology (resumeProjectId, businessGroupTextId, technologyTextId, proficiencyLevel) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (data['resumeProjectId'], data['businessGroupTextId'], data['technologyTextId'], data['proficiencyLevel']))
    mydb.commit()
    return jsonify({'message': 'Resume project technology added successfully'})

# Endpoint to search for resume projects
@app.route('/resume_projects', methods=['GET'])
def search_resume_projects():
    query = request.args.get('q')
    cursor = mydb.cursor()
    if query:
        cursor.execute("SELECT * FROM ResumeProject WHERE title LIKE %s", ('%' + query + '%',))
    else:
        cursor.execute("SELECT * FROM ResumeProject")
    rows = cursor.fetchall()
    projects = []
    for row in rows:
        projects.append({'id': row[0], 'title': row[1], 'started': row[2], 'ended': row[3], 'responsibilityDetails': row[4]})
    return jsonify(projects)

# Endpoint to search for resume project technologies
@app.route('/resume_project_technologies', methods=['GET'])
def search_resume_project_technologies():
    resume_project_id = request.args.get('resume_project_id')
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM ResumeProjectTechnology WHERE resumeProjectId = %s", (resume_project_id,))
    rows = cursor.fetchall()
    technologies = []
    for row in rows:
        technologies.append({'id': row[0], 'resumeProjectId': row[1], 'businessGroupTextId': row[2], 'technologyTextId': row[3], 'proficiencyLevel': row[4]})
    return jsonify(technologies)

if __name__ == '__main__':
    app.run(debug=True)
