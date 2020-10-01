from PyPDF2 import PdfFileWriter, PdfFileReader

filename_to_open = input('Please input filename to open with *.pdf extension: ')

name_to_save = input('Input name for file to save as (with *.pdf extension): ')

pages_to_keep = [ 5 ] # page numbering starts from 0
infile = PdfFileReader(filename_to_open, 'rb')
output = PdfFileWriter()

for i in pages_to_keep:
    p = infile.getPage(i)
    output.addPage(p)

with open(name_to_save, 'wb') as f:
    output.write(f)