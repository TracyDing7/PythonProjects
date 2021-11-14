import math
import random
import statistics

numlist=[]
def rolldice(min,max):
    i=0
    while i<100:
        number=random.randint(min,max)
        numlist.append(number)
        i+=1


rolldice(1,20)
##calculate the average of the roles
avg = statistics.mean(numlist)
print(f"Average of 100 rolls : {avg}")


print("#####stdev#####")
stdev = statistics.stdev(numlist)
print(stdev)
onenumlist=[]

def exsquare():
    squaresum = 0
    for x in range(1, 21):
        squaresum += x**2
    squaresum = squaresum / 20
    return squaresum

def mymean():
    sum = 0
    for x in range(1,21):
        sum+=x
    return sum/20

stdev1 = exsquare() - (mymean() ) ** 2
print("#####calculated stdev#####")
print(math.sqrt(stdev1))




