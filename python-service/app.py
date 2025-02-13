from flask import Flask, jsonify
import psycopg2
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

app = Flask(__name__)

# Get database connection URI from .env
DATABASE_URL = os.getenv("PYTHON_DB_URI")

# Database connection function
def get_db_connection():
    return psycopg2.connect(DATABASE_URL)

# ✅ Endpoint untuk mengambil data dari tabel attendance
@app.route('/api/attendance', methods=['GET'])
def get_attendance():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT id, date, name, time, location FROM attendance;")
    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    attendance_list = [
        {
            "id": row[0],
            "date": row[1].strftime("%Y-%m-%d"),
            "name": row[2],
            "time": row[3].strftime("%H:%M:%S"),
            "location": row[4]
        }
        for row in rows
    ]
    
    return jsonify(attendance_list)

# ✅ Endpoint untuk mengambil data dari view attendance_summary
@app.route('/api/attendance_summary', methods=['GET'])
def get_attendance_summary():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT location, date, total_attendance FROM attendance_summary;")
    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    summary_list = [
        {
            "location": row[0],
            "date": row[1].strftime("%Y-%m-%d"),
            "total_attendance": row[2]
        }
        for row in rows
    ]
    
    return jsonify(summary_list)

# ✅ Endpoint untuk mengambil data dari tabel attendance berdasarkan lokasi
@app.route('/api/attendance/<location>', methods=['GET'])
def get_attendance_by_location(location):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT id, date, name, time, location FROM attendance WHERE location = %s;", (location,))
    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    if rows:
        attendance_list = [
            {
                "id": row[0],
                "date": row[1].strftime("%Y-%m-%d"),
                "name": row[2],
                "time": row[3].strftime("%H:%M:%S"),
                "location": row[4]
            }
            for row in rows
        ]
        return jsonify(attendance_list)
    else:
        return jsonify({'message': 'No attendance records found for the specified location'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)