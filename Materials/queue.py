queue = [0]*10

headPointer = 0
endPointer = -1
queueFull = 10
queueLength = 0

def enQueue(item):
    global queueLength, endPointer
    if (endPointer < queueFull):
        if (endPointer < len(queue) -1):
            endPointer += 1
        else:
            endPointer = 0
        queue[endPointer] = item
        queueLength += 1

def deQueue():
    global queueLength, headPointer
    if(queueLength == 0):
        print("Queue is empty, cannot dequeue")
        return False
    else:
        queue[headPointer] = 0

        if(headPointer == len(queue)-1):
            headPointer = 0
        headPointer += 1
        queueLength += 1

enQueue(1)
enQueue(1)
enQueue(1)
enQueue(1)
enQueue(1)
enQueue(1)
enQueue(1)
enQueue(1)
enQueue(1)
enQueue(1)

print(queue)

deQueue()
deQueue()
deQueue()
deQueue()
deQueue()

print(queue)

enQueue(1)
enQueue(1)
enQueue(1)

print(queue)
