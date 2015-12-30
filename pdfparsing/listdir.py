import os
pdf = os.listdir("pdfs")
print pdf
files = [x for x in os.listdir('pdfs') if x.endswith('.pdf')]
