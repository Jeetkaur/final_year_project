STATUS_MESSAGE =['my message',45]
def add_status(current_status_message):
    if current_status_message != None:
        print "current status is  "+current_status_message
        print STATUS_MESSAGE
    else:
        print "you don't update any status"

default = raw_input("Do you want to select from the older status(y/n)")

if default.upper() == "N":
    new_status_message= range("what status do you want to set")
    if(new_status_message>0):
        updated_status_message=new_status_message
        STATUS_MESSAGE.append(new_status_message)  #STATUS_MESSAGE is a list
elif default.upper() =="y" :
    item_position =1
    for message in STATUS_MESSAGE:
        print item_position + "." +message
        item_position=item_position+1
    message_selection=int(raw_input("select from the above message"))
    if(len(STATUS_MESSAGE)>= message_selection):
         updated_status_message=STATUS_MESSAGE[message_selection-1]




