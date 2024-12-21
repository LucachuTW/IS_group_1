#!/usr/bin/python
# -*- coding: UTF-8 -*-
import AbstractHouseModel
from typing import List


class AbstractHouseView(object):
    def __init__(self, aModel):
        self._model = model
        self._controler = controler
        self._unnamed_AbstractHouseModel_: AbstractHouseModel = None

    def setController(self, aControler):
        pass

    def getController(self, aSelf) -> Any:
        """Retrieve the controller associated with the current instance.

        Returns:
            Any: The controller object.

        Note:
            This method provides access to the controller assigned to the instance.
            Ensure that the controller has been properly set before calling this method.

        Contributors:
            - @SantiagoRR2004"""
        pass

    def setModel(self, aModel):
        pass

    def getModel(self, aSelf) -> Any:
        """Retrieve the model associated with the current instance.

        Returns:
            Any: The model object.

        Note:
            This method provides access to the model assigned to the instance.
            Ensure that the model has been properly set before calling this method.

        Contributors:
            - @SantiagoRR2004"""
        pass

    def __repr__(self, aSelf) -> str:
        """Return a string representation of the object suitable for debugging.

        Returns:
            str: A string representation of the object.

        Contributors:
            - @SantiagoRR2004
            - @antonvm2004"""
        pass

    def __init__(self, aSelf, aModel=Any):
        """Initialize the instance with the provided model.

        Args:
        - model (Any): The model to be associated with the instance.

        Returns:
            None

        Contributors:
            - @SantiagoRR2004"""
        pass

    def setController(self, aSelf, aControler=Any):
        """Set the controller for the object.

        This method allows assigning a controller object to facilitate
        communication and interaction with the current object.

        Args:
        - controller (Any): The controller object to be set.

        Returns:
            None

        Contributors:
        - @SantiagoRR2004"""
        pass

    def setModel(self, aSelf, aModel=Any):
        """Set the model for the object.

        This method allows assigning a model object to facilitate
        communication and interaction with the current object.

        Args:
        - model (Any): The model object to be set.

        Returns:
            None

        Contributors:
            - @SantiagoRR2004"""
        pass
