# 60aria - 2100
# 90aria - 1500

import os, PyPDF2

path = './files'

directory = os.fsencode(path)

total60 = 0
total90 = 0

cost = input("What's the cost? ")

for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.endswith(".pdf") :

        pdf = PyPDF2.PdfFileReader(path+'/'+filename,"rb").getPage(0)

        width = round( float(pdf.mediaBox.getWidth()) * 0.352777778 )
        height = round( float(pdf.mediaBox.getHeight()) * 0.352777778 )

        waste = [594-width, 914-width, 594-height, 914-height]

        minimumWasteIndex = waste.index(min(list(filter(lambda x: x >= 0, waste))))

        if minimumWasteIndex == 0:
            total60 += height
            print(f'{filename}: Classified as 60')
        elif minimumWasteIndex == 1:
            total90 += height
            print(f'{filename}: Classified as 90')
        elif minimumWasteIndex == 2:
            total60 += width
            print(f'{filename}: Classified as 60')
        else:
            total90 += width
            print(f'{filename}: Classified as 90')


cost60 = total60/1000*0.6*float(cost)
print (f'\n60: {cost60} €')

cost90 = total90/1000*0.9*float(cost)
print (f'90: {cost90} €')

print (f'Total: {round(cost60+cost90, 2)} €')

