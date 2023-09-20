#!/usr/bin/python3
import unittest
import sys
from io import StringIO
from console import HBNBCommand

class TestConsole(unittest.TestCase):

    def setUp(self):
        self.console = HBNBCommand()
        self.console.prompt = ""
        self.capt_out = StringIO()
        self.backup = sys.stdout

    def tearDown(self):
        self.console = None

    def test_create(self):
        '''
        Test that create works
        '''
        self.console.onecmd("create User")
        output = self.capt_out.getvalue().strip()
        self.assertTrue(isinstance(output, str))

    
    def test_show(self):
        '''
            Testing that show exists
        '''
        
        self.console.onecmd("create User")
        user_id = self.capt_out.getvalue()
        sys.stdout = self.backup
        self.capt_out.close()
        self.capt_out = StringIO()
        sys.stdout = self.capt_out
        self.console.onecmd("show User " + user_id)
        x = (self.capt_out.getvalue())
        sys.stdout = self.backup
        self.assertTrue(str is type(x))

    def test_show_class_name(self):
        '''
        Testing the error messages for class name missing.
        '''
        self.console.onecmd("create User")
        user_id = self.capt_out.getvalue()
        sys.stdout = self.backup
        self.capt_out.close()
        self.capt_out = StringIO()
        sys.stdout = self.capt_out
        self.console.onecmd("show")
        x = (self.capt_out.getvalue())
        sys.stdout = self.backup
        self.assertEqual("** class name missing **\n", x)

    def capture_output(self, func):
        captured_output = StringIO()
        sys.stdout = captured_output
        func()
        sys.stdout = sys.__stdout__
        return captured_output.getvalue()


if __name__ == "__main__":
    unittest.main()
