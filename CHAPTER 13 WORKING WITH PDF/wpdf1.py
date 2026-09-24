import PyPDF2
Pdf1 = open('AAALSEO.pdf', 'rb')
Pdf2 = open('meetingminutes.pdf', 'rb')
reader1 = PyPDF2.PdfReader(Pdf1)
reader2 = PyPDF2.PdfReader(Pdf2)
writer = PyPDF2.PdfWriter()

for page in reader1.pages:
    writer.add_page(page)

for page in reader2.pages:
    writer.add_page(page)

pdfoutputfile = open('combinedminutes.pdf', 'wb')
writer.write(pdfoutputfile)
pdfoutputfile.close()
Pdf1.close()
Pdf2.close()
