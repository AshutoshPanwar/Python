import PyPDF2

sampleFile = open('sample.pdf', 'rb')       # Open file
pdfReader = PyPDF2.PdfFileReader(sampleFile)        # Load file data

page = pdfReader.getPage(0)     # Get first page
page.rotateClockwise(90)        # Rotate first page by 90deg.

pdfWriter = PyPDF2.PdfFileWriter()      # Open a file in write mode
pdfWriter.addPage(page)         # Add Roated page to new file
print('Creating new file with name: rotatedPage.pdf')
resultPdFile = open('rotatedPage.pdf', 'wb')        # Creating new file
pdfWriter.write(resultPdFile)       # Write data to new file

# Closing file
resultPdFile.close()
sampleFile.close()
