from subprocess import Popen, PIPE,call
# from docx import opendocx, getdocumenttext
import os
#http://stackoverflow.com/questions/5725278/python-help-using-pdfminer-as-a-library
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from cStringIO import StringIO

class Converter:
    def __init__(self):
        pass
        
    def csv_from_excel(self,file_path):
        csv_name = file_path.split("/")[-1].split(".")[0]+".txt"
        wb = xlrd.open_workbook(file_path)
        sh = wb.sheet_by_name('Sheet1')
        your_csv_file = open(csv_name, 'wb')
        wr = csv.writer(your_csv_file, quoting=csv.QUOTE_ALL)

        text = ""
        for rownum in xrange(sh.nrows):
            wr.writerow(sh.row_values(rownum))
            text += rownum
        your_csv_file.close()
        return text

    def txt_from_csv(self,file_path):
        txt = file_path.split(".")[0]+".txt"
        call(["mv",file_path,txt])

    def convert_pdf_to_txt(self,filename,path):
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
        for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
            interpreter.process_page(page)
        fp.close()
        device.close()
        str = retstr.getvalue()
        retstr.close()
        text = filename.split(".")[0]+".txt"
        with open(text,"w") as f: f.write(text)
        return str

    def real_path(self,filename):
        return os.path.realpath(filename)

    def document_to_text(self,filename, file_path):
        if filename[-4:] == ".doc":
            cmd = ['antiword', file_path]
            p = Popen(cmd, stdout=PIPE)
            stdout, stderr = p.communicate()
            with open(filename[:-4]+".txt","w") as f:
                f.write(stdout.decode("ascii","ignore"))
            return stdout.decode('ascii', 'ignore')
        elif filename[-5:] == ".docx":
            document = opendocx(file_path)
            paratextlist = getdocumenttext(document)
            newparatextlist = []
            for paratext in paratextlist:
                newparatextlist.append(paratext.encode("utf-8"))
            text = '\n\n'.join(newparatextlist)
            with open(filename[:-5]+".txt","w") as f:
                f.write(text)
            return '\n\n'.join(newparatextlist)
        elif filename[-4:] == ".odt":
            cmd = ['odt2txt', file_path]
            p = Popen(cmd, stdout=PIPE)
            stdout, stderr = p.communicate()
            with open(filename[:-4]+".txt","w") as f:
                f.write(stdout.decode("ascii","ignore"))
            return stdout.decode('ascii', 'ignore')
        elif filename[-4:] == ".pdf":
            return self.convert_pdf_to_txt(filename,file_path)
        elif filename[-4:] == ".xlsx":
            self.csv_from_excel(file_path)
            csv = file_path.split(".")[0]+".txt"
            print csv
            self.txt_from_csv(csv)

#path_xlsx = os.path.realpath("thing.xlsx")
#print document_to_text("thing.xlsx", path_xlsx)
#path_pdf = os.path.realpath("human_trafficking.pdf")
#print document_to_text("human_trafficking.pdf",path_pdf)
#path_docx = os.path.realpath("thing.docx")
#print document_to_text("thing.docx",path_docx)
#path_odt = os.path.realpath("thing.odt")
#print document_to_text("thing.odt",path_odt)
