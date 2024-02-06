import os

import PyPDF2


if __name__ == "__main__":
    pdfFiles = list(filter(lambda f: f.endswith(".pdf"), os.listdir()))

    pdfFiles.sort(key=str.lower)

    pdfWriter = PyPDF2.PdfFileWriter()

    for filename in pdfFiles:
        pdfFileObj = open(filename, "rb")
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

        for pageNum in range(1, pdfReader.numPages):
            pageObj = pdfReader.getPage(pageNum)
            pdfWriter.addPage(pageObj)

        pdfOutput = open("allminutes.pdf", "wb")
        pdfWriter.write(pdfOutput)
        pdfOutput.close()
