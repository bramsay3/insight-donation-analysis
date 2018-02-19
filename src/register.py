
import numpy as np


#Error checks if a value already exits and possible occurences of collisions
def fileDonation(key, gift, folder, storage):
    if key not in folder:
        folder[key] = storage(gift)
        return folder[key]
    else:
        giftFile = folder[key]
        if giftFile.sameEntry(gift):
            giftFile.addDonation(gift)
            return giftFile
        else :
            #Rehash with different key - acts as tombstone but requires manual check
            return fileDonation(key+a, gift, folder)

class donation(object):
    """
    Stores donation information
    """

    def __init__(self, donStr):
        self.acceptDonation(donStr)

    def acceptDonation(self, donationLine):
        fields = donationLine.split("|")
        self.CMTE_ID = fields[0]
        self.name = fields[7]
        self.zip = int(fields[10][:5])

        self.day = int(fields[13][:2])
        self.month = int(fields[13][2:4])
        self.year = int(fields[13][-4:])

        self.amt = float(fields[14])
        self.other = True if fields[15]=='' else False

class donerTracker(object):
    """
    Keeps track of repeat donation information
    """

    def __init__(self, gift):
        self.name = gift.name
        self.zip = gift.zip

        self.repeat = False
        self.donations = [gift]
        self.donationDate = [self.getDate(gift)]
        self.oldestDate = self.donationDate
        self.oldestIDX = 0

    def addDonation(self, gift):
        self.repeat = True
        self.donations.append(gift)
        self.donationDate.append([self.getDate(gift)])

    def getDate(self, gift):
        year = gift.year * int(1e4)
        month = gift.month * int(1e2)
        day = gift.day

        date = year + month + day
        return date

    #Checks that two people arn't counted as the same should there be a dictionary collision 
    def sameEntry(self, gift):
        sameZip = self.zip == gift.zip
        sameName = self.name == gift.name
        return np.all([sameZip,sameName])

    def selectRepeat(self):
        #print out the most recent date and have the older one wait
        if self.oldestDate > self.donationDate[-1]:
            repeatIDX = self.oldestIDX
            self.oldestDate = self.donationDate[-1]
            self.oldestIDX = len(self.donations)-1
            return self.donations(repeatIDX)
        else:
            return self.donations[-1]

    def repeatedDoner(self, gift):
        key = gift.CMTE_ID + str(gift.zip) + str(gift.year)
        fileDonation(key, gift, recipiantData, recipiantTracker)


class recipiantTracker(object):

    def __init__(self, gift):
        self.recipiant = gift.CMTE_ID
        self.zip = gift.zip
        self.year = gift.year
        self.contributions = [gift.amt]
        self.totalContributions = gift.amt
        self.transactions = 1

    def addDonation(self, gift):
        self.contributions.append(gift.amt)
        self.totalContributions += gift.amt
        self.transactions += 1

    def sameEntry(self, gift):
        sameRecipiant = self.recipiant == gift.CMTE_ID
        sameZip = self.zip == gift.zip
        sameYear = self.year == gift.year
        return np.all([sameRecipiant,sameZip,sameYear])

    def toString(self, percentile):
        perAmt = int(np.floor(len(self.contributions) * percentile / 100))
        roundPer = np.round(self.contributions[perAmt])


        printString = str(self.recipiant) + '|' + \
                      str(self.zip) + '|' + \
                      str(self.year) + '|' + \
                      str(roundPer) + '|' + \
                      str(self.totalContributions) + '|' + \
                      str(self.transactions)

        return printString




