from select_a_friend import select_friend
from globals import friends
import re
from steganography.steganography import Steganography
def read_message():
    friend_choice=select_friend()
    #checking if friend list is not empty
    if friend_choice!=(-1):
        pattern='^[A-Za-z][0-9A-Za-z\s]*\.jpg$'
        temp=True
        #Average words
        friends[friend_choice].calcAverageWords()
        #prepare the message
        while temp:
            output_image=raw_input("Provide the name of the image to be decrypted:")
            if(re.match(pattern,output_image)!=None):
                temp=False
            else:
                print "Enetr again"
        try:
            text=Steganography.decode(output_image)
            print "Message: ",text
        except TypeError:
            print"image does not have any message"
        except IOError:
            print "Image does not exist"
    else:
        print "Empty Friend's list"
