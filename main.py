#import statements
from spy_details import spy
from spy_start_chat import start_chat
print "Let's get started"
question="Do you want to continue as " + spy['salutation']+ " " +spy['name'] + "(y/n)"
existing= raw_input(question)
if(existing== 'y' or existing== 'Y'):
    start_chat(spy['name'],spy['age'],spy['rating'],spy['is online'])
elif(existing== 'N' or existing== 'n'):

    spy_name = raw_input("provide your name here: ")
    if len(spy['name']) > 0:
        spy['age'] = 0
        spy['rating'] = 0.0
        spy['is_online'] = False
        spy['salutation'] = raw_input("what should we call  you: ")
        # spy_age=raw_input("Enter your age: ")
        # print type(spy_age)            #it always returns string
        spy['age'] = int(raw_input("Enter your age: "))

        print type(spy['age'])  # it returns int
        if spy['age'] > 12 and spy['age'] < 60:
            spy['rating'] = float(raw_input("Enter spy rating: "))
        if spy['rating'] > 4.5:
            print "you have a great spy_rating"
        elif spy['rating'] >= 3.5 and spy['rating'] <= 4.5:
            print "you are one of the graet one"
        elif spy['rating'] >= 2.5 and spy['rating'] <= 3.5:
            print"you need to do more hardwork"
        else:
            print "You are not eligible to be spy"

        spy['is_online'] = (raw_input("Spy is online or not :"))

        spy['name'] = spy['salutation']+ " " + spy['name']
        print 'welcome ' "" + spy['name'] + " Glad to have you back with "
        print "Alright " + spy['name'] + " I would like to know something about u before we proceed further"
    else:
        print "A spy needs to have a valid name, please try againn"


else:
    print "wrong choice"









