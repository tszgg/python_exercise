"""
A website requires a password to register. As always, there are a set of rules for an allowed password:

1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
3. At least 1 letter between [A-Z]
4. At least 1 character from [$#@]
5. Minimum length of password: 6
6. Maximum length of password: 12

A valid password must satisfy NO LESS THAN (>=) 5 of the rules above.

Write a program to check the validity of password.
Hint: use the `re` library. `re` stands for Regular Expression, with a lot of tutorials online.
"""
 
import re 

def check_password_validity(pw):
    flag = 1
    if (len(pw)<6):
        flag -=1
    if  (len(pw)>12): 
        flag -=1
    if not re.search("[a-z]", pw): 
        flag -= 1
    if not re.search("[A-Z]", pw): 
        flag -= 1
    if not re.search("[0-9]", pw): 
        flag -= 1
    if not re.search("[#@$]", pw): 
        flag -= 1
    #if re.search("\s", pw): 
    #   flag -= 1
    if flag<0:
        return False
    else: 
        return True
          
    
    
good_password = "3GGEsdv2#gv1e4Ob2fbf"  # fails rule #6 only, so good
bad_password = "sgdf3298b"  # fails rule #3 and #4, so bad

#pww="1erfG222222#@$1dd31"
#print(check_password_validity(pww)) 
print(check_password_validity(good_password))  # True
print(check_password_validity(bad_password))    # False
                              


##use+
import re
def check_password_validity(pw):
#pattern = r"([a-z]+)([A-Z]+)([0-9]+)([$#@]+)"
    i=0
    if len(pw)>=6:
        i+=1
    if len(pw)<=12:
        i+=1
    if re.search("[a-z]", pw):
        i+=1
    if re.search("[A-Z]", pw):
        i+=1
    if re.search("[0-9]", pw):
        i+=1
    if re.search("[$#@]", pw):
        i+=1
    if i>=5:
        return True
        
    else:
        return False
        

        
good_password = "3GGEsdv2#gv1e4Ob2fbf"  # fails rule #6 only, so good
bad_password = "sgdf3298b"  # fails rule #3 and #4, so bad

#pww="1erfG222222#@$1dd31"
#print(check_password_validity(pww)) 
print(check_password_validity(good_password))  # True
print(check_password_validity(bad_password))    # False
                              
    
 
 #use-   
                              
import re
                              
def check_password_validity(pw):
    # TODO
    #pattern = r"[a-z]+[A-Z]+[0-9]+($|#|@)"
    fl=2
    if (len(pw)<6):
        fl -=1
    elif  (len(pw)>12): 
        fl -=1
            #break
    elif not re.search("[a-z]", pw): 
        fl -= 1
            #break
    elif not re.search("[A-Z]", pw): 
        fl -= 1
            #break
    elif not re.search("[0-9]", pw): 
        fl -= 1
            #break
    elif not re.search("[#@$]", pw): 
        fl -= 1
            #break
    elif re.search("\s", pw): 
        fl -= 1
            #break
    #elif fl=0:
        #return ("False")
    
       # break
    else: 
            #fl = 0 
        return ("True") 
        #break
        
    # return a boolean `True` if the password is valid, `False` otherwise

good_password = "3GGEsdv2#gv1e4Ob2fbf"  # fails rule #6 only, so good
bad_password = "sgdf3298b"  # fails rule #3 and #4, so bad

print(check_password_validity(good_password))  # True
print(check_password_validity(bad_password))  # False

