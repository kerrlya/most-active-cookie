"""Unit testing framework for most_active_cookie. I chose to incorporate unit testing instead of integrative testing since, 
as this assignment evolves, I may need to add additional functions that require testing."""
import unittest, subprocess
import os

def get_cmd_output(input_cmd:str):
    """Helper to test cases in TestActiveCookie. Inputs string, returns command line string output."""
    with subprocess.Popen(input_cmd, shell=True, stdout=subprocess.PIPE) as cmd:
        ostring =  cmd.stdout.read()
    return ostring.decode("utf-8")


class TestActiveCookie(unittest.TestCase):
    # given test cases in problem statement
    def test_originals(self):
        output = get_cmd_output("./most_active_cookie cookie_log.csv -d 2018-12-09")
        self.assertEqual(output, "AtY0laUfhglK3lC7\n") 
        output = get_cmd_output("./most_active_cookie cookie_log.csv -d 2018-12-08")
        self.assertEqual(output, "SAZuXPGUrfbcn5UA\n4sMM2LxV07bPJzwf\nfbcn5UAVanZf6UtG\n") 

    # custom 'base' and edge cases
    def test_empty(self):
        # empty cookie log
        output = get_cmd_output("./most_active_cookie testing_cookies/empty_log.csv -d 2018-12-08")
        self.assertEqual(output, "\n")

    def test_tiedcookies(self):
        # cookie log with only cookies that have equal frequencies for each day
        output = get_cmd_output("./most_active_cookie testing_cookies/tied_log.csv -d 2018-12-09")
        self.assertEqual(output, "AtY0laUfhglK3lC7\nfbcn5UAVanZf6UtG\n")

        output = get_cmd_output("./most_active_cookie testing_cookies/tied_log.csv -d 2018-12-08")
        self.assertEqual(output, "4sMM2LxV07bPJzwf\nfbcn5UAVanZf6UtG\n")

    def test_mostwrongdates(self):
        # cookie log where one cookie is more common if date is ignored
        output = get_cmd_output("./most_active_cookie testing_cookies/wrongdate_log.csv -d 2018-12-09")
        self.assertEqual(output, "AtY0laUfhglK3lC7\n")

    def test_allwrongdates(self):
        # cookie log where all dates do not match with input date
        output = get_cmd_output("./most_active_cookie testing_cookies/allwrongdate_log.csv -d 2018-12-08")
        self.assertEqual(output, "\n")
    
if __name__ == '__main__':
    unittest.main()