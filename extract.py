from PyPDF2 import PdfFileWriter, PdfFileReader

filename_to_open = input('Please input filename to open: ')

if '.pdf' in filename_to_open:
  filename_to_open = filename_to_open.split('.pdf')[0]

name_to_save = input('Input name for file to save as: ')

if '.pdf' in name_to_save:
  name_to_save = name_to_save.split('.pdf')[0]


stringPagesToKeep = input('Provide number of page to extract (separate with comma): ').split(',')
pagesToKeep = []

for pageNumberString in stringPagesToKeep:
  pageNumber = int(pageNumberString.strip()) - 1
  pagesToKeep.append(pageNumber)

infile = PdfFileReader(filename_to_open + '.pdf', 'rb')
output = PdfFileWriter()

for i in pagesToKeep:
  try:
    page = infile.getPage(i)
    output.addPage(page)
  except IndexError:
    print('There isnt provided page in file')
    exit()


with open(name_to_save + '.pdf', 'wb') as file:
  output.write(file)