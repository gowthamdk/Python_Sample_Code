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
path="E:/voters list1/*.pdf"
files = glob.glob(path)
for filename in files:
    print filename

    input1 = PdfFileReader(file(filename, "rb"))
    sys.exit()
    myfile=open("pdf1/"+filename[16:24]+".csv","w")
    myfile.write("Main Town"+"\t"+"Ward Number"+"\t"+"Police Station"+"\t"+"Tehsil"+"\t"+"District"+"\t"+"Pin"+"\t"+"Name&Reservation status of Assemble"+"\t"+"Part no"+"\t"+"location"+"\t"+"yr of Revison"+"\t"+"Qualifying Date"+"\t"+"Roll Identification"+"\t"+"Details Of Part"+"\t"+"Type of Revision"+"\t"+"Date of Revision"+"\t"+"Supplementary"+"\t"+"Name"+"\t"+"Sex"+"\t"+"Age"+"\t"+"Voter's Id"+"\t"+"Relation"+"\t"+"Relation Name"+"\t"+"House No"+"\t"+"FileName"+"\n")
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
    retstr.close()
    Str_start= str1.index("Main Town : ")
    Str_end= str1.index("Ward Number : ")
    Main_town= str1[Str_start+11:Str_end].strip() 
    Main_town=Main_town.split('\n')
    Main_town= ("").join(Main_town)#get Main Town
    Str_start=Str_end+13
    Str_end= str1.index("Police Station : ")
    Ward_no= str1[Str_start:Str_end].strip()
    Ward_no=Ward_no.split('\n')
    Ward_no= ("").join(Ward_no)    #get  Ward no
    Str_start= str1.index("Police Station : ")+19
    Str_end= str1.index("Tehsil:")
    Police_stat= str1[Str_start:Str_end].strip()
    Police_stat=Police_stat.split('\n')
    Police_stat= ("").join(Police_stat)#get Police Station
    Str_start= str1.index("Pin : ")+5
    Str_end= str1.index("Type of Polling")
    Pin1= str1[Str_start:Str_end].strip()
    Pin=Pin1.split('\n')
    chk= Pin1.replace(Pin[0],"").strip()
    chk=chk.split('\n')
    Tehsil= chk[0]
    pname= ("").join(chk)
    pin_code=pname.replace(Tehsil,"")
    #print  Main_town+"|"+Ward_no[0]+"|"+Police_stat+"|"+Pin[0]+"|"+Pin[1]+"|"+Pin[3]+"|"+path
    

    total= input1.getNumPages()
    s=""
    page2 = input1.getPage(0)
    cont = page2.extractText()# print each page contents using pdfminer
    Str_stat=cont.index("No. Name and Reservation Status of Assembly Constituency :")
    End_stat= cont.index("Part No.")
    St_Name = cont[Str_stat:End_stat]
    St_Name=St_Name.replace("No. Name and Reservation Status of Assembly Constituency :","")#get name
    Str_stat= cont.index("Part No.")
    End_stat=cont.index("No. Name and Reservation Status of Parliamentary Constituency (ies) in which the assembly constituency is located :")
    St_Part = cont[Str_stat:End_stat] 
    St_Part = St_Part.replace("Part No. -","")#get part no
    Str_stat=cont.index("No. Name and Reservation Status of Parliamentary Constituency (ies) in which the assembly constituency is located :")
    End_stat= cont.index("1 . DETAILS OF REVISION Year of Revision         :")
    St_Part_area= cont[Str_stat:End_stat]
    St_Part_area=St_Part_area.replace("No. Name and Reservation Status of Parliamentary Constituency (ies) in which the assembly constituency is located :","")#get area
    Str_stat= cont.index("Date of  Publication ")+23
    End_stat=Str_stat+4
    Yr_revison= cont[Str_stat:End_stat] #get year of revison
    Str_stat=End_stat
    Yr_qualification= cont[Str_stat:Str_stat+10]#get Qualifying Date
    Str_stat=Str_stat+10
    End_stat= cont.index("Roll Identification   :")
    revison= cont[Str_stat:End_stat] 
    type_revison=revison[:-10].strip()#get type of revison
    Str_publication =revison.replace(type_revison,"") #get type of Publication
    Str_stat=cont.index("Pin :")
    End_stat= cont.index("DelhiIssued By Electoral Registration Officer1")
    roll_identf= cont[Str_stat+17:End_stat] # get roll identification
    Str_stat=cont.index("Issued By Electoral Registration Officer1")
    End_stat= cont.index("Supplementry-I")
    St_details= cont[Str_stat:End_stat]
    St_details=St_details.replace("Issued By Electoral Registration Officer","")#get details
    Str_stat=cont.index("Supplementry-I")
    St_suppl= cont[Str_stat:] # get supplementary year
    for i in range(1,total): # no of pages 
        page4 = input1.getPage(i)
        contents = page4.extractText() #print each page using pypdf
        text = contents.split('Sex :')
        flag = 1
        for texts in  text :
            text1=texts.split(":")
            if flag ==1 :
                flag=flag+1
                continue
            else:
                 Relation_name=''
                 text2=text1[3]
                 text2=re.sub("\s+","",text2)
                 if text2.find("Father'sName")>=0:
                     ind=text2.index("Father'sName")
                 elif text2.find("Other'sName")>=0:
                     ind=text2.index("Other'sName")
                 elif text2.find("Mother'sName")>=0:
                     ind=text2.index("Mother'sName")
                 elif text2.find("Husband'sName")>=0:
                     ind=text2.index("Husband'sName")
                 else:
                     continue
                 pname=text2[ind:]
                 split2=[b for b in re.split(r'([A-Z][a-z]*\d*)', pname) if b]
                 Relation=split2[0]+split2[1]+split2[2]#Get Relation name
                 flat=pname.replace(Relation, "")
                 split3= re.match(r"([a-z]+)([0-9]+)", flat,re.I)
                 if split3:
                    items = split3.groups()
                    #flat_no = items[1] 
                    Relation_name = items[0] # get Relation Name 
                 text5=[a for a in re.split(r'([A-Z][a-z]*\d*)', text2) if a]
                 voter_id=text5[1]+ text5[2]+text5[3]#Get voter's Id
                 Sex=text1[0].replace("Age", "")
                 if text1[1].find("House No")>=0:
                     Age=text1[1].replace("House No", "")
                 else:    
                     Age=text1[1].replace("Name", "")
                 strt= text2.index(voter_id)
                 end = text2.index(Relation)
                 fname =text2[strt:end]
                 Name= fname.replace(voter_id, "")#Get voter's Name
                 flat_no= flat.replace(Relation_name,"") #Get flat Number
                 print Main_town+"|"+Ward_no[0:3]+"|"+Police_stat+"|"+Pin[0]+"|"+Tehsil+"|"+pin_code+"|"+Name+"|"+Sex+"|"+Age+"|"+voter_id+"|"+Relation+"|"+Relation_name+"|"+flat_no
                 myfile.write(Main_town.strip().encode('UTF-8')+"\t"+Ward_no[0:3].encode('UTF-8')+"\t"+Police_stat.strip().encode('UTF-8')+"\t"+Pin[0].strip().encode('UTF-8')+"\t"+Tehsil.encode('UTF-8')+"\t"+pin_code.encode('UTF-8')+"\t"+St_Name.encode('UTF-8') +"\t"+St_Part.encode('UTF-8') +"\t"+St_Part_area.encode('UTF-8') +"\t"+Yr_revison.encode('UTF-8') +"\t"+Yr_qualification.encode('UTF-8') +"\t"+roll_identf.encode('UTF-8') +"\t"+St_details.encode('UTF-8') +"\t"+type_revison.encode('UTF-8')+"\t"+Str_publication.encode('UTF-8')+"\t"+St_suppl.encode('UTF-8') +"\t"+Name.encode('UTF-8') +"\t"+Sex.encode('UTF-8')+ "\t"+Age.encode('UTF-8') +"\t"+voter_id.encode('UTF-8') +"\t"+Relation.encode('UTF-8') +"\t"+Relation_name.encode('UTF-8') +"\t"+flat_no.encode('UTF-8') +"\t"+filename[9:]+"\n")
    myfile.close()             
             
            
