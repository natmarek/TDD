import unittest
import main

class TestMain(unittest.TestCase):
    def setUp(self):
        print('about to do a function')

    def test_do_stuff(self):
        test_param=10
        result = main.do_stuff(test_param)
        self.assertEqual(result, 15)
    def test_do_stuff(unittest.TestCase):
        test_param = None
        result = main.do_stuff(test_param)
        self.assertEqual(result, 'please enter number')
    
    def tearDown(self):
        print('cleaning up')



unittest.main()