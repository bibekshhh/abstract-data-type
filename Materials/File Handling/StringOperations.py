try: 
    textFile = open("data.txt", 'r')
    array = []
    for x in textFile:
        array.append(x.strip().split(" "))
    print(array)

    textFile.close()
except:
    print("Somehthing went wrong")