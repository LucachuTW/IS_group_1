import houseModel
import houseEnv
import houseView
from owner import Owner
from robot import Robot
from courier import Courier
import time


def createHouse():
    model = houseModel.HouseModel("environmentBackup.json")
    view = houseView.HouseView(model)
    control = houseEnv.HouseEnv(model)
    control.setView(view)
    owner = Owner(control, view)
    time.sleep(2)  # Need to have this for graphical interface to work
    robot = Robot(control, view)
    courier = Courier(control, view)


if __name__ == "__main__":
    createHouse()
