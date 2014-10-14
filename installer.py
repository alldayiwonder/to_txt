from subprocess import call
import os
"""
this script will only work on ubuntu
"""
#antiword: 
call(["sudo", "apt-get", "install", "antiword"],shell=True)

#odt2txt: 
call(["sudo", "apt-get", "install", "odt2txt"],shell=True)

#pdfminer: 
call(["sudo", "pip", "install", "pdfminer"],shell=True)

#python-docx: 

call(["git", "clone", "https://github.com/mikemaccana/python-docx"])  
os.chdir("python-docx")
call(["sudo", "python", "setup.py", "install"],shell=True)
os.chdir("../")

#xlrd:

call(["git", "clone", "https://github.com/python-excel/xlrd"])
os.chdir("xlrd")
call(["sudo", "python", "setup.py", "install"],shell=True)
os.chdir("../")
