from steganography.steganography import Steganography
# list to storeuser friend information
friends=[]

#current status message is initalized none

current_status_message=None



#spy class
class spy:
    def _init_ (self,salutation,name,age,rating,isonline):
        #initialize the values
         self.Saluatation=salutation
         self.Name= name
         self.Age=age
         self.Rating=rating
         self.Online=isonline
         self.chat=[]
    def displayDetails(self):
        print self.Name," ",self.Age

    def calcAverageWords(self):
            # Average Words Spoken
            avg = 0
            if len(self.chat) != 0:
                for i in self.chat:
                    avg = avg + len(Steganography.decode(i.Message))
                avg = avg / (len(self.chat))
            print "Average Words Spoken: ", avg

# Chat class
class Chat:
    def __init__(self, msgImage, timestamp):
         # Assigning Values
         self.Message = msgImage
         self.Timestamp = timestamp

    def displayMessage(self):
          print"after that"













