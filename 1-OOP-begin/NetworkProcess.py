# -*- coding: utf-8 -*-
"""
TODO: Implement a NetworkProcess class

Use EventHandler as a base class (see Sender/ Receiver)

In the constructor (__init__ function) take a sender instance 
and a receiver instance.as arguments

Implement the handleEvent method to get messages from the sender and
deliver each message to the receiver.

"""
from EventHandler import EventHandler  # Import base class


class NetworkProcess(EventHandler):  # Inherit from base class
    def __init__(self, sender, receiver):  # Take sender and receiver instances
        self.sender = sender
        self.receiver = receiver
        return

    def handleEvent(self):
        messageList = self.sender.retrieveMessages()  # Retrieve messages from sender
        for message in range(len(messageList)):  # Go through list
            self.receiver.deliverMessage(messageList[message])  # Deliver message to receiver
        return
