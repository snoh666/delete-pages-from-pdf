from PyPDF2 import PdfFileWriter, PdfFileReader

filename_to_open = input('Please input filename to open: ')

if '.pdf' in filename_to_open:
  filename_to_open = filename_to_open.split('.pdf')[0]

name_to_save = input('Input name for file to save as: ')


if '.pdf' in name_to_save:
  name_to_save = name_to_save.split('.pdf')[0]

infile = PdfFileReader(filename_to_open + '.pdf', 'rb')

numOfAllPages = infile.getNumPages()

print(infile.getNumPages())

for i in range(0, numOfAllPages):
  output = PdfFileWriter()

  p = infile.getPage(i)
  output.addPage(p)

  with open(name_to_save + '-' + str(i + 1) + '.pdf', 'wb') as f:
    output.write(f)