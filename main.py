# impoprt statements.
from spy_details import spy
from start_chat import start_chat
from globals import Spy
import re
from termcolor import colored


print "Let's get started!!!"
all=True
#whole variable to iterate if value is not Y/N
while all:
    question = "Do you want to continue as " + spy.Name + "(Y/N) ? "
    existing = raw_input(question)

    # validating users input
    if existing.upper() == "Y":
        # default user
        all=False
        start_chat(spy.Name, spy.Age, spy.Rating, spy.is_Online)

    elif existing.upper() == "N":
        # new user code here
        all=False
        check_all=True#temporary variable
        while(check_all):
            temp_check=True#temporary variable
            # Validation Using Regex
            patternsalutation='^Mr|Ms$'
            patternname='^[A-Za-z][A-Za-z\s]+$'
            patternage='^[0-9]+$'
            patternrating='^[0-9]+\.[0-9]$'
            # Validating Each Values Using Regular Expression
            while temp_check:
                salutation = raw_input("Mr. or Ms.? : ")
                if (re.match(patternsalutation, salutation) != None):
                    temp_check = False

                else:
                    print colored("Enter Again!!!!",'green','on_red')
            temp_check=True
            while temp_check:
                spy.Name=raw_input("Enter Name: ")
                if(re.match(patternname,spy.Name)!=None):
                    temp_check=False
                else:
                    print colored("Enter Again!!!!",'red')
            # concatenation.
            spy.Name = salutation + "."+spy.Name
            temp_check=True
            while temp_check:
                 spy.Age = raw_input("Age?")
                 if (re.match(patternage, spy.Age) != None):
                     temp_check = False
                     spy.Age=int(spy.Age)
                 else:
                     print colored("Enter Again!!!!", 'red')
            temp_check=True
            while temp_check:
                spy.Rating = raw_input("Spy rating?")
                if (re.match(patternrating, spy.Rating) != None):
                    temp_check = False
                    spy.Rating=float(spy.Rating)
                else:
                    print colored("Enter Again!!!!",'red')
            # Checking If Spy is eligible
            if spy.Rating <= 5.0 and spy.Age > 12 and spy.Age < 50:
                start_chat(spy.Name,spy.Age,spy.Rating,spy.is_Online)
                check_all=False
            else:
                print colored("Invalid Entry!!!!Start From Scratch.",'red')
    else:
        print colored("Wrong choice. Try again",'red')