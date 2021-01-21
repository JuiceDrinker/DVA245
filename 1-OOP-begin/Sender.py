# -*- coding: utf-8 -*-
"""
Sender class
TODO: Implement
- handleEvent (you can use the _createMessages helper function)
- retrieveMessages
Run senderTest and see that the tests pass
"""
from EventHandler import EventHandler
import random
import copy


class Sender(EventHandler):
    def __init__(self):
        self._messageN = 0
        self._messages = []
        self._maxMessagesInPeriod = 10
        return

    # non-public method
    def _createMessages(self):
        nMessages = random.randint(1, self._maxMessagesInPeriod)
        for i in range(nMessages):
            self._messageN += 1
            self._messages.append("message" + str(self._messageN))
        return

    # public methods
    def handleEvent(self):
        self._createMessages()
        return

    def retrieveMessages(self):
        msgList = copy.copy(self._messages)  # Shallow copy
        self._messages.clear()  # Clear list
        return msgList
