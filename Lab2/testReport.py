# -*- coding: utf-8 -*-
"""
Test helper function
"""

def testReport(test, testInfo):
    if test:
        print("PASS: " + testInfo)
    else:
        print("FAIL: " + testInfo)