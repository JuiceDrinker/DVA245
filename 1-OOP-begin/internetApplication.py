# -*- coding: utf-8 -*-
"""
TODO: Implement an internet application program

Create instances of the Sender, Receiver and NetworkProcess classes

Create a loop, where the handleEvent functions of these instances are called
100 times 

"""
# Import necessary classes

from Sender import Sender
from Receiver import Receiver
from NetworkProcess import NetworkProcess

# Create instances
sender = Sender()
receiver = Receiver()
network = NetworkProcess(sender, receiver)


# Loop function to display retrieved messages
def loop():
    for i in range(100):
        sender.handleEvent()
        receiver.handleEvent()
        network.handleEvent()


# Display
print('\n         - Internet Application -\n')
input('Press enter to loop process one hundred times.\n')
loop()  # Call loop function
print('\nAll messages displayed.')
