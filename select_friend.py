from globals import friends
from termcolor import colored

def select_friend():

    item_number=1
    for friend in friends:
        print str (item_number )+ "."
        friend.displayDetails()
        print "" #to remove extra output
        item_number=item_number+1
    if(item_number>1):
        # create temporary variable
        temp = True
        # If entered value is greater than no. of elements
        while temp:
            result = int(raw_input("Select from the list : "))
            if (result < item_number):
                temp = False
                # If entered value is less than the no. of elements
            else:
                print colored("Enter Correct Value", 'red')
    else:
        return -1
    return result - 1
