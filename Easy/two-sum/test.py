import random
import time


def Test(function, min_n=10, max_n=15):
    elements = []
    times = []
    for i in range(min_n,max_n):
        randomList = [random.randint(0,i) for x in range(i)]
        target = random.randint(0,i)
        start = time.clock()
        t = function(randomList, target)
        total_time = time.clock()-start
        elements.append(len(randomList))
        times.append(total_time)
    return elements,times