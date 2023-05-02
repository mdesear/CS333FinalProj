class Proc:

	def __init__(self, pid, arrivalTime, burstTime, priority):
		self.pid = pid
		self.arrivalTime = arrivalTime
		self.burstTime = burstTime
		self.priority = priority
		
	def getPid(self):
		return self.pid
		
	def getArrival(self):
		return self.arrivalTime
		
	def getBurst(self):
		return self.burstTime
		
	def getPriority(self):
		return self.priority