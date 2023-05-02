import sys
import proc
import sort
import average

def main():
    batchfileName = ''
    sortType = ''
    
    if len(sys.argv) != 3:
        print ('Usage: batchSchedulingComparison.py <batchfileName> <sortType>')
    else:
        try:
            batchfileName = sys.argv[1] 
            sortType = sys.argv[2]

            processes, arrivals, bursts = fileScan(batchfileName)
            sortingAlgorithm(sortType, processes, arrivals, bursts)
            
        except IOError: 
            print ('Could not open file using provided filename.')
            sys.exit()

def fileScan(batchFile):
        processes = []
        arrivals = []
        bursts = []
                
        ifile = open(batchFile, 'r').readlines()
        for line in ifile:
            row = line.split(',')
            pid, arrivalTime, burstTime, priority = [i.strip() for i in row]
            process = proc.Proc(pid, arrivalTime, burstTime, priority)
            processes = processes + [ process ]
                
        arrivals = [proc.arrivalTime for proc in processes]
        bursts = [proc.burstTime for proc in processes]

        return processes, arrivals, bursts

def sortingAlgorithm(sortType, processes, arrivals, bursts):
    completeTimes = []
    match sortType:
        case 'FCFS':
            completeTimes, FCFSpids = sort.FirstComeFirstServedSort(processes)
            avgTurnaround, taTimes = average.AverageTurnaround(completeTimes, arrivals)
            avgWait = average.AverageWait(taTimes, bursts)
            print ('\nPID ORDER OF EXECUTION\n')
            for i in range(0, len(FCFSpids)):
                print (str(FCFSpids[i]) + '\n')
            print ('Average Process Turnaround Time: ' + '%.2f' % avgTurnaround + '\n')
            print ('Average Process Wait Time: ' + '%.2f' % avgWait + '\n') 
                    
        case 'ShortestFirst':
            completeTimes, SJFpids = sort.ShortestJobFirstSort(processes)
            avgTurnaround, taTimes = average.AverageTurnaround(completeTimes, arrivals)
            avgWait = average.AverageWait(taTimes, bursts)
            print ('\nPID ORDER OF EXECUTION\n')
            for i in range(0, len(SJFpids)):
                print (str(SJFpids[i]) + '\n')
            print ('Average Process Turnaround Time: ' + '%.2f' % avgTurnaround + '\n')
            print ('Average Process Wait Time: ' + '%.2f' % avgWait + '\n')
                    
        case 'Priority':
            completeTimes, priorityPids = sort.PrioritySort(processes)
            avgTurnaround, taTimes = average.AverageTurnaround(completeTimes, arrivals)
            avgWait = average.AverageWait(taTimes, bursts)
            print ('\nPID ORDER OF EXECUTION\n')
            for i in range(0, len(priorityPids)):
                print(str(priorityPids[i]) + '\n')
            print ('Average Processes Turnaround Time: ' 
                   + '%.2f' % avgTurnaround + '\n')
            print ('Average Processes Wait Time: ' + '%.2f' % avgWait + '\n')

        case _:
            print ('Invalid process scheduling algorithm entered. ' +
                      'Valid options are FCFS, ShortestFirst, or Priority.')

if __name__ == "__main__":
    main()