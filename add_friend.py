# import statements.
from globals import friends,Spy

from spy_details import spy
# add new friends.
import re
from termcolor import colored

def add_friend():
    new_friend =Spy(" "," ",0,0.0,False)
    temp_check=True
    #temporary variable
    #Validation Using regular expressions
    patternsalutation='^Mr|Ms$'
    patternname='^[A-Za-z][A-Za-z\s]+$'
    patternage='^[0-9]+$'
    patternrating='^[0-9]+\.[0-9]$'
    #Validating Each Values Using Regular Expression
    while temp_check:
        salutation = raw_input("Mr. or Ms.? : ")
        if (re.match(patternsalutation, salutation) != None):
            temp_check = False
        else:
            print colored("Enter Again!!!!",'red')
    temp_check=True
    while temp_check:
        new_friend.Name=raw_input("Enter Name: ")
        if(re.match(patternname,new_friend.Name)!=None):
            temp_check=False
        else:
            print colored("Enter Again!!!!",'red')

    # concatenation.
    new_friend.Name = salutation + "."+new_friend.Name
    temp_check=True
    while temp_check:
        new_friend.Age = raw_input("Age?")
        if (re.match(patternage, new_friend.Age) != None):
            temp_check = False
            new_friend.Age=int(new_friend.Age)
        else:
            print colored("Enter Again!!!!",'red')
    temp_check=True
    #temporary variable
    while temp_check:
        new_friend.Rating = raw_input("Spy rating?")
        if (re.match(patternrating, new_friend.Rating) != None):
            temp_check = False
            new_friend.Rating=float(new_friend.Rating)
        else:
            print colored("Enter Again!!!!",'red')
    # validating input->AGE and RATING,i.e.,
    #Age b/w 12 and 50
    #Rating b/w 0.0 to 5.0
    #Rating of friend must be greater than or equal to User Rating
    if new_friend.Rating <= 5.0 and new_friend.Age > 12 and new_friend.Age < 50 and new_friend.Rating>=spy.Rating:
        # add_friend
        friends.append(new_friend)
        print colored("Friend Added",'green')
    else:
        print colored("Sorry invalid entry!!!!",'red')
    # returning number of friends
    return len(friends)