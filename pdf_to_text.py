# from pypdf import PdfReader
#
# pdf_reader = PdfReader('Mr Joel.pdf')
#
# page_content = {}
#
#
# for index, pdf_page in enumerate(pdf_reader.pages):
#     page_content[index + 1] = pdf_page.extract_text()
#
#
#
# print(page_content)

from pypdf import PdfReader

reader = PdfReader('.pdf')

page = reader .pages[0]
text = page.extract_text()

print(text)