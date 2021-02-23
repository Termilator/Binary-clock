import datetime
from tkinter import * 
from tkinter.ttk import *

# creating the graphic window
window = Tk()
window.title("Binary clock [hours:minutes]")
timelabel = Label(window, font=("courier", 30, "bold"),foreground ="white", background = "black")
timelabel.pack(anchor="center")

# defining when the hour numbers switch to 1
def hours():

    hourBin = [0, 0, 0, 0, 0, 0]
    
    # get current time, hours and minutes
    ttime = datetime.datetime.now()
    hour = ttime.hour

    # hour bin1
    if(hour %2 != 0):
        hourBin[5] = 1

    # hour bin2
    hbin2list = [2,3,6,7,10,11,14,15,18,19,22,23]
    if hour in hbin2list:
        hourBin[4] = 1

    # hour bin4
    hbin4list = [4,5,6,7,12,13,14,15,20,21,22,23]
    if hour in hbin4list:
        hourBin[3] = 1

    # hour bin8
    if (hour >= 8) and (hour <= 15):
        hourBin[2] = 1

    # hour bin16
    if (hour >= 16) and (hour <= 23):
        hourBin[1] = 1
   
    return hourBin
   
# defining when the minute numbers switch to 1
def minutes():
    
    minuteBin = [0, 0, 0, 0, 0, 0]

    mTime = datetime.datetime.now()
    minute = mTime.minute

    # minute bin 1
    if(minute %2 != 0):
        minuteBin[5] = 1

    # minute bin2
    mbin2list = [2,3,6,7,10,11,14,15,18,19,22,23,26,27,30,31,34,35,38,39,42,43,46,47,50,51,54,55,58,59]
    if minute in mbin2list:
        minuteBin[4] = 1

    # minute bin4
    mbin4list = [4,5,6,7,12,13,14,15,20,21,22,23,28,29,30,31,36,37,38,39,44,45,46,47,52,53,54,55]
    if minute in mbin4list:
        minuteBin[3] = 1

    # minute bin8
    if ((minute >= 8) and (minute <=15)) or ((minute >= 24) and (minute <= 31)) or ((minute >= 40) and (minute <= 47)) or (minute >=56):
        minuteBin[2] = 1

    # minute bin16
    if ((minute >= 16) and (minute <= 31)) or (minute >= 48):
        minuteBin[1] = 1

    # minute bin32
    if minute >= 32:
        minuteBin[0] = 1
    
    return minuteBin

# printing and updating the binaries to the graphic window
def printClock(list1, list2):
    
    stringi1 = ' '.join(map(str, list1))
    stringi2 = ' '.join(map(str, list2))

    timelabel.config(text=stringi1 + " : " + stringi2)
    timelabel.after(2000, main)
  
# main program that runs until stopped
def main():

    while True:

        hourlist = hours()
        minlist = minutes()
        printClock(hourlist, minlist)        
        mainloop()

if __name__ == '__main__':
    main()
