import unittest
from unittest.mock import patch, mock_open
import testfunc
import os

class TestMock(unittest.TestCase):
    def setUp(self) -> None:
        self.phrase = "Greetings"

    # def test_setup(self):
    #     self.assertEqual(self.phrase, "Greetings")
        
    # def test_calc(self):
    #     self.assertEqual(4+4, 8)

    # @patch("testfunc.getName")
    # def test_get_name(self, mock_getName):
    #     mock_getName.return_value = 'Bob'
    #     result = testfunc.getName('Peter')
    #     self.assertEqual('Bob', result)

    # @patch("testfunc.getName")
    # def test_get_name(self, mock_getName):
    #     mock_getName.return_value = 'Peter'
    #     result = mock_getName('Peter')
    #     # print("Data print:", result)
    #     self.assertEqual('Peter', result)

    # @patch("testfunc.getName")
    # def test_modify_getName_sayHello(self, mock_get_name):
    #     mock_get_name.return_value = "Mike"
    #     testfunc.sayHello("Peter")

    # @patch('testfunc.sayHello')
    # def test_error_say_hello(self, mock_say_hello):
    #     mock_say_hello.side_effect = FileNotFoundError('Broke')
    #     with self.assertRaises((ArithmeticError, FileNotFoundError)) as cm:
    #         mock_say_hello("peter")
    #         print((cm.exception.message))

    
    # @patch('testfunc.double_read')
    # @patch('testfunc.read_file')
    # @patch('builtins.open', new_callable=mock_open, read_data="data")
    # def test_mock_reads(self, mock_open, mock_read):
    #     # handle1 = MagicMock()
    #     mock_read.side_effect = ['data1', 'data2']
    #     # handle1.return_value=['something1']
    #     # handle2 = MagicMock()
    #     # handle2.return_value=['something2']
    #     mock_open.side_effect = ['data1', 'data2']
    #     print(open('file1'))
    #     testfunc.double_read('list.txt', 'list2.txt')

    # @patch('testfunc.read_file')
    # def test_assert_read(self, mock_read):
    #     testfunc.read_file('list.txt')
    #     mock_read.assert_called_with('list.txt')

    @patch('testfunc.print_stuff')
    def test_effects_print(self, mock_prints):
        mock_prints.side_effect = ['ad1', 'ad2']
        result = testfunc.print_stuff
        print(testfunc.print_stuff)
        print(testfunc.print_stuff)

    # @patch("testfunc.side_feed")
    # def test_side_print(self, mock_side_feed):
    #     mock_side_feed.return_value = 'abc'
    #     result = testfunc.side_feed('hi')


    