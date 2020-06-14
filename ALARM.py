#@author: Şükrü Erdem Gök
#@date:14/35/2020
#Python 3.8 Windows
#Note: for only windows

#Python alarm

#LIB
from time import strftime
from winsound import Beep
from sys import exit

#Main function
def alarm():

    #Get values
    hour=int(input("HOUR: "))
    minute=int(input("MIN: "))

    #Check
    while True:

        #İf user wrote 1 or 5, change into 01 or 05
        if(hour/10<1):
            hour="0"+str(hour)

        if(minute/10<1):
            minute="0"+str(minute)

        #İf it' s time
        if str(hour)==str(strftime("%H")) and str(minute)==str(strftime("%M")):
            print("***************")
            print("IT'S TIME !!!!")
            print("***************")
            i = 37
            while True:
                #Beep(frequenty, duration(msec))
                Beep(1000, 700)
                Beep(1000, 700)
                Beep(2500, 500)

#Try
try:
    alarm()

#Give one more chance
except:

    #Try
    try:
        alarm()

    #No more chances :)
    except:
        exit(0)
