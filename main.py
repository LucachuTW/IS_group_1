import houseModel
import owner
import robot


def createHouse():
    model = houseModel.HouseModel()
    controller = model.getController()
    viewer = model.getView()
    owner1 = owner.Owner(controller, viewer)
    robot1 = robot.Robot(controller, viewer)
    return [model, controller, viewer, owner1, robot1]


if __name__ == "__main__":
    createHouse()
