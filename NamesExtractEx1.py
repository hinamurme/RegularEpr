#Program for Extracting the names from Given Text by using Regular Expressions
#NamesExtractEx1.py
import re
gd="Rossum is the author of python , Ritche is the author of c , James is the author of java and Travis is the author of numpy and Kinney is the author of pandas and Kvr is the faculty for python"
sp="[A-Z][a-z]+"
matres=re.findall(sp,gd)
print("Name of List:")
print("------------------------------------------------------------------------")
for mat in matres:
    print("\t{}".format(mat))
    print("---------------------------------------------")
