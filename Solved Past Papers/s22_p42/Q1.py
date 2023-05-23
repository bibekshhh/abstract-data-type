# Q1 (a)
global StackData
global StackPointer

StackData = [0 for i in range(10)]
StackPointer = 0

# Q1 (b)


def PrintStack():
    global StackData
    global StackPointer

    print(StackPointer)
    for i in range(10):
        print(StackData[i])

# Q1 (c)


def Push(newItem):
    global StackPointer
    global StackData

    if StackPointer == 10:
        return False
    else:
        StackData[StackPointer] = newItem
        StackPointer = StackPointer + 1
        return True

# Q1 (d)


def main():
    global StackPointer
    global StackData

    for i in range(11):
        newItem = int(input("Enter a number: "))
        result = Push(newItem)

        if result == True:
            print(f"{newItem} added in stack.")
        else:
            print("Stack is full.")

    PrintStack()


main()


# Q1 (e)
def Pop():
    global StackData
    global StackPointer
    if StackPointer == 0:
        return -1
    else:
        ReturnData = StackData[StackPointer - 1]
        StackPointer = StackPointer - 1
        return ReturnData 