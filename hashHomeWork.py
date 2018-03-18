#!/usr/bin/env python

##############################################################################################
## A Python Program to perform Hash Function, which creates Hash of a file in 32 Bit Format ##
##############################################################################################

## Importing the following Modules Since they are used in the code ##
import BitVector as BV
import glob as dir
import binascii as BA

## Function To Do Hashing of all Files in a Directory ##
def hashFunction():
    #print "Hash Function Called"
    hash = BV.BitVector (size = 32)   ## 32 Bit Zero's
    #print type(hash)

    files = dir.glob('*.*')                                        ## Glob used to get all the Files in the Current Directory. ## 
    
    ## If the Files in the Directory is none or only the Python Program.. Creating a new Sample File ##
    if (len(files) <= 1):
        newFile = open ('createdNewFile.txt','w')
        newFile.write("A file Created for the Purpose of Hashing")
        newFile.close()
        files = dir.glob('*.*')

    outputFile = open('outputHashFunction.txt', 'w')
   
    print "File Name                               " , " : " , "Hash Value of the File"    
    print "---------------------------------------------------------------------------"
    for fileName in files:
        currFile = BV.BitVector(filename = fileName)

        while(currFile.more_to_read):
            xor = currFile.read_bits_from_file(8)
            hash << 4                                               ## Circular Shift Left by 4 digits to the Left ##
            hash[0:8] = xor ^ hash[0:8]                             ## Xor the Bits as they are read ##
        
        hashnew = hash.getHexStringFromBitVector()                  ## Converting the Bits to Hexa Decimal Form ##
        hash = BV.BitVector (size = 32)                             ## 32 Bit Zero's, Re-Initializing for the Next File ##
        outputFile.write(hashnew)
        outputFile.write("\n")
        print fileName .ljust(40), " : ", hashnew                   ## Printing The Output to Console ##
    print "---------------------------------------------------------------------------"
    print "All Hash Values are Dumped to a output File Named: outputHashFunction.txt"
    outputFile.close()
    #print "Leaving Hash Function
## Funtion End ##

## Function to Check Collisions from the Output File ##
def checkHashCollision():
    print "---------------------------------------------------------------------------"
    print "Checking For Collisions"
    outputFile = open ('outputHashFunction.txt', 'r')
    #outputFile.read()

    bool = False
    hashList = [fileName for fileName in outputFile]

    if (len(hashList) == len(set(hashList))):               ## Checking if all the data is unique, if Not Unique then collision is present ##
        bool = False
    else:
        bool = True

    if ( bool ):
        print "There is a Collision in the Output File "
    else:
        print "There is no Collision in the Output File"    
    # previous = ""
    # for present in outputFile:
    #     print present
    #     if (previous == present and previous != ""):
    #         bool = True 
    #         break

    #     else:
    #         previous = present
    #         bool = False
## Function End ##

## Program Starts Executing Here ##
if __name__ == '__main__':
    print "------------------------------Program Started------------------------------"
    hashFunction()                                          ## Calling the Hash Function ##
    checkHashCollision()                                    ## Calling the Check Collision Function ##
    print "------------------------------Program Ended  ------------------------------"
## Program End ##