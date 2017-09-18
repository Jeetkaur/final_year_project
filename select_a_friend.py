from globals import friends
def select_friend():
    counter =1
    #displaying all friend detail
    for friend in friends:  #here friend is a dictionary
      print str(counter) + ".",
      friend.displayDetails(),
      print ""
      counter=counter+1

    if(counter>1):
        temp=True
        #In case if entered value is greater than no. of elemnts
        while temp:
            result=int(raw_input("select from the list : " ))
            if(result<counter):
                temp=False
            else:
                print"Enter coloured value"
    else:
        return -1

    return result - 1

