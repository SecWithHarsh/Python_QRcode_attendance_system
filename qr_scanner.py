import sqlite3
from datetime import datetime
import winsound
import cv2
from pyzbar.pyzbar import decode

ALLOWED_SECTION = "A"

def init_db():
    conn = sqlite3.connect("attendance.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS attendance (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      student_id TEXT,
                      name TEXT,
                      roll_number TEXT,
                      section TEXT,
                      date_time TEXT)''')
    conn.commit()
    conn.close()

def mark_attendance(student_id, name, roll_number, section):
    conn = sqlite3.connect("attendance.db")
    cursor = conn.cursor()
    date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute("INSERT INTO attendance (student_id, name, roll_number, section, date_time) VALUES (?, ?, ?, ?, ?)",
                   (student_id, name, roll_number, section, date_time))
    conn.commit()
    conn.close()
    print(f"✅ Attendance marked for {name} ({roll_number}) from {section} on {date_time}")

def beep_alert():
    winsound.Beep(2000, 1000) #playe the sound if wrong section scans the QR

def scan_qr():
    cap = cv2.VideoCapture(0)
    print("📷 Scan a QR Code...")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        decoded_objects = decode(frame)
        for obj in decoded_objects:
            student_data = obj.data.decode("utf-8")
            try:
                student_id, name, roll_number, section = student_data.split(",")
                cap.release()
                cv2.destroyAllWindows()
                return student_id, name, roll_number, section
            except ValueError:
                print("❌ Invalid QR Code format.")
                cap.release()
                cv2.destroyAllWindows()
                return None, None, None, None

        cv2.imshow("QR Scanner", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    
    return None, None, None, None

# --- MAIN EXECUTION ---

init_db()

student_id, name, roll_number, section = scan_qr()

if student_id:
    if section == ALLOWED_SECTION:
        mark_attendance(student_id, name, roll_number, section)
    else:
        print(f"🚫 Unauthorized section: {section}. Attendance denied.")
        beep_alert()
