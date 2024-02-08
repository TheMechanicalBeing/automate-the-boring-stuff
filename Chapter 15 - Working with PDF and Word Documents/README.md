# Chapter 15- working with PDF and Word Documents

## Exercise 1 - Combining Select Pages from Many PDFs

Program that merges all PDF files that are placed in directory but without first (cover) page.

### Requirements
- Find all PDF files in the current directory
- Sort the filenames so the PDFs are added in order
- Write each page, excluding the first page, of each PDF to the output file
- Call `os.listdir()` to find all the files in the working directory and remove and non-PDF files
- Call Python's `sort()` list method to alphabetize the filenames.
Create a `PdfFileWriter` object for the output PDF
- Loop over each PDF file, creating a `PdfFileReader` object for it
- Loop over each page (except the first) in each PDF file
- Add the pages to the output PDF
- Write the output PDF to a file named _allminutes.pdf_

## Exercise 2 - PDF Paranoia

Program that encrypts/decrypts all PDF files that are place in current directory

### Requirements
- Use _sys.argv_ for analyzing user's input
- Use _os.walk()_ to search through all PDF files
- If PDF file found encrypt/decrypt it
- If decryption fails print out message and continue to the next PDF

## Exercise 3 - Custom Invitations as Word Documents

### Requirements

## Exercise 4 - Brute-Force PDF Password Breaker

### Requirements