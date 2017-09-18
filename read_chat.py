from steganography.steganography import Steganography
from select_a_friend import select_friend
from globals import friends
def read_chat():
    friend_choice=select_friend()
    #checking if friend list is not empty
    if friend_choice!=-1:
        spyobj=friends[friend_choice]
        # display spy details
        # print colored(spyobject.Name, 'red'), " ", colored(spyobject.Age, 'red')
        #Average words
        spyobj.calcAverageWords()
        #Checking if chat history is not empty
        if(len(spyobj.chat)>0):
            for chatobj in spyobj.chat:
                tempstr=chatobj.Message
                chatobj.Message=Steganography.decode(chatobj.Message)
                chatobj.displayMessage()
                chatobj.Message=tempstr

        else:
            print"No Chat History"



    else:
        print"Empty friends list"