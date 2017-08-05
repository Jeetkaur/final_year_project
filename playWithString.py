print"lets play wit string and manipulate string using different  operator"
choice=raw_input("enter your choice :\n 1.+ concatination  \n2.* repition  \n3.[] slice  \n4.[ : ] range slice  \n")
#print choice
if(choice=='1'):                                 #use for only concat two string
    str1 = raw_input("enter first string:  ")
    str2 = raw_input("enter string string: ")
    print str1+" "+str2
elif(choice=='2'):                    #creating multiples copies of samestring
    str1 = raw_input("enter first string: ")
    print str1 * 2
elif(choice=='3'):       #get character by define their index
    str1 = raw_input("enter first string: ")
    print str1[3]
elif(choice=='4'):  #give substring
    str1 = raw_input("enter first string: ")
    print str1[1:4]
else:
    print"Invalid! choice"


