#!/usr/bin/python
# -*- coding: UTF-8 -*-
from typing import List


class testController(object):
    def test_createsController(self, aSelf):
        """Test if the controller is created.

        This method checks if the controller is created.

        Contributors:
            - @SantiagoRR2004"""
        pass

    def test_checkAddDrug1(self, aSelf):
        """Test adding drugs to a cabinet when it is not open.

        This method tests the scenario where drugs are added to a cabinet when it is
        not open so it should return False.

        Contributors:
            - @SantiagoRR2004
            - @antonoterof"""
        pass

    def test_checkAddDrug2(self, aSelf):
        """Test adding drugs to a cabinet when it is open.

        This method tests the scenario where drugs are added to a
        cabinet when it is open. No problems arise so it returns True
        and the number doesn't change.

        Contributors:
            - @SantiagoRR2004
            - @antonoterof"""
        pass

    def test_checkAddDrug3(self, aSelf):
        """Test adding drugs to a cabinet to overfill it.

        This method tests the scenario where drugs are added
        to a cabinet to overfill it. It returns False and the
        value stays constant.

        Contributors:
            - @SantiagoRR2004
            - @antonoterof"""
        pass

    def test_checkAddDrug4(self, aSelf):
        """Test adding too many negative drugs to a cabinet.

        This method tests the scenario where negative drugs are added to a cabinet
        in excess. It returnd False and the value stays the same.

        Contributors:
            - @SantiagoRR2004
            - @antonoterof"""
        pass

    def test_checkAddDrug5(self, aSelf):
        """Test adding drugs to a robot.

        This method tests the scenario where drugs are added to a robot
        until it's maxed. This works because the robot can carry
        drugs. This is a special case because robot doesn't
        have the attribute open.

        Contributors:
            - @SantiagoRR2004
            - @antonoterof"""
        pass

    def test_checkAddDrug6(self, aSelf):
        """Test removing drugs from a cabinet.

        This method tests the scenario where drugs are removed from a cabinet
        until it has cero. It returns True and the value doesn't change.

        Contributors:
            - @SantiagoRR2004
            - @antonoterof"""
        pass

    def test_checkAddDrug7(self, aSelf):
        """Test adding strings to a cabinet.

        This method tests the scenario where a string is added to a cabinet.
        The result is False.

        Contributors:
            - @antonoterof"""
        pass

    def test_checkAddDrug8(self, aSelf):
        """Test adding strings to a agent (robot).

        This method tests the scenario where a string is added to an agent.

        Contributors:
            - @antonoterof"""
        pass

    def test_areAdjacent1(self, aSelf):
        """This method tests if two agents are next
        to each other in the house model when one is below
        at a distance of one unit.

        Contributors:
            - @SantiagoRR2004"""
        pass

    def test_areAdjacent2(self, aSelf):
        """Test if two agents are next to each other.

        This method tests if two agents are next to
        each other in the house model when one is to the right
        at a distance of one unit.

        Contributors:
            - @SantiagoRR2004"""
        pass

    def test_areAdjacent3(self, aSelf):
        """Test if two agents are next to each other.

        This method tests if two agents are next to
        each other in the house model when one is on top
        at a distance of one unit.

        Contributors:
            - @SantiagoRR2004"""
        pass

    def test_areAdjacent4(self, aSelf):
        """Test if two agents are next to each other.

        This method tests if two agents are next to
        each other in the house model when one is to the left
        at a distance of one unit.

        Contributors:
            - @SantiagoRR2004"""
        pass

    def test_areAdjacent5(self, aSelf):
        """This method tests if two agents are
        diagonally from each other. This means they are not
        next to each other.

        Contributors:
            - @SantiagoRR2004"""
        pass

    def test_areAdjacent6(self, aSelf):
        """This method tests if two agents are at a distance
        of 2 units horizontally. This means they are not
        next to each other.

        Contributors:
            - @SantiagoRR2004"""
        pass

    def test_areAdjacent7(self, aSelf):
        """This method tests if two agents are next
        to each other in the house model if one on
        the other side.

        Contributors:
            - @SantiagoRR2004"""
        pass

    def test_areAdjacent8(self, aSelf):
        """This method tests if two agents are next
        to each other in the house model if one on
        the other side by giving negative coordinates
        that appear to be one unit away.

        Contributors:
            - @SantiagoRR2004"""
        pass

    def test_areAdjacent9(self, aSelf):
        """This method tests if two agents are next
        to each other in the house model if both have negative
        coordinates but are next to each other.

        Contributors:
            - @SantiagoRR2004"""
        pass

    def test_areAdjacent10(self, aSelf):
        """This method tests if two agents are next
        to each other in the house model if both have negative
        coordinates but are next to each other.

        Contributors:
            - @SantiagoRR2004"""
        pass

    def test_transferDrugs1(self, aSelf):
        """This method tests the scenario where drugs are transferred from the cabinet to one agent.

        Contributors:
            - @SantiagoRR2004"""
        pass

    def test_transferDrugs2(self, aSelf):
        """This method tests the scenario where drugs are transferred from one agent to the cabinet.

        Contributors:
            - @SantiagoRR2004"""
        pass

    def test_transferDrugs3(self, aSelf):
        """This method tests the scenario where drugs are transferred from the cabinet to one agent.
        Fails because the motor can't be transferred because it can't move on its own.

        Contributors:
            - @SantiagoRR2004"""
        pass

    def test_transferDrugs4(self, aSelf):
        """This method tests the scenario where drugs are transferred from one agent to the cabinet.
        Fails because they aren't adjacent.

        Contributors:
            - @SantiagoRR2004"""
        pass

    def test_transferDrugs5(self, aSelf):
        """This method tests the scenario where drugs are transferred from the cabinet to one agent.
        Fails because it isn't enough space on the reciever.

        Contributors:
            - @SantiagoRR2004"""
        pass

    def test_transferDrugs6(self, aSelf):
        """This method tests the scenario where drugs are transferred from one agent to the cabinet.
        Fails because it isn't enough drugs on the giver.

        Contributors:
            - @SantiagoRR2004"""
        pass

    def test_transferDrugs7(self, aSelf):
        """This method tests the scenario where drugs are transferred from the cabinet to one agent.
        Fails because cabinet isn't open.

        Contributors:
            - @SantiagoRR2004"""
        pass

    def test_checkOpeneable1(self, aSelf):
        """It is ensure that the method returns a Boolean value.

        Contributors:
            - @SantiagoRR2004
            - @Ventupentu"""
        pass

    def test_checkOpeneable2(self, aSelf):
        """It is ensure that the method works correctly.

        Contributors:
            - @SantiagoRR2004
            - @Ventupentu"""
        pass

    def test_checkIfShareable1(self, aSelf):
        """It is ensure that the method works correctly.

        Contributors:
            - @SantiagoRR2004"""
        pass

    def test_checkIfShareable2(self, aSelf):
        """It is ensure that the method works correctly.
        The object can not share space because it is openable and not is open.

        Contributors:
            - @SantiagoRR2004"""
        pass

    def test_checkIfShareable3(self, aSelf):
        """It is ensure that the method works correctly.
        The object can share space because it is semisolid and not openable.

        Contributors:
            - @SantiagoRR2004"""
        pass

    def test_checkIfShareable4(self, aSelf):
        """It is ensure that the method works correctly.
        The object can not share space because it is not semisolid.

        Contributors:
            - @SantiagoRR2004"""
        pass

    def test_checkIfMovableTo1(self, aSelf):
        """It is ensure that the method works correctly.
        The agent can move to the position (0,0) because it is empty.

        Contributors:
            - @SantiagoRR2004"""
        pass

    def test_checkIfMovableTo2(self, aSelf):
        """It is ensure that the method works correctly.
        The agent cannot move to position (0,0) because a prime number is formed

        Contributors:
            - @SantiagoRR2004"""
        pass

    def test_checkIfMovableTo3(self, aSelf):
        """It is ensure that the method works correctly.
        The agent can move to position (0,0) because object is semisolid, openable and it is open.

        Contributors:
            - @SantiagoRR2004"""
        pass

    def test_checkIfMovableTo4(self, aSelf):
        """It is ensure that the method works correctly.
        The agent can move to position (0,0) because object is semisolid, and no openable .

        Contributors:
            - @SantiagoRR2004"""
        pass

    def test_checkIfMovableTo5(self, aSelf):
        """It is ensure that the method works correctly.
        The agent can not move to position (0,0) because object is not semisolid.

        Contributors:
            - @SantiagoRR2004"""
        pass

    def test_checkIfMovableTo6(self, aSelf):
        """It is ensure that the method works correctly.
        The agent can not move to position (0,0) because object is semisolid, openable and it is no open.

        Contributors:
            - @SantiagoRR2004"""
        pass

    def test_moveTo1(self, aSelf):
        """It is ensure that the method works correctly.
        The agent can move to position (1,0) without problems.

        Contributors:
            - @SantiagoRR2004"""
        pass

    def test_moveTo2(self, aSelf):
        """It is ensure that the method works correctly.
        The agent can move to position (1,0) because the object that is in that position is semisolid and no openable.

        Contributors:
            - @SantiagoRR2004"""
        pass

    def test_moveTo3(self, aSelf):
        """It is ensure that the method works correctly.
        The agent can move to position (0,1) without problems.

        Contributors:
            - @SantiagoRR2004"""
        pass

    def test_moveTo4(self, aSelf):
        """It is ensure that the method works correctly.
        The agent can move to position (0,0) without problems.

        Contributors:
            - @SantiagoRR2004"""
        pass

    def test_moveTo5(self, aSelf):
        """It is ensure that the method works correctly.
        The agent can be returned to position (0,0) without problems.

        Contributors:
            - @SantiagoRR2004"""
        pass

    def test_moveTo6(self, aSelf):
        """It is ensure that the method works correctly.
        The agent can not move diagonally.

        Contributors:
            - @SantiagoRR2004"""
        pass

    def test_moveTo7(self, aSelf):
        """It is ensure that the method works correctly.
        The agent can not move to far away.

        Contributors:
            - @SantiagoRR2004"""
        pass

    def test_moveTo8(self, aSelf):
        """It is ensure that the method works correctly.
        The agent can not move itself.

        Contributors:
            - @SantiagoRR2004"""
        pass

    def test_moveTo9(self, aSelf):
        """It is ensure that the method works correctly.
        The agent can not move to position that is occupied by 2 other objects.

        Contributors:
            - @SantiagoRR2004
            - @Ventupentu"""
        pass

    def test_moveTo10(self, aSelf):
        """It is ensure that the method works correctly.
        The agent can move the object without problems.

        Contributors:
            - @SantiagoRR2004"""
        pass

    def test_moveTo11(self, aSelf):
        """It is ensure that the method works correctly.
        The agent can not move the object because mover and moved need to be adjacent.

        Contributors:
            - @SantiagoRR2004"""
        pass

    def test_moveTo12(self, aSelf):
        pass

    def test_moveTo13(self, aSelf):
        pass

    def test_moveTo14(self, aSelf):
        pass

    def test_moveTo15(self, aSelf):
        pass

    def test_moveTo16(self, aSelf):
        pass

    def test_moveMultipleTimes(self, aSelf):
        pass
