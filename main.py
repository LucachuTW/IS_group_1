import houseModel
import houseEnv
import houseView
from owner import Owner
from robot import Robot


def createHouse():
    model = houseModel.HouseModel("environmentBackup.json")
    view = houseView.HouseView(model)
    control = houseEnv.HouseEnv(model)
    control.setView(view)
    owner = Owner(control, view)
    robot = Robot(control, view)


if __name__ == "__main__":
    createHouse()
