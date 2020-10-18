from PyPDF2 import PdfFileWriter, PdfFileReader

filenamesToOpen = input('Please input filenames to open and join (comma separate): ').split(',')

files = []

for filename in filenamesToOpen:
  newFilename = filename
  if '.pdf' in filename:
    newFilename = filename.split('.pdf')[0]
  newFilename = newFilename.strip()
  files.append(newFilename)

name_to_save = input('Input name for file to save as: ')


if '.pdf' in name_to_save:
  name_to_save = name_to_save.split('.pdf')[0]

output = PdfFileWriter()

for filenameToOpen in files:
  infile = PdfFileReader(filenameToOpen + '.pdf', 'rb')
  numOfAllPages = infile.getNumPages()
  for i in range(0, numOfAllPages):
      page = infile.getPage(i)
      output.addPage(page)

with open(name_to_save + '-' + '.pdf', 'wb') as f:
  output.write(f)