# from random import randint as rand
import random
import time
# from map import checkXY
from datetime import datetime

def rnd(start, end):
    # time.sleep(random.uniform(0.001, 0.006))
    random.seed(datetime.now().timestamp())
    return random.randint(start, end)

def randbool(percent): #percent - процент вхождения, будем менять по желанию
    # time.sleep(random.uniform(0.001, 0.006))
    random.seed(datetime.now().timestamp())
    tmp = random.randint(0, 100)
    return (tmp <= percent)

def randcell(width, height):
    time.sleep(random.uniform(0.01, 0.06))
    random.seed(datetime.now().timestamp())
    rcW = random.randint(0, width - 1)
    rcH = random.randint(0, height - 1)
    return(rcH, rcW)

def pause(n):
    for i in range(n*1000000):
        i += 1