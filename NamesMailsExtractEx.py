#Program for Extracting the  Names and Mail IDs from Given Text  where It present in Files by using Regular Expressions
#NamesMailsExtractEx.py
import re
try:
    with open("C:\\Users\\murme\\PycharmProject\\RegularExpression\\mail.data","r")as fp:
        filedata=fp.read()
        Namelist=re.findall("[A-Z][a-z]+",filedata)
        mailist=re.findall(r"\S@\S+",filedata)
        print("---------------------------------------------------------------------")
        print("\t\tNames\t\t Mail-ID")
        print("---------------------------------------------------------------------------")
        for names,mail in zip(Namelist,mailist):
            print("\t\t{}\t\t{}".format(names,mail))
            print("--------------------------------------------------------------")
except FileNotFoundError:
    print("File Does Not Exist")