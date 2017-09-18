STATUS_MESSAGE =['my message',45]
def add_status():
    temp=True
    whole=True
    while whole:
        default=raw_input("Do you want to select from older status (y/n)")
        if default.upper()=="N":
            whole=False
            #setting of new new status message
            while temp:
                new_status_message=raw_input("What status do you want set?")
                if len(new_status_message)>0:
                    updated_status_message=new_status_message
                    STATUS_MESSAGE.append(updated_status_message)
                    temp=False
                else:
                    print "Please enter a valid status"



        elif default.upper=="Y":
            whole=True
            while temp:
                item_position=1
                #selecting status from list of status
                for message in STATUS_MESSAGE :
                    print str(item_position) + "." +str(message)
                    item_position=item_position+1
                message_selection=int(raw_input("Use number to select desired status \Enter your choice"))
                if(len(STATUS_MESSAGE))>=message_selection:
                    updated_status_message=STATUS_MESSAGE[message_selection-1]
                    temp=False
                else:
                    print "Select a proper status"


        else:
            print "Wrong choice ,Please try again"

    return updated_status_message





















