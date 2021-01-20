# -*- coding: utf-8 -*-
"""
Test of the Sender class
"""
from Sender import Sender
from testReport import testReport

sender = Sender()
messages = sender.retrieveMessages()
testReport( len(messages) == 0, "Zero messages after construction")
sender.handleEvent()
messages = sender.retrieveMessages()
testReport( len(messages) > 0 , "More than zero messages after message creation")
messages = sender.retrieveMessages()
testReport(len(messages) == 0, "Zero messages after retrieval")
