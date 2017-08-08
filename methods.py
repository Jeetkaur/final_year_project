print "lets play with functions of string"
choice=raw_input("enter your choice:\n1.capitalize() \n2.center()              \n")

if(choice=='1'):                  #only fist letter capitial
    str1 = raw_input("enter string:  ")
    str2= str1.capitalize()
    print str2
elif(choice=='2'):
    str1 = raw_input("enter string: ")
    print str1.center(5,'a')
else:

    print "Invalid! choice"
