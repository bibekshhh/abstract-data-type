#Qno: 3

QueueArray = [""] * 10  #string

HeadPointer = 0 #integer
TailPointer = 0 #integer
NoOfItemsInQueue = 0 #integer

#enqueue function
def Enqueue(QueueArray, HeadPointer, TailPointer, NoOfItemsInQueue, DataToAdd):
    if (NoOfItemsInQueue >= 10):
        return (False, QueueArray, HeadPointer, TailPointer, NoOfItemsInQueue)

    QueueArray[TailPointer] = DataToAdd

    if (TailPointer >= 9):
        TailPointer = 0

    TailPointer += 1
    NoOfItemsInQueue += 1

    return (True, QueueArray, HeadPointer, TailPointer, NoOfItemsInQueue)

#dequeue function
def Dequeue(QueueArray, HeadPointer, TailPointer, NoOfItemsInQueue):
    if (NoOfItemsInQueue == 0):
        return False

    returnData = QueueArray[HeadPointer]
    HeadPointer += 1
    
    if (HeadPointer >= 9):
        HeadPointer = 0
    NoOfItemsInQueue -= 1

    return (returnData, QueueArray, HeadPointer, TailPointer, NoOfItemsInQueue)
    

for x in range(0, 11):
    inputString = input("Enter the data to be added: ")

    returnVal = Enqueue(QueueArray, HeadPointer, TailPointer, NoOfItemsInQueue, inputString)
    if (returnVal == False):
        print('Successful')
    print('Unsuccessful')

print(QueueArray)





