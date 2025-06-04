#Program for Extracting the  Names and Marks from Given Text by using Regular Expressions
#NamesMarksExtractEx1.py
import re
gd="Rossum is  got 56 marks , Ritche got 66 marks, James  got 45 marks and Travis got 76 marks and Kinney got 54 marks"
sp1=r"\d{2}"
sp2="[A-Z][a-z]+"
Marks=re.findall(sp1,gd)
Names=re.findall(sp2,gd)
print("\t\tMarks\t\tNames")
print("-----------------------------------------------------")
for name,marks in zip(Marks,Names):
    print("\t\t{}\t\t{}".format(name,marks))
    print("---------------------------------------------------------------")