import MyPDF2

# open first pdf
pdf1 = open('file1.pdf', 'rb')

#open other pdf
pdf2 = open('file2.pdf', 'rb')

#create a reader object
reader1 = PyPDF2.PdfFileReader(pdf1)
reader2 = PyPDF2.PdfFileReader(pdf2)
