from globals import current_status_message
from read_chat import read_chat
from add_status import add_status
from add_friend import add_friend
from send_message import send_a_message
from read_message import read_message

#start_chat() defination
def start_chat(name ,age ,rating,online):
    show_menu=True
    while (show_menu):
        menu_choices="what do you want to do \n" \
                      "1.Add status \n"\
                      "2.Add friend   \n" \
                      "3.Send a secret message  \n" \
                      "4.Read a secret message   \n" \
                      "5.Read chats \n "\
                      "6.Exit application  \n"

        result=int(raw_input(menu_choices))
        print result
        #validating user input
        if result == 1:
            current_status_message=add_status()
        elif result==2:
            no_of_friends=add_friend()
        elif result == 3:
            send_a_message()
        elif result == 4:
            read_message()
        elif result == 5:
            read_chat()
        elif result == 6:
            menu_choices = False
        else:
            print "Wrong choice.Try again"



