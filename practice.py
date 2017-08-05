print "caluclator"
choice=raw_input("Enter your choice what do you want to perform: +  for Addition - for for subtraction  * for multiplication / for division");
print choice
num1=int(raw_input("enter first no."))
num2=int(raw_input("enter second no."))


if(choice=='+'):
    print num1+num2
elif(choice=='-'):
    if(num1<num2):
        print"num1 should be greater than num2"
    num3=num1
    num1=num2
    num2=num3
    print num1-num2
elif(choice=='*'):
    print num1*num2
elif(choice=='/'):
    if(num1<0):
        print "enter positive value"

    print num1/num2
else:
    print "plz choose a correct choice"
