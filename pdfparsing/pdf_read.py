from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfpage import PDFTextExtractionNotAllowed
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice
from pdfminer.layout import LAParams
from pdfminer.converter import PDFPageAggregator
from pdfminer.converter import TextConverter
from cStringIO import StringIO
from pyPdf import PdfFileWriter, PdfFileReader
import sys
import re
import glob
path="D:/Python27/Python Code/pdfparsing/pdfs/*.pdf"
files = glob.glob(path)
for filename in files:
    print filename

    input1 = PdfFileReader(file(filename, "rb"))
    myfile=open("pdf1/"+filename[40:47]+".csv","w")
    myfile.write("Main Town")
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    fp = file(filename, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos=set()
    for page in PDFPage.get_pages(fp, pagenos, maxpages=1, password=password,caching=caching, check_extractable=True):
        interpreter.process_page(page)
    fp.close()
    device.close()
    str1 = retstr.getvalue()#print whole pdf contents as string using pdfminer
    #print str1
    retstr.close()
##    Str_start= str1.index("UNITED")
##    Str_end= str1.index("FORM 10-K")
##    Main_town= str1[Str_start+6:Str_end].strip()
##    Main_town=Main_town.split('\n')
##    print Main_town


    total= input1.getNumPages()
    s=""
    page2 = input1.getPage(65)
    cont = page2.extractText()# print each page contents using pdfminer
    #print cont
    Str_stat=cont.index("Revenue:")
    End_stat= cont.index("Cost of revenue:")
    St_Name = cont[Str_stat:End_stat]
    print St_Name
    
    
