import random
def randomNum5():
    n = 5
    i = 0
    frontNum = [0] * 5
    while i < n :
        num = random.randint (1,35)
        if checkNum(num,frontNum) :
            frontNum[i] = num
            i = i + 1
            
    return(frontNum)

    



def randomNum2():
    n = 2
    i = 0
    backNum = [0] * 2
    while i < n :
        num = random.randint (1,12)
        if checkNum(num,backNum) :
            backNum[i] = num
            i = i + 1
            
    return(backNum)

    

def checkNum(num,lst):
    #ensure the nums are not duplicated
    i = 0
    n = len(lst)
    while i < n :
        if int(lst[i]) == num :
            return False
        i = i + 1
    return True


def lottoPrint(list):
    n = len(list)
    i = 0
    while i < n :
        print("%s " % list[i],end="" )
        i = i +1
    