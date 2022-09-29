import PyPDF2

pdfFile = open('sample.pdf', 'rb')      # Read file
pdfReader = PyPDF2.PdfFileReader(pdfFile)       # Load data
pdfWriter = PyPDF2.PdfFileWriter()      # New file

for pageNum in range(pdfReader.numPages):
    pdfWriter.addPage(pdfReader.getPage(pageNum))       # Add data to new file

pdfWriter.encrypt('password')       # Encrypting data of new file
print("Creating new file with name: encryptedSample.pdf, Password: 'password'")
resultPdf = open('encryptedSample.pdf', 'wb')       # Creating new file
pdfWriter.write(resultPdf)      # Copying data to new file

# Close file
resultPdf.close()