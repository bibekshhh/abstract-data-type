arr = [0]*10

topPointer = 0
basePointer = 1
stackFull = 10

def append(item):
    global topPointer
    if (topPointer < stackFull):
        topPointer += 1
        arr[topPointer] = item
    else:
        print("Cannot append, stack is full")

def remove():
    global topPointer
    if (topPointer == basePointer -1):
        print("Stack is empty, cannot remove")
    else:
        arr[topPointer] = 0
        topPointer -= 1

append(2)
append(5)
append(3)
append(8)
append(9)

print(arr)

remove()
remove()

print(arr)

append(5)
append(3)

print(arr)
