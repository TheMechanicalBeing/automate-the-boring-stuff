import os
import sys

import PyPDF2


def encrypt_pdf_file(foldername, filename):
    reader = PyPDF2.PdfReader(open(os.path.join(foldername, filename), 'rb'))

    if reader.is_encrypted:
        print(f"The pdf file named {filename} is already encrypted.")
    else:
        writer = PyPDF2.PdfWriter()
        for page in reader.pages:
            writer.add_page(page)

        writer.encrypt(input("Enter the encryption key\n"))
        result = open(f"{foldername}/{filename.split('.')[0]}_encrypted.pdf", "wb")
        writer.write(result)
        result.close()


def decrypt_pdf_file(foldername, filename):
    reader = PyPDF2.PdfReader(open(os.path.join(foldername, filename), "rb"))

    if reader.is_encrypted:
        if reader.decrypt(input("Enter the decryption key\n")):
            writer = PyPDF2.PdfWriter()

            for page in reader.pages:
                writer.add_page(page)

            result = open(f"{filename.split('.')[0]}_decrypted.pdf", "wb")
            writer.write(result)
            result.close()

        else:
            print(f"The given key is invalid.")
    else:
        print(f"The pdf file named {filename} is already decrypted")


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: python pdfParanoia.py (encrypt|decrypt)")
        exit()

    if sys.argv[1] not in ("encrypt", "decrypt"):
        print("Usage: python pdfParanoia.py (encrypt|decrypt)")
        exit()
    else:
        mode = sys.argv[1]

    for foldername, subfolders, filenames in os.walk(os.getcwd()):
        pdfs = [filename for filename in filenames if filename.endswith("pdf")]

        for pdf in pdfs:
            print(f"Checking for {pdf}...")
            if mode == "encrypt":
                encrypt_pdf_file(foldername, pdf)
            else:
                decrypt_pdf_file(foldername, pdf)
