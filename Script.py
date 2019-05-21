#This script will open an excel file containing words in a language and their
#translate and ask for the user to input the translations. The script will
#then update the 
#
#HOWEVER,before doing so, it will ask what wants to be tested
#       verbs, nouns, others, and all.
#
#The files should have columns containing the following information for each row/word (note, the last two columns should be set to 0 or left empty):
# Type    Det    Singular Dutch    Plural Dutch    Singular english     Plural English   Errors   Uses
#             (or het indefinite)  (or definite)
#
#Example
#
#  Noun    Het    Paard             Paarden          Horse                 Horses        0          0
#
#After writing the xcel file in this way, save it as a .csv file. Make sure to select ; as the delimiter


import random

#Function for sorting
def SortIdx(inlist,r1,r2):
    rang = list(range(r1,r2))
    return [rang for _,rang in sorted(zip(inlist,rang))]

#ask for file to import
#predetlist = str.lower(input('Do you want to use a predetermined set of lists? (yes/no) '))
#
#if predetlist == 'yes':
#    namload = input('Which set of list do you want to use?')
#    #Code should be added when predetermined lists exist
    
#else:


filist = [input('Which file do you want to use: ')]
morfil = [str.lower(input('Do you want to load another file? (yes/no) '))]
while morfil[0] == 'y':
    filist.append(input('Which file do you want to add: '))
    morfil =    str.lower(input('Do you want to load another file? (yes/no) '))

#Files loading loop
nn=0
aa=0
for ff in filist:
    import csv
    with open(ff, newline='') as f:
        readd = csv.reader(f, delimiter=';')
        for row in readd:
            if str.lower(row[0])== "noun":
                if nn == 0:
                    dDet = [row[1]]
                    dNounSing = [row[2]]
                    dNounPlur = [row[3]]
                    eNounSing = [row[4]]
                    eNounPlur = [row[5]]
                    wErr = [int(row[6])]
                    wUse = [int(row[7])]
                    nn += 1    
                else:
                    dDet.append(row[1])
                    dNounSing.append(row[2])
                    dNounPlur.append(row[3])
                    eNounSing.append(row[4])
                    eNounPlur.append(row[5])
                    wErr.append(int(row[6]))
                    wUse.append(int(row[7]))
                    
            elif str.lower(row[0])== "adjective":
                if aa == 0:
                    dAdjSing = [row[2]]
                    dAdjPlur = [row[3]]
                    eAdjSing = [row[4]]
                    aErr = [int(row[6])]
                    aUse = [int(row[7])]
                    aa += 1    
                else:
                    dAdjSing.append(row[2])
                    dAdjPlur.append(row[3])
                    eAdjSing.append(row[4])
                    aErr.append(int(row[6]))
                    aUse.append(int(row[7]))

                    

numit = int(input('How many sentences would you like to translate?'))

#Question loop
it = 0

eSubVerb = ["I have", "You have", "He has"]
eDeter = ["a","the","","the"]#undefined singular, defined singular, undefined plural, defined plural
dSubVerb = ["Ik heb","Je hebt","Hij heeft"]

while it < numit:
    separ = "******************************************"
    #Seach which word to test
    nUseSort = SortIdx(wUse,0,len(dNounSing))
    aUseSort = SortIdx(aUse,0,len(dAdjSing))
    nErrSort = SortIdx(wErr,0,len(dNounSing))
    aErrSort = SortIdx(aErr,0,len(dAdjSing))

    wList = random.sample(nUseSort[0:3] + nErrSort[-1:-3:-1], 5 )#<----------------------------Here to modify ratio of error to new words
    aList = random.sample(aUseSort[0:3] + aErrSort[-1:-3:-1], 5 )

    for nn in range(0,5): #small loop over 5 trials#<----------------------------also Here to modify ratio of error to new words


        rsv = random.randrange(3)
        rdet = random.randrange(4)

        #Figure out which nouns/adjectives/determinants are used
        if rdet < 2:
            tEngNoun = eNounSing[wList[nn]]
            tDutNoun = dNounSing[wList[nn]]
            if rdet == 0:                           #Indefinite
                if str.lower(dDet[wList[nn]]) == 'het':
                    tDutAdj  = "een " + dAdjSing[aList[nn]]    #Het word
                else:
                    tDutAdj  = "een " + dAdjPlur[aList[nn]]    #De word
            elif str.lower(dDet[wList[nn]]) == 'het':         #Definite
                tDutAdj  = "het " + dAdjPlur[aList[nn]]        #Het word
            else:
                tDutAdj  = "de " + dAdjPlur[aList[nn]]         #De word
        else:
            tEngNoun = eNounPlur[wList[nn]]
            tDutNoun = dNounPlur[wList[nn]]

            if rdet == 2: 
                tDutAdj  = dAdjPlur[aList[nn]]
            else:
                tDutAdj  = "de " + dAdjPlur[aList[nn]]

        #Display trial
        tstr = eSubVerb[rsv] + " " + eDeter[rdet] + " " + eAdjSing[aList[nn]] + " " + tEngNoun
        InTrans = str.lower(input('\n %s \n %s \n ' % (separ,tstr) ))

        if InTrans[0:3]=="jij":                             #Replace jij by je to simplify comparisono to answer
            InTrans = "je" + InTrans[3:]

        #Test if the answer is correct
        TruTrans = dSubVerb[rsv] + " " + tDutAdj + " " + tDutNoun

        if str.lower(TruTrans) == InTrans:
            print("Well done!")#---------------------------------------------------------------------------------------------------------add green color and counter
        else:  
            print("Too bad, the right answer is: " + TruTrans)#--------------------------------------------------------------------------Add color to too bad only and
        
        it+=1
        if it == numit:
            numit += int(input('You have translated %i sentences. If you want to do more, write how many, otherwise write 0.' % numit))
            #---------------------------------------------------------------------------------------------------------------------------------Add break statement



print("Goodbye!/Totziens")
