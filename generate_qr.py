import pyqrcode
import png
from pyqrcode import QRCode

def generate_qr(student_id, name, roll_number, section):
    data = f"{student_id},{name},{roll_number},{section}"
    qr = pyqrcode.create(data)
    qr.png(f"{student_id}.png", scale=8)
    print(f"QR Code generated for {name} ({student_id}) - Section: {section}")


# List for the QR codes
students = [
    {"id": "1", "name": "Harsh Raj", "roll": "XXX2353", "section": "A"},
    {"id": "2", "name": "Soumya Kumari", "roll": "XXX3456", "section": "A"},
    {"id": "3", "name": "Shivam Raj", "roll": "XXX3456", "section": "A"},
    {"id": "4", "name": "Harsh Kumar", "roll": "XXX325", "section": "B"}, #Section b generating to demonstrate unauthorised attempt
]


for student in students:
    generate_qr(student["id"], student["name"], student["roll"], student["section"])
