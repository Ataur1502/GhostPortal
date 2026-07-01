from hashlib import sha256
from pypdf import PdfReader, PdfWriter

PASSWORD = sha256(b"guest").hexdigest()

reader = PdfReader("Employee_Handbook_embedded.pdf")
writer = PdfWriter()

for page in reader.pages:
    writer.add_page(page)

# Preserve embedded attachments
writer.clone_document_from_reader(reader)

writer.encrypt(PASSWORD)

with open("Employee_Handbook_Final.pdf", "wb") as f:
    writer.write(f)

print("Encrypted.")
print(PASSWORD)