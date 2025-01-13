import pdfplumber
with pdfplumber.open('小学属性-公式.pdf') as pdf:
    for i in pdf.pages:
        print(i.extract_text())
        print(f'__________{i.page_number}页结束')