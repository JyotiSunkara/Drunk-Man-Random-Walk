import random

total = 10000

def pos(n):
    x = 0
    for i in range(n-1):
        if(random.randint(0, 1) == 0):
            x += 1
        else:
            x -= 1
    return x


def probability(n):
    count = 0
    for i in range(total):
        if(pos(n) == pos(n)):
            count += 1
    return count/total


if __name__ == "__main__":
    n = int(input("Enter N: "))
    print("For N="+str(n)+", the probability that the two drunk walkers reach the same point is "+str(probability(n)))
