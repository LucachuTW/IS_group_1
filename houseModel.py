class HouseModel():
    def __init__(self):
        #@Ventupentu
        self._availableDrugs: int = 0

    def addDrug(self, quantity):
        #@Ventupentu
        self._availableDrugs += quantity

    def getDrug(self):
        #@Ventupentu
        return self._availableDrugs 