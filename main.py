import numpy as np
import pandas as pd

## TODO - Arrange part one into columns (round robin)
## TODO - Arrange part two into columns (divide/4 and split)
## TODO - rand function to select from columns
## TODO - cat columns together
## TODO - wrap and add discord components
## TODO - create function to call 

divider = '`@@@@@`'

itemList=[]
for item in pd.read_csv('raccoon-society-phrases.csv'):
    itemList.append(str(item).strip())

itemListDivided = [[],[],[],[]]
count = 0

## The first part of the list was done using a alternating item list as columns were read 
## from a ocr from left to right as opposed to
  
for item in range(len(itemList[0:31])):
    if count == 0 :
        itemListDivided[0].append(itemList[item])
        count= 1
    elif count == 1:
        itemListDivided[1].append(itemList[item])
        count= 2
    elif count == 2:
        itemListDivided[2].append(itemList[item])
        count = 3
    elif count == 3:
        itemListDivided[3].append(itemList[item])
        count = 0

[print(item) for item in itemListDivided]