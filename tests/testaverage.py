import src.batchSchedulingComparison.average as average
import unittest

class TestAverage(unittest.TestCase):
    def test_avgTurnaround(self):
        test_completionTimes = [10, 20, 30, 40]
        test_arrivalTimes = [1, 2, 3, 4]
        
        test_turnaroundTimes = []

        for i in range(len(test_completionTimes)):
            test_turnaroundTimes.append(test_completionTimes[i] - test_arrivalTimes[i])

        test_avgTurnaround = sum(test_turnaroundTimes) / len(test_completionTimes)    

        test_avgResult, test_timesResult = average.AverageTurnaround(
                            test_completionTimes, test_arrivalTimes)

        self.assertEqual(test_avgTurnaround, test_avgResult)
        self.assertEqual(test_turnaroundTimes, test_timesResult)

    def test_avgWait(self):
        test_turnaroundTimes = [5, 10, 15, 20]
        test_burstTimes = [2, 4, 6, 8]

        test_waitTimes = []
        
        for i in range(len(test_turnaroundTimes)):
            test_waitTimes.append(test_turnaroundTimes[i] - test_burstTimes[i])

        test_avgWait = sum(test_waitTimes) / len(test_turnaroundTimes)

        test_waitResult = average.AverageWait(test_turnaroundTimes, test_burstTimes)

        self.assertEqual(test_avgWait, test_waitResult)

if __name__ == "__main__":
    unittest.main()