import csv, json, zipfile
import requests, PyPDF2, fitz

# pip3 install PyMuPDF


# Get ZIP file
zip_file_url = 'https://disclosures-clerk.house.gov/public_disc/financial-pdfs/2021FD.ZIP'
pdf_file_url = 'https://disclosures-clerk.house.gov/public_disc/ptr-pdfs/2021/'

r = requests.get(zip_file_url)
zipfile_name = '2021.zip'

with open(zipfile_name, 'wb') as f:
    f.write(r.content)

# Extract ZIP File
# https://docs.python.org/3/library/zipfile.html#zipfile-objects

with zipfile.ZipFile(zipfile_name) as z:
    z.extractall('.')

# Open File.txt
with open('2021FD.txt') as f:
    for line in csv.reader(f, delimiter='\t'):
        if line[1] == 'Pelosi':
            print(line)
            date = line[7]
            doc_id = line[8]

            r = requests.get(f"{pdf_file_url}{doc_id}.pdf")

            with open(f"{doc_id}.pdf", 'wb') as pdf_file:
                pdf_file.write(r.content)

# Open File.txt
with open('2021FD.txt') as f:
    for line in csv.reader(f, delimiter='\t'):
        if line[1] == 'Peters':
            print(line)
            date = line[7]
            doc_id = line[8]

            r = requests.get(f"{pdf_file_url}{doc_id}.pdf")

            with open(f"{doc_id}.pdf", 'wb') as pdf_file:
                pdf_file.write(r.content)

# https://pymupdf.readthedocs.io/en/latest/tutorial.html

# doc = fitz.open("20018539.pdf")

# page = doc.load_page(page_id=0)

# json_data = page.get_text('json')

# json_data = json.loads(json_data)

# print(json_data.keys())

# for block in json_data['blocks']:
#     if 'lines' in block:
#         print(block)