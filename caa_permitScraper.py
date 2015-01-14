import os
from converter import Converter
c = Converter()

# test file to convert
path_pdf = os.path.realpath("test_files/914640016400117_r1_4.pdf")
text = c.document_to_text("converted_files/914640016400117_r1_4.pdf", path_pdf)
print text
