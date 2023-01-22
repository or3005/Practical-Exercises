


# Initialize variables

maxnumber=0
maxsequence=0
count={}
count[0]=-1

# Put the input stream and change it to iterator of int
line=input()
numberlist=list(map(int,line.split()))
iterator = iter(numberlist)


def findsequence(number, maxnumber, maxsequence):
    
    # The stop condition
    if(number==0):
        print(str(maxnumber) + '; ' + str(count[maxnumber]))
        return
    
    #Put the next int element in sequence
    sequence=next(iterator)
    
    #Check if this is the first time we met this value and if not increment the place in its count position 
    if(sequence not in count):
        count[sequence]=1
    else:
        count[sequence] += 1
    
    #Change the values if we found bigger number
    if(maxnumber<sequence):
        maxsequence=count[sequence]
        maxnumber=sequence
   
    #Recursion call
    findsequence(sequence,maxnumber,maxsequence)

#Test
findsequence(2,0,0)
