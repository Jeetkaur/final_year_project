from globals import friends
def select_friend():
    counter =1
    for friend in friends  #here friend is a dictionary
        print str(counter) + "."+friend['name'] + "age : "+str(friend['age'])
        counter=counter+1


    result=int(raw_input("select from the list :"))
    return result-1#return the index