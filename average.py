def AverageTurnaround(processCompletionTimes, processArrivalTimes):
			
	averageTurnaround = 0.0
	numProcesses = 0
	turnaroundTimes = []
			
	completionTimes = list(processCompletionTimes)
	arrivalTimes = list(processArrivalTimes)
			
	for i in range(len(processCompletionTimes)):
		turnaroundTimes.append(int(completionTimes[i]) - int(arrivalTimes[i]))
		numProcesses += 1
				
	turnaroundSum = sum(turnaroundTimes)
	averageTurnaround = float(turnaroundSum / numProcesses)
				
	return averageTurnaround, turnaroundTimes

def AverageWait(processTurnaroundTimes, processBurstTime):
		
	averageWait = 0.0
	numProcesses = 0
	waitTimes = []
		
	turnaroundTimes = list(processTurnaroundTimes)
	burstTimes = list(processBurstTime)
		
	for i in range(len(turnaroundTimes)):
		waitTimes.append(int(turnaroundTimes[i]) - int(burstTimes[i]))
		numProcesses += 1

	waitSum = sum(waitTimes)
	averageWait = float(waitSum / numProcesses)
	return averageWait