import unittest
#import src.inListener as inListener
import inListener

class TestListener(unittest.TestCase):

    def test_breakdown(self):
        
        test_phrases = ["What is the time",
                        "What is 1 + 1",
                        "Set an timer at 3 to pickup package"]

        
        breakdownResults = []
        for i in test_phrases: breakdownResults.append(None)
        
        def getOutput(ind):
            out = inListener.breakdown(test_phrases[ind])
            print (out)
            return True

        message = "The breakdown test has failed. Test Number: "
        self.assertIsNotNone(getOutput(0), message + str(0))

        