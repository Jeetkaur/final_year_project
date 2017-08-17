#start_chat() defination
def start_chat(name ,age ,rating,online):
    show_menu=True
    while (show_menu):
        menu_choices="what do you want to do :"  "\n"  " 1.Add status" "\n" "2.Add friend " "\n" "3.Send a secret message "  "\n" "4.Read a secret message ""\n" "5.Exit application "

        result=int(raw_input(menu_choices))
        print result
        #validating user input
        if result == 1:
            print "status update"
        elif result==2:
            print "Add friend"
        elif result == 3:
            print "Send  a secret message"
        elif result == 4:
            print "Read  a secret message"
        elif result == 5:
            print "Exit"

        else:
         print"wrong choice"


