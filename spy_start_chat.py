#start_chat() defination
def start_chat(name ,age ,rating):
    show_menu=True
    while (show_menu):
        menu_choices="what do you want to do: \n 1.Add status  \n2. Exit application "
        result=int(raw_input(menu_choices))
        #validating user input
        if result == '1':
            print "status update"
        elif result=='2':
            show_menu=False
        else:
         print"wrong choice"


