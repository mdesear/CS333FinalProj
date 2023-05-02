from batchScheduling.src import batchSchedulingComparison, average, proc, sort
import unittest
from unittest.mock import patch, mock_open, call

test_procs = [proc.Proc(1, 2, 5, 4), proc.Proc(2, 10, 16, 1), 
              proc.Proc(3, 8, 20, 3), proc.Proc(4, 1, 3, 2)]
test_arrivals = [2, 10, 8, 1]
test_bursts = [5, 16, 20, 3]

class TestIntegration(unittest.TestCase):
    def test_fileScanProcs(self):
        
        with patch("builtins.open", mock_open(
            read_data="1,2,5,4\n2,10,16,1\n3,8,20,3\n4,1,3,2")) as mock_file:
                test_procResults, test_arrivalResults, test_burstResults = (
                     batchSchedulingComparison.fileScan(mock_file))
                for i in range (len(test_procs)):
                    self.assertEqual(int(test_procs[i].pid), int(
                         test_procResults[i].pid))
                    self.assertEqual(int(test_procs[i].arrivalTime), 
                                     int(test_procResults[i].arrivalTime))
                    self.assertEqual(int(test_procs[i].burstTime), 
                                     int(test_procResults[i].burstTime))
                    self.assertEqual(int(test_procs[i].priority), int(
                         test_procResults[i].priority))
                    self.assertEqual(int(test_bursts[i]), int(test_burstResults[i]))
                    self.assertEqual(int(test_arrivals[i]), int(test_arrivalResults[i]))

    @patch("builtins.print")
    def test_fcfs(self, mock_print):
        test_completeTimes, test_fcfsPids = sort.FirstComeFirstServedSort(test_procs)
        test_avgTurnaround, test_taTimes = average.AverageTurnaround(
                                                  test_completeTimes, test_arrivals)
        test_pidOrder = []

        for i in range(len(test_fcfsPids)):
             test_pidOrder.append(str(test_fcfsPids[i]) + "\n")

        test_avgWait = average.AverageWait(test_taTimes, test_bursts)
        batchSchedulingComparison.sortingAlgorithm("FCFS", test_procs, 
                                                   test_arrivals, test_bursts)
        self.assertEqual(mock_print.mock_calls, [call("\nPID ORDER OF EXECUTION\n"),
                                                 call(str(test_pidOrder[0])),
                                                 call(str(test_pidOrder[1])),
                                                 call(str(test_pidOrder[2])),
                                                 call(str(test_pidOrder[3])),
                                                 call("Average Process " + 
                                                      "Turnaround Time: "
                                                      + '%.2f' % test_avgTurnaround 
                                                      + "\n"),
                                                 call("Average Process Wait Time: " 
                                                      + '%.2f' 
                                                     % test_avgWait + "\n")])
         
    @patch("builtins.print")
    def test_shortestFirst(self, mock_print):
        test_completeTimes, test_sjfPids = sort.ShortestJobFirstSort(test_procs)
        test_avgTurnaround, test_taTimes = average.AverageTurnaround(
             test_completeTimes, test_arrivals)
        test_pidOrder = []

        for i in range(len(test_sjfPids)):
             test_pidOrder.append(str(test_sjfPids[i]) + "\n")

        test_avgWait = average.AverageWait(test_taTimes, test_bursts)
        batchSchedulingComparison.sortingAlgorithm("ShortestFirst", test_procs, 
                                                   test_arrivals, test_bursts)
        self.assertEqual(mock_print.mock_calls, [call("\nPID ORDER OF EXECUTION\n"),
                                                 call(str(test_pidOrder[0])),
                                                 call(str(test_pidOrder[1])),
                                                 call(str(test_pidOrder[2])),
                                                 call(str(test_pidOrder[3])),
                                                 call(str(test_pidOrder[4])),
                                                 call("Average Process " + 
                                                      "Turnaround Time: " +
                                                      '%.2f' % test_avgTurnaround 
                                                      + "\n"),
                                                 call("Average Process Wait Time: " 
                                                      + '%.2f' 
                                                     % test_avgWait + "\n")])

    @patch("builtins.print")
    def test_priority(self, mock_print):
        test_completeTimes, test_priorityPids = sort.PrioritySort(test_procs)
        test_avgTurnaround, test_taTimes = average.AverageTurnaround(
          test_completeTimes, test_arrivals)
        test_pidOrder = []

        for i in range(len(test_priorityPids)):
             test_pidOrder.append(str(test_priorityPids[i]) + "\n")

        test_avgWait = average.AverageWait(test_taTimes, test_bursts)
        batchSchedulingComparison.sortingAlgorithm("Priority", test_procs, 
                                                   test_arrivals, test_bursts)
        self.assertEqual(mock_print.mock_calls, [call("\nPID ORDER OF EXECUTION\n"),
                                                 call(str(test_pidOrder[0])),
                                                 call(str(test_pidOrder[1])),
                                                 call(str(test_pidOrder[2])),
                                                 call(str(test_pidOrder[3])),
                                                 call("Average Processes " + 
                                                      "Turnaround Time: " +
                                                      '%.2f' % test_avgTurnaround 
                                                      + "\n"),
                                                 call("Average Processes Wait Time: " 
                                                      + '%.2f' 
                                                     % test_avgWait + "\n")])

    @patch("builtins.print")    
    def test_incorrectInput(self, mock_print):
        batchSchedulingComparison.sortingAlgorithm("Test", test_procs, 
                                                   test_arrivals, test_bursts)
        self.assertEqual(mock_print.mock_calls, [call("Invalid process scheduling " + 
                                                      "algorithm entered." +
                                                      " Valid options are FCFS, " + 
                                                      "ShortestFirst, or Priority.")])
         
if __name__ == "__main__":
     unittest.main()