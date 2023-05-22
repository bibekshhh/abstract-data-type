import pickle
import datetime

class Student:
    def __init__(self) -> None:
        self.name = ""
        self.regNo = 0
        self.dateOfBirth = datetime.datetime.now()
        self.fullTime = True

studentRecord = Student()

studentRecord.name = str(input("Enter student's full name: "))
studentRecord.regNo = int(input("Enter registration number: "))
year = int(input("Enter year of birth: "))
month = int(input("Enter month of birth: "))
day = int(input("Enter day of birth: "))

studentRecord.dateOfBirth = datetime.datetime(year, month, day)
studentRecord.fullTime = bool(input("Enter full time status: "))

def writeBinaryFile():
    try: 
        studentFile = open("students.dat", "w+b")
        pickle.dump(studentRecord, studentFile)

        print("=============== Write Binary File ===============")
        print("")

        print("Successfully added data.")
        print(f"Name: {studentRecord.name} | RegNo. : {studentRecord.regNo} | DOB: {studentRecord.dateOfBirth} | FullTimeStatus: {studentRecord.fullTime}")

        studentFile.close()
    except:
        print("Something went wrong:")

def readBinaryFile():
    try: 
        studentFile = open("students.dat", "rb")
        studentRecord = pickle.load(studentFile)

        print("")
        print("=============== Read Binary File ===============")
        print("")

        print("Successfully fetched data.")
        print(f"Name: {studentRecord.name} | RegNo. : {studentRecord.regNo} | DOB: {studentRecord.dateOfBirth} | FullTimeStatus: {studentRecord.fullTime}")

        studentFile.close()
    except:
        print("Something went wrong:")

writeBinaryFile()
readBinaryFile()