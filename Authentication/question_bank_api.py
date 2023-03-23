from flask import Flask, jsonify, request
import mysql.connector

app = Flask(__name__)

# Database connection information
mydb = mysql.connector.connect(
  host="localhost",
  user="cs595",
  password="hAlp3yGyMmZLog8S",
  database="QuestionBank"
)

# Endpoint to add a new question
@app.route('/questions', methods=['POST'])
def add_question():
    data = request.get_json()
    cursor = mydb.cursor()
    query = "INSERT INTO QuestionBank (companyTextId, question, questionType, details, answerJson, isGlobal, privateOnly, businessGroupTextId, technologyTextId, proficiencyLevel) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    cursor.execute(query, (data['companyTextId'], data['question'], data['questionType'], data['details'], data['answerJson'], data['isGlobal'], data['privateOnly'], data['businessGroupTextId'], data['technologyTextId'], data['proficiencyLevel']))
    mydb.commit()
    return jsonify({'message': 'Question added successfully'})

# Endpoint to search for questions
@app.route('/questions', methods=['GET'])
def search_questions():
    query = request.args.get('q')
    cursor = mydb.cursor()
    if query:
        cursor.execute("SELECT * FROM QuestionBank WHERE question LIKE %s", ('%' + query + '%',))
    else:
        cursor.execute("SELECT * FROM QuestionBank")
    rows = cursor.fetchall()
    questions = []
    for row in rows:
        questions.append({'id': row[0], 'companyTextId': row[1], 'question': row[2], 'questionType': row[3], 'details': row[4], 'answerJson': row[5], 'isGlobal': row[6], 'privateOnly': row[7], 'businessGroupTextId': row[8], 'technologyTextId': row[9], 'proficiencyLevel': row[10], 'created': row[11], 'updated': row[12]})
    return jsonify(questions)

# Endpoint to update a question
@app.route('/questions/<int:question_id>', methods=['PUT'])
def update_question(question_id):
    data = request.get_json()
    cursor = mydb.cursor()
    query = "UPDATE QuestionBank SET companyTextId = %s, question = %s, questionType = %s, details = %s, answerJson = %s, isGlobal = %s, privateOnly = %s, businessGroupTextId = %s, technologyTextId = %s, proficiencyLevel = %s WHERE id = %s"
    cursor.execute(query, (data['companyTextId'], data['question'], data['questionType'], data['details'], data['answerJson'], data['isGlobal'], data['privateOnly'], data['businessGroupTextId'], data['technologyTextId'], data['proficiencyLevel'], question_id))
    mydb.commit()
    return jsonify({'message': 'Question updated successfully'})

# Endpoint to delete a question
@app.route('/questions/<int:question_id>', methods=['DELETE'])
def delete_question(question_id):
    cursor = mydb.cursor()
    query = "DELETE FROM QuestionBank WHERE id = %s"
    cursor.execute(query, (question_id,))
    mydb.commit()
    return jsonify({'message': 'Question deleted successfully'})

if __name__ == '__main__':
    app.run(debug=True)
