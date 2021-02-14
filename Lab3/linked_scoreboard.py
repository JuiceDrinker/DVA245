# Anna Friebe, developed for DVA245, based on material with the following
# copyright:
#
# Copyright 2013, Michael H. Goldwasser
#
# Developed for use with the book:
#
#    Data Structures and Algorithms in Python
#    Michael T. Goodrich, Roberto Tamassia, and Michael H. Goldwasser
#    John Wiley & Sons, 2013
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from testReport import testReport

class LinkedScoreboard:
    """Scoreboard implementation using a singly linked list for storage."""

    # -------------------------- nested _Node class --------------------------
    class _Node:
        """Lightweight, nonpublic class for storing a singly linked node."""
        __slots__ = '_playerName', '_score', '_next'         # streamline memory usage

        def __init__(self, playerName, score, next):      # initialize node's fields
            self._playerName = playerName       # name
            self._score = score               # score
            self._next = next                     # reference to next node

    # ------------------------------- stack methods -------------------------------
    def __init__(self, capacity):
        """Create an empty scoreboard."""
        self._capacity = capacity
        self._head = None
        self._size = 0
        # TODO: Implement the constructor.
        # Keep a reference to the first node in the list, the head.
        # Initially the scoreboard is empty and the head reference None.
        # Keep the capacity limit, to determine when to discard scores.
        # Possibly keep the current number of nodes in the list if you want to
        # avoid going through the list to count.

    def __len__(self):
        """Return the number of elements in the scoreboard."""
        return self._size

    def isEmpty(self):
        """Return True if the scoreboard is empty."""
        return self._size == 0
    
    def push(self, player, score):
            new_node = self._Node(player, score, self._head)
            self._head = new_node

    def handleCapacity(self):
        if self._size == self._capacity:
            curr = self._head
            prev = None
            while(True):
                if curr._next is not None:
                    curr = curr._next
                else:
                    prev._next = None
                    break;
        self._size = self._size + 1
    
    def insert(self, prev, player, score):
        new_node = self._Node(player, score, prev._next)
        prev._next = new_node
        self.handleCapacity()

    def addScore(self, playerName, score):
        """Add element with playerName and score at the right place of the scoreboard."""
        # TODO implement
        # The head node contains the node with the highest score.
        # The list consists of at most capacity number of nodes, in order of
        # decreasing scores.
        # When adding a score you need to:
        # - Find the correct position for the new score.
        # - If it is within the scoreboard capacity, create a new Node.
        # - Insert it at the right position (adjust next/ head references).
        # - If the scoreboard capacity is exceeded remove the reference to the
        # node that is pushed out
        # - Adjust the current number of nodes in the list if you keep it as a
        # member variable.
        curr = self._head
        prev = self._Node('Previous', 0, None)
        while(True):
            if self.isEmpty(): # If list is empty, add new Node as head
                new_node = self._Node(playerName, score, None)
                self._head = new_node
                self._size = self._size + 1
                break
            else: 
                if score > curr._score: 
                    if curr == self._head: #If at top of list push to list 
                        self.push(playerName, score)
                    elif curr._next is not None: # If not at end
                       self.insert(prev, playerName, score)
                    else: # if at End 
                        new_node = self._Node(playerName, score, None)
                        prev._next = new_node
                else: # Run loop again
                    prev = curr 
                    curr = curr._next

    def _getNode(self, position):
        """Helper function to get the node at a position in the list, to be used
        by playerName() and score(). Raise Exception if there is no node at position.
        position 1 refers to the first element in the list with the highest score."""
        # TODO: Implement
        # Walk through the nodes in the list until the correct position
        pointer = 1
        curr = self._head
        if pointer == position:
            return curr
        pointer = pointer + 1
        if(curr._next is None):
            Exception('No node at that position')
        curr = curr._next

    def playerName(self, position):
    #     """Returns the player name at a position in the list"""
        return self._getNode(position)._playerName

    #     """Returns the score at a position in the list"""

    def score(self, position):
        return self._getNode(position)._score

    def printHighScoreList(self):
    #     """Print the high score list
    #     """
    #     # TODO Print the contents of the scoreboard.
    #     # Start with printing a scoreboard header
    #     # Go through each node in the list, and print the position number,
    #     # player name and score.
    #     # Do not use the _getNode, playerName and score functions, because
    #     # it is more efficient to go through the nodes in the linked list once
        if not self.isEmpty():
            curr = self._head
            position = 1
            print('----- Scoreboard -----')
            while(curr is not None):
                print('Position: ' + position + ' Player: ' + curr._playerName + ' Score: ' + curr._score )
                curr = curr._next
                position = position + 1
        return
            

scoreboard = LinkedScoreboard(5)
testReport(scoreboard.isEmpty(), "Scoreboard empty")
scoreboard.printHighScoreList()
scoreboard.addScore("Donald Duck", 10)
scoreboard.addScore("Pluto", 12)
testReport(not scoreboard.isEmpty(), "Scoreboard not empty")
testReport(len(scoreboard) == 2, "Scoreboard len 2")
testReport(scoreboard.playerName(1) == "Pluto", "Scoreboard playerName 1")
testReport(scoreboard.score(1) == 12, "Scoreboard score 1")
testReport(scoreboard.playerName(2) ==
           "Donald Duck", "Scoreboard playerName 2")
testReport(scoreboard.score(2) == 10, "Scoreboard score 2")

scoreboard.printHighScoreList()
scoreboard.addScore("Mickey Mouse", 7)
scoreboard.addScore("Donald Duck", 19)
scoreboard.addScore("Goofy", 5)
scoreboard.addScore("Pluto", 9)
testReport(len(scoreboard) == 5, "Scoreboard len 5")
testReport(scoreboard.playerName(1) ==
           "Donald Duck", "Scoreboard playerName 1")
testReport(scoreboard.score(1) == 19, "Scoreboard score 1")
testReport(scoreboard.playerName(2) == "Pluto", "Scoreboard playerName 2")
testReport(scoreboard.score(2) == 12, "Scoreboard score 2")
testReport(scoreboard.playerName(3) ==
           "Donald Duck", "Scoreboard playerName 3")
testReport(scoreboard.score(3) == 10, "Scoreboard score 3")
testReport(scoreboard.playerName(4) == "Pluto", "Scoreboard playerName 4")
testReport(scoreboard.score(4) == 9, "Scoreboard score 4")
testReport(scoreboard.playerName(5) ==
           "Mickey Mouse", "Scoreboard playerName 5")
testReport(scoreboard.score(5) == 7, "Scoreboard score 5")

scoreboard.printHighScoreList()
scoreboard.addScore("Daisy Duck", 8)
testReport(scoreboard.playerName(5) == "Daisy Duck", "Scoreboard playerName 5")
testReport(scoreboard.score(5) == 8, "Scoreboard score 5")
testReport(len(scoreboard) == 5, "Scoreboard len 5")

scoreboard.printHighScoreList()
