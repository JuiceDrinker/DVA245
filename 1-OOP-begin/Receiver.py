# -*- coding: utf-8 -*-
"""
Receiver class
"""

from EventHandler import EventHandler

class Receiver(EventHandler):
    def __init__(self):
        self._messages = []
        return
    def deliverMessage(self, message):
        self._messages.append(message)
    def handleEvent(self):
        deliveredMessages = self._messages
        self._messages = []
        for message in deliveredMessages:
            print("Received message: " + message)
        