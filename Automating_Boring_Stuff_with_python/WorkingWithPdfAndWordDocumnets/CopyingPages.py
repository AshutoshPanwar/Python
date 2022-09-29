import PyPDF2

pdf1File = open('sample.pdf', 'rb')     # Open File in Read Binary Mode


pdf1Reader = PyPDF2.PdfFileReader(pdf1File)     # Load file

pdfWrite = PyPDF2.PdfFileWriter()       # Open a file in write mode

for pageNum in range(pdf1Reader.numPages):
    pageObj = pdf1Reader.getPage(pageNum)       # Get text from one file
    pdfWrite.addPage(pageObj)       # Copy text to Write file

print("New file created with name: New_File.pdf")
pdfOutputFile = open('New_File.pdf', 'wb')
pdfWrite.write(pdfOutputFile)       # Write content to new file

# Close File
pdfOutputFile.close()
pdf1File.close()

