#!/usr/bin/python
# -*- coding: UTF-8 -*-
import destroyer
from typing import List


class testOwner(destroyer):
    def test_getContext(self, aSelf):
        """Test if the owner has a context

        Contributors:
            - @SantiagoRR2004"""
        pass

    def test_state(self, aSelf):
        """Test if the owner has a context

        Contributors:
            - @SantiagoRR2004"""
        pass

    def test_data(self, aSelf):
        """Test if the owner has a data

        Contributors:
            - @SantiagoRR2004"""
        pass

    def test_setup(self, aSelf):
        """Test that the owner has a setup method

        Contributors:
            - @SantiagoRR2004"""
        pass

    def test_getThreads(self, aSelf):
        """Test the getThreads method of the owner object

        This test checks if the getThreads method of the owner object returns a
        list with callable methods.

        Contributors:
            - @SantiagoRR2004"""
        pass

    def test_changePulse(self, aSelf):
        """Test the changePulse method of the owner object

        This test checks if the changePulse method of the owner object changes
        the pulse attribute of the owner's data

        Because it changes randomly it could be the same and fail the test

        Contributors:
            - @SantiagoRR2004"""
        pass

    def test_checkForDeath(self, aSelf):
        """Test the checkForDeath method of the owner object

        This test checks if the checkForDeath method of the owner object sets
        the health attribute of the owner's data to 100 when the health is 0.

        Contributors:
            - @SantiagoRR2004"""
        pass

    def test_stateOfEmergency(self, aSelf):
        """Test the stateOfEmergency method of the owner object

        This test checks if the stateOfEmergency method of the owner object returns
        True when the health attribute of the owner's data is less than or equal to 50
        and false when it is more than 100.

        Contributors:
            - @SantiagoRR2004"""
        pass
