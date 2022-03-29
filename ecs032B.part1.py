class Package:
    def __init__(self, id):
        self.id = id
        self.address = ""
        self.office = ""
        self.ownerName = ""
        self.collected = False
        self.delivered = False


class Truck:
    def __init__(self, id, n, loc):
        self.id = id
        self.size = n
        self.location = loc
        self.idpackages = {}
        self.addrpacks = {}

    def collectPackage(self, pk):
        if self.size == len(self.idpackages):
            return
        else:
            if self.location == pk.office:
                self.idpackages[pk.id] = pk
                pk.collected = True
                if pk.address in self.addrpacks.keys():
                    self.addrpacks[pk.address][pk.id] = pk
                else:
                    self.addrpacks[pk.address] = {}
                    self.addrpacks[pk.address][pk.id] = pk

    def deliverOnePackage(self, pk):
        if pk.address == self.location:
            if pk.id in self.idpackages.keys():
                pk.delivered = True
                del self.idpackages[pk.id]
                del self.addrpacks[pk.address][pk.id]

    def deliverPackages(self):
        if self.location in self.addrpacks.keys():
            hold = {}
            hold.update(self.addrpacks[self.location])
            del self.addrpacks[self.location]
            for thing in hold.values():
                thing.delivered = True
                del self.idpackages[thing.id]

    def removePackage(self, pk):
        if pk.id in self.idpackages.keys():
            pk.office = self.location
            pk.collected = False
            del self.idpackages[pk.id]

    def driveTo(self, loc):
        self.location = loc

    def getPackagesIds(self):
        idList = []
        if self.idpackages != {}:
            for key in self.idpackages.keys():
                idList.append(key)
            return idList
        else:
            return idList
