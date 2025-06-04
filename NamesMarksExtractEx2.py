#Program for Extracting the  Names and Marks from Given Text  where It present in Files by using Regular Expressions
#NamesMarksExtractEx2.py
import re
try:
    with open("C:\\Users\murme\\PycharmProject\\RegularExpression\\Stud.data","r")as fp:
        filedata=fp.read()
        Marks=re.findall(r"\d{2}",filedata)
        Names=re.findall("[A-Z][a-z]+",filedata)
        print("---------------------------------------------------------")
        print("\t\tMarks\t\tNames")
        print("----------------------------------------------------------")
        for marks,names in zip(Marks,Names):
            print("--------------------------------------------------")
            print("\t\t{}\t\t{}".format(marks,names))
            print("------------------------------------------")
except FileNotFoundError:
    print("File Dose Not Exist")