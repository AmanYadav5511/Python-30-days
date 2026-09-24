import PyPDF2
Minutesfile = open('meetingminutes.pdf', 'rb')
reader = PyPDF2.PdfReader(Minutesfile)
page = reader.pages[0]
page.rotate(90)

writer = PyPDF2.PdfWriter()
writer.add_page(page)
resultfile = open('rotatePage.pdf','wb')
writer.write(resultfile)
resultfile.close()
Minutesfile.close()