from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

# Create database
def init_db():
    conn = sqlite3.connect("complaints.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS complaints (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    issue_type TEXT,
    location TEXT,
    description TEXT,
    contact TEXT,
    status TEXT DEFAULT 'Pending'
    )
    """)

    conn.commit()
    conn.close()

init_db()


@app.route('/submit_complaint', methods=['POST'])
def submit_complaint():

    data = request.json

    issue = data.get("issueType")
    location = data.get("location")
    description = data.get("description")
    contact = data.get("contact")

    conn = sqlite3.connect("complaints.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO complaints (issue_type, location, description, contact)
    VALUES (?, ?, ?, ?)
    """, (issue, location, description, contact))

    conn.commit()
    conn.close()

    return jsonify({"message": "Complaint saved successfully"})

@app.route('/get_complaints')
def get_complaints():

    conn = sqlite3.connect('complaints.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM complaints")
    rows = cursor.fetchall()

    conn.close()

    complaints = []

    for row in rows:
        complaints.append({
            "id": row[0],
            "issueType": row[1],
            "location": row[2],
            "description": row[3],
            "contact": row[4],
            "status": row[5]
        })

    return jsonify(complaints)


@app.route('/delete_complaint/<int:id>', methods=['DELETE'])
def delete_complaint(id):

    conn = sqlite3.connect("complaints.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM complaints WHERE id=?", (id,))

    conn.commit()
    conn.close()

    return jsonify({"message": "Complaint deleted"})

@app.route('/resolve_complaint/<int:id>', methods=['PUT'])
def resolve_complaint(id):

    conn = sqlite3.connect("complaints.db")
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE complaints SET status='Resolved' WHERE id=?",
        (id,)
    )

    conn.commit()
    conn.close()

    return jsonify({"message": "Complaint resolved"})

if __name__ == "__main__":
    app.run(debug=True)