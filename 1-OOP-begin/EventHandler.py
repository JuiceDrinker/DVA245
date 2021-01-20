# -*- coding: utf-8 -*-
"""
Base class for event handling
"""

class EventHandler:
    def handleEvent(self):
        raise NotImplementedError('must be implemented by subclass')
