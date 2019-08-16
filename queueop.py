from pythonds.basic import Queue

def hotline(namelist,num):
    simqueue=Queue()
    for name in namelist:
        simqueue.enqueue(name)

    while simqueue.size()>1:
        for i in range(num):
            simqueue.enqueue (simqueue.dequeue())
        simqueue.dequeue()
    return simqueue.dequeue()
print(hotline(["joseph","devi","subha","kani","abel","jeffrey"],5)) 
