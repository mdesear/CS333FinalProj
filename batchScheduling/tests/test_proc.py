from batchScheduling.src import proc
import unittest

class TestProc(unittest.TestCase):
    def test_pid(self):
        test_proc = proc.Proc(1, 0, 0, 0)
        self.assertEqual(test_proc.getPid(), 1)
    
    def test_arrival(self):
        test_proc = proc.Proc(0, 1, 0, 0)
        self.assertEqual(test_proc.getArrival(), 1)
    
    def test_burst(self):
        test_proc = proc.Proc(0, 0, 1, 0)
        self.assertEqual(test_proc.getBurst(), 1)
    
    def test_priority(self):
        test_proc = proc.Proc(0, 0, 0, 1)
        self.assertEqual(test_proc.getPriority(), 1)

if __name__ == "__main__":
    unittest.main()