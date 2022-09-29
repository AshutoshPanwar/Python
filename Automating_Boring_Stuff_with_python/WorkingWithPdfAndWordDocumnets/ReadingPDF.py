import PyPDF2

pdfFileObj = open('sample.pdf', 'rb')       # Open PDF
pdfRead = PyPDF2.PdfFileReader(pdfFileObj)      # Load PDF

print('No of pages in Pdf:')
print(pdfRead.numPages)     # No of pages in PDF

pageObj = pdfRead.getPage(0)
print(pageObj.extractText())        # Print PDF file text

pdfFileObj.close()      # Close file