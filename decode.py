from pypdf import PdfReader, PdfWriter

INPUT_PDF = "Employee_Handbook_Final.pdf"
OUTPUT_PDF = "Employee_Handbook_decrypted.pdf"

# Replace with the correct password
PASSWORD = "84983c60f7daadc1cb8698621f802c0d9f9a3c3c"  # Full SHA256 hash of "guest"

reader = PdfReader(INPUT_PDF)

if reader.is_encrypted:
    if reader.decrypt(PASSWORD) == 0:
        print("[-] Incorrect password!")
        exit()

writer = PdfWriter()

for page in reader.pages:
    writer.add_page(page)

with open(OUTPUT_PDF, "wb") as f:
    writer.write(f)

print(f"[+] Decrypted PDF saved as {OUTPUT_PDF}")