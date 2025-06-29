# 🎓 QR Code-Based Attendance System

A simple and effective Python-based QR Code Attendance System designed for educational institutions and training environments. This project enables quick and accurate attendance tracking using QR codes and SQLite, with easy export to CSV for reporting.

---

## 🚀 Features

- 🔧 **QR Code Generator**  
  Generate unique QR codes for students using their Name, Registration ID, and Section.

- 📷 **Attendance Scanner**  
  Scan QR codes in real-time using a webcam and store attendance records in a **SQLite3 database**.

- 📄 **Export to CSV**  
  Easily export all attendance data to a `.csv` file for further processing or reporting.

---

## 🗂️ Project Structure

```bash
├── qr_generator.py       # Generates QR codes for each student
├── qr_scanner.py         # Scans QR code and stores data in SQLite3
├── export_csv.py         # Exports attendance database to CSV
├── /qrcodes/             # Folder to store generated QR images
├── attendance.db         # SQLite3 database file
└── output.csv            # Exported attendance data (generated)


🧰 Technologies Used
Python 3.x

OpenCV (cv2)

qrcode library

sqlite3

csv
