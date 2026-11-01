email = input (" Enter your Email address : ")# g@g.in it is the smallest email ever exist 1
k,j,d=0,0,0
if len(email) >= 6:
    if email[0].isalpha():
        if ("@" in email) and (email.count("@")==1 ):
            if (email[-4]==".") ^ (email[-3]=="."):
              #  if "in" or "com" in email:
                    for i in email:
                        if i==i.isspace():
                            k=1 
                        elif i.isalpha():
                            if i.isupper():
                                j=1
                        elif i.isdigit():
                            continue
                        elif i=="_" or i=="." or i=="@":
                            continue 
                        else:
                            d=1
                    if k==1 or j ==1 or d ==1:
                        print("wrong email")

                    else :
                        print (" hey its right Email HURRAY!")
               # else:
                    #print("try again!")
            else:
                print("Try Again !!")
        else:
            print("Sorry! @ is missing !!")
    else:
        print (" sorry ! email starts with alphabets!!")
else:
    print (" Wrong Email address!! ")
