import unittest
import puzzle

class PuzzleTests(unittest.TestCase):

    def testFirstFrequencyVisitedTwice(self):
        self.assertEquals(0,puzzle.get_first_frequency_reached_twice([1,-1,1,1]))

    def testGetFrequencies(self):
        self.assertEquals([0,1,2,3],list(puzzle.get_frequencies([1,1,1])))
        

if __name__ == "__main__":
    unittest.main()
    
