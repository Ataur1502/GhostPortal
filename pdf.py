from reportlab.pdfgen import canvas

c = canvas.Canvas("Employee_Handbook.pdf")

c.setFont("Helvetica-Bold", 20)
c.drawString(70, 780, "Employee Incident Report")

c.setFont("Helvetica", 12)

lines = [
    "",
    "An internal backup has been archived.",
    "",
    "Please review the attached archive.",
    "",
    "This document is intended for internal employees only.",
]

y = 740
for line in lines:
    c.drawString(70, y, line)
    y -= 25

c.save()

print("PDF Created")


import fitz
from hashlib import sha256

PASSWORD = sha256(b"guest").hexdigest()[:40]

doc = fitz.open("Employee_Handbook.pdf")

with open("Backup.zip", "rb") as f:
    doc.embfile_add(
        "Backup.zip",
        f.read(),
        filename="Backup.zip",
        desc="Internal Backup"
    )

doc.save(
    "Employee_Handbook_Final.pdf",
    encryption=fitz.PDF_ENCRYPT_AES_256,
    owner_pw=PASSWORD,
    user_pw=PASSWORD,
    permissions=fitz.PDF_PERM_ACCESSIBILITY,
)

doc.close()

print("Done")
print(PASSWORD)
