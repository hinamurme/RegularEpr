#Program for Extracting the Marks from Given Text by using Regular Expressions
#MarksExtractEx1.py
import re
gd="Rossum is  got 56 marks , Ritche got 66 marks, James  got 45 marks and Travis got 76 marks and Kinney got 54 marks"
sd=r"\d{2}"
matres=re.findall(sd,gd)
print("List of Marks")
print("----------------------------------------------------------------------")
for mat in matres:
    print("\t{}".format(mat))
    print("---------------------------------------------------------")