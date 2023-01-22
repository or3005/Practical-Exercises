


def findsum(number):
    
    if(number<=0):
        return 0
    else:
        return number%10 +findsum(number//10)
  
    
    
    
#Test
print(findsum(2347623))  