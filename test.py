import main
import unittest

class TestCase(unittest.TestCase):

    def test_first_matrix(self):
        self.assertEqual(main.rotate_matrix([[1,2,3],
                                            [4,5,6],
                                             [7,8,9]]), 
        
        
        [[7,4,1],
        [8,5,2],
        [9,6,3]])

    def test_second_matrix(self):

        self.assertEqual(main.rotate_matrix([[10, 9, 2, 3],
                                            [4,5,8,7],
                                            [22,6,10,11],
                                            [3,44,8,5]]),

                                            
                                            [[3,22,4,10],
                                            [44,6,5,9],
                                            [8,10,8,2],
                                            [5,11,7,3]] )


    def test_third(self):

        self.assertEqual(main.rotate_matrix([[1,2],
                                            [3,4]]),


                                            [[3,1],
                                            [4,2]])
        


