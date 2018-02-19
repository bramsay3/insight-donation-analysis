import numpy as np
from register import (donation, donerTracker, fileDonation, recipiantTracker)
import sys




#check to make sure the the number of inputs are equal to 3
inputLen = len(sys.argv)
inputNum = 4

if inputLen != inputNum:
    if inputLen < inputNum:
        raise NameError('Too few inputs! Three text files are needed for input')
    else:
        raise NameError('Too many inputs! Three text files are needed for input')

#read in text files
pFile = open(sys.argv[2], 'r')
percentile = int(pFile.read())

#A shared dictionary for collecting recipiant information from donations
recipiantData = {}

#A shared dictionary for collecting information about who gives donations
donateBin = {}

outFile = open(sys.argv[3],'a+')

dFile = open(sys.argv[1], 'r')
for line in dFile:
    collected = donation(line)

    #If the donation is not from an individual disregard
    if collected.other == False:
        continue
    key = collected.name + str(collected.zip)
    giftFile = fileDonation(key, collected, donateBin, donerTracker)

    if giftFile.repeat:
        repeatGift = giftFile.selectRepeat()

        repeatKey = repeatGift.CMTE_ID + str(repeatGift.zip) + str(repeatGift.year)
        recipiantInfo = fileDonation(repeatKey, repeatGift, recipiantData, recipiantTracker)

        recipiantSummary = recipiantInfo.toString(percentile)
        outFile.write(recipiantSummary+'\n')






