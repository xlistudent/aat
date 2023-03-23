from flask import Flask, jsonify, request
import mysql.connector

app = Flask(__name__)

# Database connection information
mydb = mysql.connector.connect(
  host="localhost",
  user="cs595",
  password="hAlp3yGyMmZLog8S",
  database="QuizManagement"
)

# Endpoint to add a new quiz
@app.route('/quizzes', methods=['POST'])
def add_quiz():
    data = request.get_json()
    cursor = mydb.cursor()
    query = "INSERT INTO Quiz (textId, businessGroupTextId, companyTextId, title, status, type, maxAllowDayToAccess, totalNumberOfQuestion, maxTimeAllowedInMinutes, technologyIdCsv, linkedQuizTextIdCsvByOrder, additionalQuestion1, additionalQuestion2, additionalQuestion3, additionalQuestion4, additionalQuestion5, additionalDataJson, published) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    cursor.execute(query, (data['textId'], data['businessGroupTextId'], data['companyTextId'], data['title'], data['status'], data['type'], data['maxAllowDayToAccess'], data['totalNumberOfQuestion'], data['maxTimeAllowedInMinutes'], data['technologyIdCsv'], data['linkedQuizTextIdCsvByOrder'], data['additionalQuestion1'], data['additionalQuestion2'], data['additionalQuestion3'], data['additionalQuestion4'], data['additionalQuestion5'], data['additionalDataJson'], data['published']))
    mydb.commit()
    return jsonify({'message': 'Quiz added successfully'})

# Endpoint to search for quizzes
@app.route('/quizzes', methods=['GET'])
def search_quizzes():
    query = request.args.get('q')
    cursor = mydb.cursor()
    if query:
        cursor.execute("SELECT * FROM Quiz WHERE title LIKE %s", ('%' + query + '%',))
    else:
        cursor.execute("SELECT * FROM Quiz")
    rows = cursor.fetchall()
    quizzes = []
    for row in rows:
        quizzes.append({'id': row[0], 'textId': row[1], 'businessGroupTextId': row[2], 'companyTextId': row[3], 'title': row[4], 'status': row[5], 'type': row[6], 'maxAllowDayToAccess': row[7], 'totalNumberOfQuestion': row[8], 'maxTimeAllowedInMinutes': row[9], 'technologyIdCsv': row[10], 'linkedQuizTextIdCsvByOrder': row[11], 'additionalQuestion1': row[12], 'additionalQuestion2': row[13], 'additionalQuestion3': row[14], 'additionalQuestion4': row[15], 'additionalQuestion5': row[16], 'additionalDataJson': row[17], 'published': row[18], 'created': row[19], 'updated': row[20]})
    return jsonify(quizzes)

# Endpoint to update a quiz
@app.route('/quizzes/<int:quiz_id>', methods=['PUT'])
def update_quiz(quiz_id):
    data = request.get_json()
    cursor = mydb.cursor()
    query = "UPDATE Quiz SET textId = %s, businessGroupTextId = %s, companyTextId = %s, title = %s, status = %s, type = %s, maxAllowDayToAccess = %s, totalNumberOfQuestion = %s, maxTimeAllowedInMinutes = %s, technologyIdCsv = %s, linkedQuizTextIdCsvByOrder = %s, additionalQuestion1 = %s, additionalQuestion2 = %s, additionalQuestion3 = %s, additionalQuestion4 = %s, additionalQuestion5 = %s, additionalDataJson = %s, published = %s WHERE id = %s"
    cursor.execute(query, (data['textId'], data['businessGroupTextId'], data['companyTextId'], data['title'], data['status'], data['type'], data['maxAllowDayToAccess'], data['totalNumberOfQuestion'], data['maxTimeAllowedInMinutes'], data['technologyIdCsv'], data['linkedQuizTextIdCsvByOrder'], data['additionalQuestion1'], data['additionalQuestion2'], data['additionalQuestion3'], data['additionalQuestion4'], data['additionalQuestion5'], data['additionalDataJson'], data['published'], quiz_id))
    mydb.commit()
    return jsonify({'message': 'Quiz updated successfully'})


if __name__ == '__main__':
    app.run(debug=True)
    
