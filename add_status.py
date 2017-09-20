from termcolor import colored

STATUS_MESSAGES = ["Spy is Online", "Busy, Call If Urgent"]
def add_status():
    temp_check=True
    #temporary variable
    check_all=True
    #temporary variable
    while check_all:
        default = raw_input("Do you want to select from older status (y/n)? ")
        if default.upper() == "N":
            check_all=False
            #Setting new Status Message
            while temp_check:
                new_status_message = raw_input("What status message do you want to set? ")
                if len(new_status_message)>0:
                    updated_status_message = new_status_message
                    STATUS_MESSAGES.append(updated_status_message)
                    temp_check=False
                else:
                    print colored("Please enter a valid status ",'red')

        elif default.upper() == "Y":
            check_all=False
            while temp_check:
                item_position = 1
                #selecting from list(Status)
                for message in STATUS_MESSAGES:
                    print str(item_position) +". "+ str(message)
                    item_position = item_position + 1
                message_selection = int(raw_input("Use Number To Select Desired Status\nEnter Choice:  "))
                if len(STATUS_MESSAGES) >= message_selection:
                    updated_status_message = STATUS_MESSAGES[message_selection - 1]
                    temp_check=False
                else:
                    print colored("Select a proper status",'red')

        else:
            print colored("Wrong choice. Please try again",'red')
    return updated_status_message
