# -*- coding: utf-8 -*-
"""
TODO: Implement an internet application program

Create instances of the Sender, Receiver and NetworkProcess classes

Create a loop, where the handleEvent functions of these instances are called
100 times 

"""

from Sender import Sender
from Receiver import Receiver
from NetworkProcess import NetworkProcess

if __name__ == "__main__":
    sender = Sender()
    receiver = Receiver()
    np = NetworkProcess(sender, receiver)
    for i in range(100):
      sender.handleEvent()
      receiver.handleEvent()
      np.handleEvent()
    