import sqlite3
import csv

def export_to_csv():
    conn = sqlite3.connect("attendance.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM attendance")

    with open("attendance.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Student ID", "Name", "Roll Number", "section","Date & Time"])  # Column headers
        writer.writerows(cursor.fetchall())

    conn.close()
    print("Attendance records exported to attendance.csv")

export_to_csv()
