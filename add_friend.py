#new_name =raw_input("plz add your friend name")
#new_salutation=raw_input("what should we call you ")
#new_name=new_name +" "+ new_salutation
#new_age=int(raw_input("enter your age"))
#new_rating=float(raw_input("enter your rating"))
from globals import friends,spy
import re

def add_friend():
    new_friend = {
        'name': ' ',
        'salutation': ' ',
        'age': 0,
        'rating': 0.0,
        'is online': False

    }
    temp=True
    #validation
    patternsalutation='~Mr|Ms$'
    patternname='^[A-Za-z][A-Za-z\s]+$'
    patternage='^[0-9]+$'
    patternrating='^[0-9]+\.[0-9]$'
    #validating each values using regular expression
    while temp:
        saluation=raw_input("Mr.or Ms. ?:")
        if(re.match(patternsalutation,saluation)!=None):
            temp=False
        else:
            print "Enter again"



     #concatination
    new_friend.Name=saluation +". "+new_friend.Name
    temp=True
    while temp:
        new_friend.age=raw_input("age?")
        if(re.match(patternage,new_friend.Age)!=None):
            temp=False
        else:
            print"Enter again"

    temp=True
    while temp:
        new_friend.Rating=raw_input("Rating of spy")
        if(re.match(patternrating,new_friend.Rating)!=None):
            temp=False
            new_friend.Rating=float(new_friend.Rating)
        else:
            print"Enter again"


     #Now validating age and rating of spy
    if new_friend.Rating <=5.0 and new_friend.Age>12 and new_friend.Age<50 and new_friend.Rating>=spy.Rating:
         #add friend
         friends.append(new_friend)
    else:
         print"Invalid entery"
    #return the length i.e no of friends
    return len(friends)



































































    new_name = raw_input("Please add your new friend name :")
    new_salutation=raw_input("what should we call you")

    new_name=new_name +" " +new_salutation


    new_age = int(raw_input("enter age"))
    new_rating = float(raw_input("spy rating"))

    if len(new_name)>0 and new_age>12 and new_rating>0:
        friends.append(new_friend)#don't forget to declear friends as a global
        print "Friend added"