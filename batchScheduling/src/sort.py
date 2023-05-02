def FirstComeFirstServedSort(batchFileData):
        
    startTime = []
    endTime = []
    sTime = 0
        
    sortedProcesses = sorted(batchFileData, key=lambda x: (int(x.arrivalTime), x.pid))
        
    sortedPids = [o.pid for o in sortedProcesses]
    completeTimes = [o.burstTime for o in sortedProcesses]
    arrivalTimes = [o.arrivalTime for o in sortedProcesses]
        
    for i in range(len(sortedProcesses)):
        if (sTime < int(arrivalTimes[i])):
            sTime = int(arrivalTimes[i])
        startTime.append(sTime)
        sTime = sTime + int(completeTimes[i])
        eTime = sTime
        endTime.append(eTime)
        completeTimes[i] = eTime
                
    return completeTimes, sortedPids

def ShortestJobFirstSort(batchFileData):

    completeTimes = []
        
    complete = 0
    t = 0
    minimum = 999999999
    shortest = 0
    n = len(batchFileData)
    check = False
            
    sortedProcesses = sorted(batchFileData, key=lambda x: (x.pid, int(x.arrivalTime)))
        
    remainingTime = [o.burstTime for o in sortedProcesses]
    sortedPids = [o.pid for o in sortedProcesses]
    arrivalTimes = [o.arrivalTime for o in sortedProcesses]
        
    pids = []
        
    for i in range (0, n):
        remainingTime[i] = int(remainingTime[i])
        arrivalTimes[i] = int(arrivalTimes[i])
            
    while (complete != n):
        for j in range (n):
            if ((arrivalTimes[j] <= t) and (remainingTime[j] < minimum) 
                   and remainingTime[j] > 0):
                minimum = remainingTime[j]
                shortest = j
                check = True
                pids.append(sortedPids[j])
        if (check is False):
            t += 1
            continue
                    
        remainingTime[shortest] -= 1
        minimum = remainingTime[shortest]
        if (minimum == 0):
            minimum = 999999999
                
        if (remainingTime[shortest] == 0):
            complete += 1
            check = False
                    
            fint = t + 1
            completeTimes.append(fint)
                    
        t += 1
            
    return completeTimes, pids
    
def PrioritySort(batchFileData):

    startTime = []
    endTime = []
    sTime = 0
        
    sortedProcesses = sorted(batchFileData, key=lambda x: (
                    int(x.arrivalTime), int(x.priority), x.pid))
        
    sortedPids = [o.pid for o in sortedProcesses]
    completeTimes = [o.burstTime for o in sortedProcesses]
    arrivalTimes = [o.arrivalTime for o in sortedProcesses]
        
    for i in range(len(sortedProcesses)):
        if (sTime < int(arrivalTimes[i])):
            sTime = int(arrivalTimes[i])
        startTime.append(sTime)
        sTime = sTime + int(completeTimes[i])
        eTime = sTime
        endTime.append(eTime)
        completeTimes[i] = eTime
        
    return completeTimes, sortedPids