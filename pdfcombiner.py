import PyPDF2

pdf1 = open('JadaDixon_rates_of_reaction_lab.pdf', 'rb')
pdf2 = open('JadaDixon_reaction_rate_p_and_d_.pdf', 'rb')
pdf3 = open('JadaDixon_Redox_Lab_Template.pdf', 'rb')
pdf4 = open('JadaDixonchemistry.pdf', 'rb')
pdf5 = open('jadadixonenergeticslab.pdf', 'rb')
pdf6 = open('JadaDixonSBaLab2.pdf', 'rb')
pdf7 = open('Chemistry_P_and_D__Jada_Dixon.pdf', 'rb')


pdf1reader = PyPDF2.PdfFileReader(pdf1)
pdf2reader = PyPDF2.PdfFileReader(pdf2)
pdf3reader = PyPDF2.PdfFileReader(pdf3)
pdf4reader = PyPDF2.PdfFileReader(pdf4)
pdf5reader = PyPDF2.PdfFileReader(pdf5)
pdf6reader = PyPDF2.PdfFileReader(pdf6)
pdf7reader = PyPDF2.PdfFileReader(pdf7)


pdfwrite = PyPDF2.PdfFileWriter()

for i in range(pdf1reader.numPages):
    pageO = pdf1reader.getPage(i)
    pdfWRITE