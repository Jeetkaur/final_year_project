print "Let's get started"
spy_name=raw_input("provide your name here: ")
if len(spy_name)> 0:
    spy_age=0
    spy_rating=0.0
    spy_is_online=False
    spy_salutation = raw_input("what should we call  you: ")
    #spy_age=raw_input("Enter your age: ")
    #print type(spy_age)            #it always returns string
    spy_age = int(raw_input("Enter your age: "))
    print type(spy_age)  # it returns int
    if spy_age > 12 and spy_age <60:
        spy_rating=float(raw_input("Enter spy rating: "))
    if spy_rating>4.5:
        print "you have a great spy_rating"
    elif spy_rating>=3.5 and spy_rating <= 4.5:
        print "you are one of the graet one"
    elif spy_rating>=2.5 and spy_rating <=3.5:
        print"you need to do more hardwork"
    else:
        print "You are not eligible to be spy"

    spy_is_online=(raw_input("Spy is online or not :"))
    spy_name = spy_salutation+" "+spy_name
    print 'welcome ' ""   + spy_name + " Glad to have you back with "
    print "Alright " + spy_name + " I would like to know something about u before we proceed further"
else:
    print "A spy needs to have a valid name, please try againn"

