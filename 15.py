import re
def find(s):
     charRe  = re.compile(r"^7")
     if  charRe.match(s):
         return True
     else :
         return False   


s= input()
print (find(s) )