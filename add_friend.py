#new_name =raw_input("plz add your friend name")
#name_salutation=raw_input("what should we call you ")
#new_name=new_name +" "+ name_salutation
#name_age=int(raw_input("enter your age"))
#name_rating=float(raw_input("enter your rating"))

def add_friend():
    new_friend = {
        'name': ' ',
        'salutation': ' ',
        'age': 0,
        'rating': 0.0,
        'is online': False

    }
    new_name = raw_input("Please add your new friend name :")
    new_salutation=raw_input("what should we call you")

    new_name=new_name +" " +new_salutation


    new_age = int(raw_input("enter age"))
    new_rating = float(raw_input("spy rating"))

    if len(new_name)>0 and new_age>12 and new_rating>0:
        friends.append(new_friend)#don't forget to declear friends as a global
        print "Friend added"