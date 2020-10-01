from PyPDF2 import PdfFileWriter, PdfFileReader

pages_to_keep = [ 5 ] # page numbering starts from 0
infile = PdfFileReader('document.pdf', 'rb')
output = PdfFileWriter()

for i in pages_to_keep:
    p = infile.getPage(i)
    output.addPage(p)

with open('newfile1.pdf', 'wb') as f:
    output.write(f)