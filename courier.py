import time
from typing import List, Tuple
from AbstractUser import AbstractUser
from Context import Context
from wrapper import Wrapper


class Courier(AbstractUser):
    requiredData = {
        "unique": {"type": bool, "default": True},
        "numberDrugs": {"type": int, "default": 999999999999999999999},
        "maxCapacity": {"type": int, "default": 50},
        "symbol": {"type": int, "default": 7},
        "openable": {"type": bool, "default": False},
        "semisolid": {"type": bool, "default": True},
        "moving": {
            "type": dict,
            "default": {"auto": True, "mover": True, "moved": True},
        },
    }
    def setup(self) -> None:
        """
        Sets up the courier's context, initializes data, and sets the position.

        Args:
            - None

        Returns:
            - None. This method does not return any value.

        Contributors:
            - @Ventupentu
        """
        self.setContext(Context(LeaveCourier, self))
        self.data = self.getView().drawAgent("courier")
        self.setPosition()

    def getThreads(self) -> List:
        """
        Returns a list of threads.

        Each thread represents a specific task or functionality.

        Returns:
            - List: A list of threads.

        Contributors:
            - @Ventupentu
        """
        return [
            self.changeState,
        ]
    

    def changeState(self) -> None:
        """
        Changes the state of the courier based on the current conditions.

        If the state of emergency is True, transitions the courier to the ComeCourier state.
        Otherwise, transitions the courier to the LeaveCourier state.

        Returns:
            - None. This method does not return any value.

        Contributors:
            - @Ventupentu
        """
        while self.exitNegativeFlag:
            if self.stateOfCourier():
                self.context.transition_to(ComeCourier)
            else:
                self.context.transition_to(LeaveCourier)

    def stateOfCourier(self) -> bool:
        """
        Checks if the cabinet has to be filled.

        Returns:
            - bool: True if cabinet has less than 3 drugs.

        Contributors:
            - @Ventupentu
        """
        return True
        



class ComeCourier(Wrapper, Courier):
    def main(self) -> None:
        self.fillUpCabinet()

    def fillUpCabinet(self) -> None:
        """
        Fills up the cabinet with drugs.

        Returns:
            - None. This method does not return any value.

        Contributors:
            - @Ventupentu
        """
        objX, objY = self.getView().findNearestPositionOfSomething(
            "cabinet", self.x, self.y
        )

        nearbyPositions = [
            [self.x, self.y],
            [self.x, self.y + 1],
            [self.x, self.y - 1],
            [self.x + 1, self.y],
            [self.x - 1, self.y],
        ]

        if [objX, objY] in nearbyPositions:
            self.getController().openSomething(
                "courier", element="cabinet", opX=self.x, opY=self.y, eX=objX, eY=objY
            )
            while self.getController().transferDrugs("courier", "courier", "cabinet", 1):
                pass
            self.getController().closeSomething(
                "courier", element="cabinet", opX=self.x, opY=self.y, eX=objX, eY=objY
            )

        else:
            nextX, nextY = self.nextPosition(self.x, self.y, objX, objY)
            if self.getController().moveTo("courier", "courier", nextX, nextY):
                self.x = nextX
                self.y = nextY
            else:
                self.getController().openSomething("courier", eX=nextX, eY=nextY)

class LeaveCourier(Wrapper,Courier):
    def main (self) -> None:
        self.LeaveCourier()
    
    def LeaveCourier(self) -> None:
        """
        courier leaves the house.(cell 0,11)

        Returns:
            - None. This method does not return any value.
        
        Contributors:
            - @Ventupentu
        """
        exit_position= [0,11]
        if exit_position is not None:
            exitX, exitY = exit_position
            nextX, nextY = self.nextPosition(self.x, self.y, exitX, exitY)
            if self.getController().moveTo("courier", "courier", nextX, nextY):
                self.x = nextX
                self.y = nextY
            else:
                self.getController().openSomething("courier", eX=nextX, eY=nextY)
    