import os

import PyPDF2


if __name__ == "__main__":
    # Selects each file from current directory that has pdf extension
    pdfs = list(filter(lambda f: f.endswith(".pdf"), os.listdir()))

    pdfs.sort()

    writer = PyPDF2.PdfWriter()

    for filename in pdfs:
        pdf_file_object = open(filename, "rb")
        reader = PyPDF2.PdfReader(pdf_file_object)

        # Adds each page (except the first) to writer
        [writer.add_page(page) for page in list(reader.pages[1:])]

        with open("allminutes.pdf", "wb") as pdfOutput:
            writer.write(pdfOutput)
