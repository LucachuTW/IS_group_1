import houseModel
import owner
import robot

if __name__ == "__main__":
    model = houseModel.HouseModel()
    controller = model.getController()
    viewer =  model.getView()

    owner1 = owner.Owner(controller,viewer)
    robot1 = robot.Robot(controller,viewer)
   