# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 18:05:19 2022

@author: Sagar_Maher
"""

import re

housenumber = []
street = []
dictStreet =  {}

def GetResult(StringInput):
    StringInput = re.sub('[^A-Za-z0-9ä]+', ' ', StringInput)
    itemList = StringInput.split(" ")
    print(itemList)
    for i in itemList:
        if i.isdigit() or i.endswith('B'):
            housenumber.append(i)
        else:           
            street.append(i)

    dictStreet["street"] = ' '.join(street)            
    dictStreet["housenumber"] = ' '.join(housenumber)
    return dictStreet

def formatGetResult(formatInput):
    formatInput = re.sub('[^A-Za-z0-9]+', ' ', formatInput)
    if "No" in formatInput:
        street = formatInput.split(" No")[0]
        housenumber = "No " + formatInput.split("No")[1]
        dictStreet["street"] = ''.join(street)            
        dictStreet["housenumber"] = ''.join(housenumber)
    elif formatInput.endswith(' b'):
        index = formatInput.index(" b") - 2
        street  = formatInput.split(formatInput[index:])[0]
        housenumber = formatInput[index:]
        dictStreet["street"] = ''.join(street)            
        dictStreet["housenumber"] = ''.join(housenumber)
    return dictStreet



def main():
    StringInput = "Calle 39 No 1540"
    if "No" in StringInput or StringInput.endswith(' b'):
        result = formatGetResult(StringInput)
    else:
        result = GetResult(StringInput)
    
    print(result)

if __name__ == "__main__":
    main()


 



