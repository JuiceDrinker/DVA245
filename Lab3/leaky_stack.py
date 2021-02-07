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
#


from testReport import testReport


class LeakyStack:
    """LIFO Leaky Stack implementation using a Python list as underlying storage."""

    def __init__(self, capacity):
        """Create an empty stack."""
        self._capacity = capacity
        self._stack = [] * self._capacity

    def __len__(self):
        """Return the number of elements on the stack."""
        return len(self._stack)

    def isEmpty(self):
        """Return True if the stack is empty."""
        return len(self._stack) == 0  # True if equal to zero

    def top(self):
        """Return (but do not remove) the element at the top of the stack. Raise Exception if the stack is empty."""
        if self.isEmpty():
            raise Empty('No elements in stack.')
        return self._stack[-1]  # Return last element

    def pop(self):
        """Remove and return the element at the top of the stack. Raise Exception if the stack is empty."""
        if self.isEmpty():
            raise Empty('No elements in stack.')
        return self._stack.pop()  # Return top element on stack

    def push(self, e):
        """Add an element onto the stack."""
        if len(self._stack) == self._capacity:  # If nr of elements is equal to capacity (full)
            self._stack = self._stack[1:]  # Shift all elements one step to the left and deleting oldest element
        self._stack.append(e)  # Always append


if __name__ == '__main__':
    S = LeakyStack(10)  # contents: [ ]
    testReport(S.isEmpty(), "LeakyStack is_empty True")
    S.push(5)  # contents: [5]
    S.push(3)  # contents: [5, 3]
    testReport(not S.isEmpty(), "LeakyStack is_empty False")
    testReport(len(S) == 2, "LeakyStack len 2")
    testReport(S.pop() == 3, "LeakyStack pop 3")
    testReport(S.pop() == 5, "LeakyStack pop 5")
    S.push(7)  # contents: [7]
    S.push(9)  # contents: [7, 9]
    testReport(S.top() == 9, "LeakyStack top 9")
    S.push(4)  # contents: [7, 9, 4]
    testReport(len(S) == 3, "LeakyStack len 3")
    testReport(S.pop() == 4, "LeakyStack pop 4")

    S.push(6)  # contents: [7, 9, 6]
    S.push(8)  # contents: [7, 9, 6, 8]
    S.push(3)  # contents: [7, 9, 6, 8, 3]
    S.push(4)  # contents: [7, 9, 6, 8, 3, 4]
    S.push(5)  # contents: [7, 9, 6, 8, 3, 4, 5]
    S.push(1)  # contents: [7, 9, 6, 8, 3, 4, 5, 1]
    S.push(2)  # contents: [7, 9, 6, 8, 3, 4, 5, 1, 2]
    S.push(7)  # contents: [7, 9, 6, 8, 3, 4, 5, 1, 2, 7]
    S.push(8)  # contents: [9, 6, 8, 3, 4, 5, 1, 2, 7, 8]; 7 leaked
    testReport(S.pop() == 8, "LeakyStack pop 8")
    testReport(S.pop() == 7, "LeakyStack pop 7")
    testReport(len(S) == 8, "LeakyStack len 8")
    testReport(S.pop() == 2, "LeakyStack pop 2")
    testReport(S.pop() == 1, "LeakyStack pop 1")
    testReport(S.pop() == 5, "LeakyStack pop 5")
    testReport(S.pop() == 4, "LeakyStack pop 4")
    testReport(S.pop() == 3, "LeakyStack pop 3")
    testReport(S.pop() == 8, "LeakyStack pop 8")
    testReport(S.pop() == 6, "LeakyStack pop 6")
    testReport(S.pop() == 9, "LeakyStack pop 9")
    testReport(S.isEmpty(), "LeakyStack is_empty True")
