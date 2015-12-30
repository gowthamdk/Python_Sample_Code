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

def convert_pdf_to_txt(path):
    #print Name_const +"|"+Part_No+"|"+Location+"|"+Yr_revsion+"|"+Ty_revsion+"|"+Main_town+"|"+Ward+"|"+Police_station+"|"+taluka+"|"+District+"|"+Pin_code
    print path.split("\\")[-1]
    myfile=open("Padmanabanagar_Excel/"+path.split("\\")[-1]+".xls","w")
    Main_town=''
    Ward=''
    Police_station=''
    taluka=''
    District=''
    Pin_code=''
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    fp = file(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos=set()
    for page in PDFPage.get_pages(fp, pagenos, maxpages=2, password=password,caching=caching, check_extractable=True):
        interpreter.process_page(page)
    fp.close()
    device.close()
    str1 = retstr.getvalue()
    #print str1
    retstr.close()
    print path+"=============="
    Str_start=str1.index("No. And Name of Polling Station")
    Str_end=str1.index("Address of Polling Station")
    Str_diff = Str_end -  Str_start
    if Str_diff > 200 :
        Polling_addr = str1[Str_start:Str_start+100]
        Polling_addr = (" ").join(Polling_addr.split('\n')).replace("No. And Name of Polling Station ","")
    else:
        Polling_addr =  str1[Str_start:Str_end]
        Polling_addr = (" ").join(Polling_addr.split('\n')).replace("No. And Name of Polling Station ","")#Polling Address
    Str_start = str1.index("Address of Polling Station")
    Str_end = str1.index(" 4.  NUMBER OF ELECTORS")
    Polling_Station = str1[Str_start:Str_end]#Polling Station
    Polling_Station = (" ").join(Polling_Station.split('\n')).replace("Address of Polling Station","").replace("Number of Auxiliary Polling Stations in this Part","")
    # Str_start=str1.index("Year of Revision")
    # Str_end=str1.index("Roll Identification")
    Main= str1.strip()
    Main= Main.split('\n')
    Yr_revsion= Main[7]
    Name_const= Main[0] +  Main[1]
    Part_No = Main[3]
    Location =Main[5]
    Str_start=str1.index("Type of Revision")
    Str_end=str1.index("Basic (Mother) Roll of 2014")
    Qualify_date= str1[Str_start:Str_end].strip()
    Str_start=Str_end+29
    Str_end=str1.index("Date of Publication")
    Ty_revsion= str1[Str_start:Str_end].strip()
    Ty_revsion= Ty_revsion.split('\n')
    Ty_revsion= ("").join(Ty_revsion)
    if(str1.find("Main Metro")!=-1):
        Str_start=str1.index("Police Station ")
        Str_end=str1.index("Taluka")
        Addr= str1[Str_start:Str_end].strip()
        Addr=Addr.split('\n')
        #Addr= ("|").join(Addr)
        #print Addr
        if len(Addr) > 2:
            print "top"
            Main_town= Addr[2]
            Ward=Addr[3].strip()+Addr[4].strip()
            if(str1.find("Type of Polling Station")==-1) :
                if(len(Addr)<6):
                    Str_start=str1.index("Pin Code")
                    Str_end=str1.index("Date of Publication")
                    Addr= str1[Str_start:Str_end].strip()
                    taluka=Addr[1].strip()
                    District=Addr[2].strip()
                    Pin_code=Addr[3].strip()
                else:    
                    Police_station=Addr[5].strip()
                    taluka=Addr[6].strip()
                    District=Addr[7].strip()
                    Pin_code=Addr[8].strip()
            else:
                Police_station=Addr[4]
                Str_start=str1.index("Pin Code")
                Str_end=str1.index("Type of Polling Station")
                Addr= str1[Str_start:Str_end].strip()
                Addr=Addr.split('\n')
                taluka=Addr[1].strip()
                District=Addr[2].strip()
                Pin_code=Addr[3].strip()         
        else:
##            Str_start=str1.index("Roll Identification")
##            Str_end=str1.index("Police Station")
##            if Str_start > Str_end :
##                Str_end=str1.index("Type of Polling Station")
##            Addr= str1[Str_start:Str_end].strip()
##            Addr=Addr.split('\n')
##            #Addr= ("|").join(Addr)
##            Main_town= Addr[3].strip()
##            Ward=Addr[4].strip()
##            Police_station=Addr[5].strip()+Addr[6].strip()
##            taluka=Addr[7].strip()
##            District=Addr[8].strip()
##            Pin_code=Addr[9].strip()
            Str_start=str1.index("Pin Code")
            Str_end=str1.index("3.  POLLING STATION DETAILS")
            if Str_start > Str_end :
                Str_end=str1.index("Type of Polling Station")
            Addr= str1[Str_start:Str_end].strip()
            Addr=Addr.split('\n')
            #Addr= ("|").join(Addr)
            Main_town= Addr[1].strip()
            Ward=Addr[2].strip()
            Police_station=Addr[3].strip()
            taluka=Addr[4].strip()
            District=Addr[5].strip()
            Pin_code=Addr[6].strip()
            print "bottom"

            
    elif(str1.find("Main Town")!=-1):
        Str_start=str1.index("Pin Code")
        Str_end=str1.index("3.  POLLING STATION DETAILS")
        if Str_start > Str_end :
            Str_end=str1.index("Type of Polling Station")
        Addr= str1[Str_start:Str_end].strip()
        Addr=Addr.split('\n')
        #Addr= ("|").join(Addr)
        Main_town= Addr[1].strip()
        Ward=Addr[2].strip()
        Police_station=Addr[3].strip()
        taluka=Addr[4].strip()
        District=Addr[5].strip()
        Pin_code=Addr[6].strip()
        print "bottom"

    input1 = PdfFileReader(file(path, "rb"))
    total= input1.getNumPages()
    for i in range(1,total):
        page4 = input1.getPage(i)
        contents = page4.extractText()
        #print contents
        if contents.find("Section No")!=-1:
            Str_end = contents.index("Section No")
            Str_start= contents.index('Name')
            Street_name =  contents[Str_end:Str_start]
            Street_name = (" ").join(Street_name.split('\n'))
        if contents.find("Name:")!=-1:
            text = contents.split('Name:')
            for texts in  text :
                if(texts.find("House No.:")!=-1):
                    Str_start= texts.index("House No.:")
                    Str_end= texts.index("Sex:")
                    Main= texts[Str_start:Str_end]
                    Main= Main.split('\n')
                    House_no= Main[0].strip()
                    Relation_name= Main[1].strip()
                    Name= Main[2].strip()
                    Voter_id= Main[3].strip()
                    #print Voter_id
                    Str_start= texts.index('Sex:')
                    Str_end= texts.index('Age: ')
                    Sex=texts[Str_start:Str_end].strip()
                    Str_start=Str_end
                    Str_end=Str_start+8
                    Age=texts[Str_start:Str_end].strip()
                    Str_start=Str_end
                    Str_end=Str_start+15
                    Relation=texts[Str_start:Str_end].strip()
                    #print House_no+"|"+Street_name
                    final_content= Name_const +"|"+Part_No+"|"+Location+"|"+Yr_revsion+"|"+Ty_revsion+"|"+Polling_addr+"|"+Polling_Station+"|"+Main_town+"|"+Ward+"|"+Police_station+"|"+taluka+"|"+District+"|"+Pin_code+"|"+Name+"|"+Sex+"|"+Age+"|"+Voter_id+"|"+Relation+"|"+Relation_name+"|"+House_no+"|"+Street_name
                    #final_content= Name_const.decode('UTF-8') +"|"+Part_No.decode('UTF-8')+"|"+Location.decode('UTF-8')+"|"+Yr_revsion.decode('UTF-8')+"|"+Ty_revsion.decode('UTF-8')+"|"+Polling_addr.decode('UTF-8')+"|"+Polling_Station.decode('UTF-8')+"|"+Main_town.decode('UTF-8')+"|"+Ward.decode('UTF-8')+"|"+Police_station.decode('UTF-8')+"|"+taluka.decode('UTF-8')+"|"+District.decode('UTF-8')+"|"+Pin_code.decode('UTF-8')+"|"+Name.decode('UTF-8')+"|"+Sex.decode('UTF-8')+"|"+Age.decode('UTF-8')+"|"+Voter_id.decode('UTF-8')+"|"+Relation.decode('UTF-8')+"|"+Relation_name.decode('UTF-8')+"|"+House_no.decode('UTF-8')+"|"+Street_name.decode('UTF-8')
                    print final_content
                    myfile.write(final_content.encode('UTF-8') + "\n")
    myfile.close()

path="B.B.M.P(SOUTH)\Padmanabanagar/*.pdf"
files = glob.glob(path)
for filename in files:
    convert_pdf_to_txt(filename)
    #sys.exit(0)
