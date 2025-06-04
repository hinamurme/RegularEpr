#Program for Validation of Mobile Number with Regular Expression.
#MobileNumberValidationEx1.py
import  re
while(True):
    mno=input("Enter Ur Mobile Number:")
    if(len(mno)==10):
        res=re.search(r"\d{10}",mno)
        if(res!=None):
            print("\t{} Is Valid Mobile Number".format(mno))
            break
        else:
            print("\t{} Is In Valid Mobile Number-Must Contains int Values Only--try again".format(mno))
    else:
        print("\t{} Is Invalid Mobile Number Length----try again".format(mno))