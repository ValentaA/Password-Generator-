import random
print("PASSWORD GENERATOR v.1.1")
print("- - - - - - - - - - ")
print("CRTL+C to exit")
print ("- - - - - - - - - -")

while True:
    print ("# Enter first word:")
    a = input ("# ")
    print(" ")
    print ("# Enter second word:")
    b = input ("# ")
    print(" ")
    c = random.randint(10000,100000)
    d = random.randint(10,100)
    e = random.choice("!#$%&/=?*-_*")
    e2 = random.choice("!#$%&/=?*-_*")
    e3 = random.choice("!#$%&/=?*-_*")

    def passwd(a,b,c,d,e,e2,e3):
        for results in a,b,c,d,e,e2,e3:
            results = a[0:2] + e + str(d) + b[4] + a[-1] + e2 + b[-1:2] + b[0] + str(c) + e3
            return (results)       
    print("# Password:")
    print("-------------------")
    print("#",passwd(a,b,c,d,e,e2,e3))
    print("-------------------")
    print("# Save password to text file?")
    print ("# Yes/No")
    pwd = passwd(a,b,c,d,e,e2,e3)  
    Answer = input("# ")
    if Answer == "Yes" or Answer == "yes":
       print ("# Enter location/file name/file type -> /home/linux/file.txt")
       Pswd_Location = input ("#Save to:   ") 
       with open(Pswd_Location ,"w") as f:
           f.write(str(pwd))
       print ("# Saved to:",Pswd_Location)    
    elif Answer == "No" or Answer == "no":
         pass 
    
    
    
 

  

    
