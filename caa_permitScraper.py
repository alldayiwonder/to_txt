import os
import re  # provides text matching patterns described with a formal syntax
from converter import Converter
c = Converter()

# test file to convert
path_pdf = os.path.realpath("test_files/914640016400117_r1_4.pdf")
text = c.document_to_text("converted_files/914640016400117_r1_4.pdf", path_pdf)
#print text

# http://stackoverflow.com/questions/4666973/how-to-extract-a-substring-from-inside-a-string-in-python

# scrape PTE values
pte = re.findall(r"(?<=PTE:).*?(?=pounds)", text)

for value in pte:
    print 'PTE: ', str.strip(value), ' ', 'lbs'

# scrape emission units, descriptions
eu = re.findall(r"(?<=Emission Unit: ).*?(?= )", text)

for value in eu:
    print 'Emission Unit: ', str.strip(value)

# scrape Upper Permit Limits
limits = re.findall(r"(?<=Upper Permit Limit: ).*?(?= )", text)

for value in limits:
    print 'Upper Permit Limit: ', str.strip(value)

# scrape FEDERALLY ENFORCEABLE CONDITIONS
