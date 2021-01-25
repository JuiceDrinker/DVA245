# -*- coding: utf-8 -*-
"""
TODO: Implement a NetworkProcess class

Use EventHandler as a base class (see Sender/ Receiver)

In the constructor (__init__ function) take a sender instance 
and a receiver instance.as arguments

Implement the handleEvent method to get messages from the sender and
deliver each message to the receiver.

"""
from EventHandler import EventHandler


class NetworkProcess(EventHandler):
  def __init__(self, Sender, Reciever):
    self.sender = Sender
    self.receiver = Reciever
    return

  def handleEvent(self):
    messages = self.sender.retrieveMessages()
    for message in messages:
      self.receiver.deliverMessage(message)
