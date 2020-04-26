#!/usr/bin/env python3

import os
from research import *
import unittest

log = r"C:\Users\Benjamin\Documents\111 Education\888 Coursera\AUT Google IT Automation with Python Professional Certificate\222 Using Python to Interact with the Operating System\proj_ticky\syslog.txt"
ef_csv = r"C:\Users\Benjamin\Documents\111 Education\888 Coursera\AUT Google IT Automation with Python Professional Certificate\222 Using Python to Interact with the Operating System\proj_ticky\error_freqs.csv"
us_csv = r"C:\Users\Benjamin\Documents\111 Education\888 Coursera\AUT Google IT Automation with Python Professional Certificate\222 Using Python to Interact with the Operating System\proj_ticky\usage_stats.csv"
output = {'test':0}

class test_research (unittest.TestCase):
    # error_freqs
    def test_ef_fnf (self):
        with self.assertRaises(FileNotFoundError):
            error_freqs(r"T:\his\file\does\not\exist.txt")
            error_freqs(True)
            error_freqs(2)
            error_freqs(3.14)
            error_freqs([test])
            error_freqs({"test":0})
    def test_ef_idx_true (self):
        expected = 2
        output = error_freqs(log)
        self.assertEqual(output["What the f*%^?"], expected)
    def test_ef_idx_false (self):
        output = error_freqs(log)
        with self.assertRaises(KeyError):
            output["This message should not exist"]
    
    # usage_stats
    def test_us_fnf (self):
        with self.assertRaises(FileNotFoundError):
            usage_stats(r"T:\his\file\does\not\exist.txt")
            usage_stats(True)
            usage_stats(2)
            usage_stats(3.14)
            usage_stats([test])
            usage_stats({"test":0})
    def test_us_idx_true (self):
        output = usage_stats(log)
        self.assertEqual(output["bbtruc"]["ERROR"], 1)
        self.assertEqual(output["bbtruc"]["INFO"], 1)
        self.assertEqual(output["arawr"]["ERROR"], 2)
        self.assertEqual(output["arawr"]["INFO"], 0)
    def test_us_idx_false (self):
        output = usage_stats(log)
        with self.assertRaises(KeyError):
            output["This message should not exist"]
            output["wreg_cas"]["This message should not exist"]
        
    # ef2csv
    def test_ef2csv_raise (self):
        self.assertIsNone(ef2csv(r"T:\his\file\does\not\exist.txt"))
    def test_ef2csv_exist (self):
        self.assertTrue(os.path.exists(ef_csv))
    def test_ef2csv_output (self):
        output = ['Error, Count\n', 'What the f*%^?, 2\n', 'Yo mama failed, 1\n']
        with open("error_freqs.csv", "r") as f:
            self.assertEqual(f.readlines(), output)
            
    # us2csv
    def test_us2csv_raise (self):
        self.assertIsNone(us2csv(r"T:\his\file\does\not\exist.txt"))
    def test_us2csv_exist (self):
        self.assertTrue(os.path.exists(us_csv))
    def test_us2csv_output (self):
        output = ['Error, Count\n', 'What the f*%^?, 2\n', 'Yo mama failed, 1\n']
        with open("usage_stats.csv", "r") as f:
            self.assertEqual(f.readlines(), output)
    
    
unittest.main()