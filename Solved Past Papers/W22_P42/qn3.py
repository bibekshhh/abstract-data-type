# a)
global Queue, HeadPointer, TailPointer

Queue = [-1 for x in range(100)]
HeadPointer = -1
TailPointer = 0

# b)
def Enqueue(newItem):
    global TailPointer, HeadPointer
    if TailPointer < 100:
        if HeadPointer == -1:
            HeadPointer = 0
        else:
            Queue[TailPointer] = newItem
            TailPointer += 1
            return True
    return False

# c)
status = False
for x in range(21):
    status = Enqueue(x)

if (status == False):
    print("Unsuccessful")
elif (status == True):
    print("Successful")

# d, e)
def RecursiveOutput(start):
    if start == 0:
        return Queue[start]
    else:
        return Queue[start] + RecursiveOutput(start -1)

print(f"Total: {RecursiveOutput(TailPointer -1)}")

