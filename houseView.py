import AbstractHouseView
import software.GridWorldModel.GridWorldModel

class HouseView(AbstractHouseView.AbstractHouseView):
    def __init__(self):
        pass

    def draw(self):
        # @antonoterof
        # Modified by @SantiagoRR2004
        model = self.getModel()
        return model.getAttribute("grid")

    def drawAgent(self, object):
        # @antonoterof
        # Modified by @SantiagoRR2004
        model = self.getModel()
        return model.getAttribute(object)