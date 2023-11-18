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
            model.addDrug(object, quantity)