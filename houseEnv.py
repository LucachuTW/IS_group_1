import AbstractHouseEnv

class HouseEnv(AbstractHouseEnv.AbstractHouseEnv):
    def __init__(self) -> None:
        pass

    def addDrug(self, object, quantity):
        # @antonoterof
        model= self.getModel()
        if model.getOpenStatus(object)== False:
            return False
        else:
            return True
        
    def areAdjacent(self, object1, object2):
        model= self.getModel()
        if (model.getPositionOf(object1)==[0,0] and model.getPositionOf(object2)==[0,1]
             or  model.getPositionOf(object1)==[0,0] and model.getPositionOf(object2)==[1,0] 
             or model.getPositionOf(object1)==[0,1] and model.getPositionOf(object2)==[0,0]
             or model.getPositionOf(object1)==[1,0] and model.getPositionOf(object2)==[0,0]
             ):
            return True
        elif (model.getPositionOf(object1)==[0,0] and model.getPositionOf(object2)==[1,1]
              or model.getPositionOf(object1)==[0,0] and model.getPositionOf(object2)==[0,2]
              ):
            return False