from steganography.steganography import Steganography
import re
from datetime import datetime
from globals import friends,Chat
from select_a_friend import select_friend
def send_a_message():
    friend_choice=select_friend()
    #check first if list is not empty
    if friend_choice!=-1:
        pattern='^[A-Za-z][0-9A-Za-z\s]*\.jpg$'
        patternsave='^SOS|SAVE ME|IN DANGER|HELP$'
        temp1=True
        #prepare the message
        while temp1:
            original_image=raw_input("Prvide the name of the image to hide the message")
            if(re.match(pattern,original_image)!=None):
                temp1=False
            else:
                print"enter again"

        temp1=True
        while temp1:
            output_image=raw_input("Provide the name of the  output image :")
            if(re.match(pattern,output_image)!=0):
                temp1=False
        text=raw_input("Enter your text here")
        if(len(text)>100): #In case if friend type more than words remove from friends list
            print"Lage message input"
            print"You are no more a spy"
            friends.remove(friends[friend_choice])
        else:
            try:                     #Encrpt the message
                Steganography.encode(original_image, output_image, text)
                chatobject=Chat(output_image,datetime.now())
                friends[friend_choice].chat.append(chatobject)  #Sucessful message

                print "Your message encrypted sucessfully"
                #Handling situation for SOS|Danger
                if(re.match(patternsave,text.upper())!=None):
                    print "I got your location!!!!I'll be there soon!"


            except IOError:
                print"Image %s Does Not Exist !!!"%(original_image)

    else:
        print"Empty Friends list"

















































    #prepare the  message
    original_image=raw_input("provide the name of the image to hide the message")
    output_image=raw_input("provide the name of the output image")
    text=raw_input("enter your text here: ")
    #encrypt the message here
    Steganography.encode(original_image,output_image,text)