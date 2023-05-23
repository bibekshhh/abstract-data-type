global Jobs, NumberOfJobs

def Initialise():
    global Jobs, NumberOfJobs
    Jobs = [[-1, -1] for x in range(100)]
    NumberOfJobs = 0

def AddJob(jobNumber, jobPriority):
    global AddStatus, NumberOfJobs, Jobs

    if NumberOfJobs == 100:
        print("Not added")
    else:
        Jobs[NumberOfJobs] = [jobNumber, jobPriority]
        print("Added")
        NumberOfJobs += 1


