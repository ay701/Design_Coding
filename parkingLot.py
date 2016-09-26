# When parking is full, there is car wants to park?
# Use car plate ID as hash key, slot as value

class parkingLot:

    lot = None

    @staticmethod
    def getInstance():
        if parkingLot.lot is None:
            parkingLot.lot = parkingLot()

        return parkingLot.lot

    def __init__(self):
        self.smallslots = []
        self.mediumslots = []
        self.largeslots = []
        self.waitingQueue = []
        self.occupiedSlots = {}  # Plate Number -> Slot
        self.num_empty_slots = 0

    def addSlots(self,numOfslots,size):

    	for i in range(numOfslots):
            if size==1:
        	    self.smallslots.append(Slot(i,size))
            elif size==2:
        	    self.mediumslots.append(Slot(i,size))
            elif size==3:
        	    self.largeslots.append(Slot(i,size))

            self.num_empty_slots += 1

    def findEmptySlot(self,size):

    	if size==1:
	    	for ind, slot in enumerate(self.smallslots):
	            if slot.empty:
	                return ind
       	elif size==2:
       	    for ind, slot in enumerate(self.mediumslots):
                if slot.empty:
                    return ind
        elif size==3:
            for ind, slot in enumerate(self.largeslots):
                if slot.empty:
                    return ind

        return None

    def parkWaiting(self,slotIndex,size):

        for ind, vehicle in enumerate(self.waitingQueue):
            if vehicle.size==size:
                
                self.waitingQueue.pop(ind)

                if size==1:
                    parkingLot.lot.smallslots[slotIndex].vehicle = vehicle
                    parkingLot.lot.smallslots[slotIndex].empty = False
                elif size==2:
                    parkingLot.lot.mediumslots[slotIndex].vehicle = vehicle
                    parkingLot.lot.mediumslots[slotIndex].empty = False
                elif size==3:
                    parkingLot.lot.largeslots[slotIndex].vehicle = vehicle
                    parkingLot.lot.largeslots[slotIndex].empty = False
                
                print vehicle.plateNum + " parked from waiting queue to slot " + str(slotIndex) + "\n"
                self.num_empty_slots -= 1
                break

    def printSlots(self):
    	print "\nParking Info:\n--------"
    	
    	for slot in self.smallslots:
    		print slot.vehicle.plateNum if not slot.empty else slot
    	
    	for slot in self.mediumslots:
    		print slot.vehicle.plateNum if not slot.empty else slot

    	for slot in self.largeslots:
    		print slot.vehicle.plateNum if not slot.empty else slot

    	print "Total available slots: " + str(self.num_empty_slots)

    def printWaiting(self):
    	print "\nWaiting Queue:\n--------"
    	for car in self.waitingQueue:
    		print car.plateNum

class Slot:

	def __init__(self, id, size):
		self.id = id 
		self.size = size
		self.empty = True
		self.vehicle = None

class Vehicle:

    def __init__(self, size, plateNum=None):
    	self.size = size
    	self.plateNum = plateNum
    	self.lot = parkingLot.getInstance()
    	self.parked = False

    def setParked(self, parked=True):
    	self.parked = parked

    def park(self):
    	if self.parked:
    		print "Already parked."
    	else:
            slotIndex = self.lot.findEmptySlot(self.size)

            if slotIndex is None:
                self.lot.waitingQueue.append(self)
                print self.plateNum + " is added to waiting queue.\n"
            else:
                self.setParked()

            	if self.size==1:
    		        self.lot.smallslots[slotIndex].empty = False
    		        self.lot.smallslots[slotIndex].vehicle = self
                elif self.size==2:
                    self.lot.mediumslots[slotIndex].empty = False
                    self.lot.mediumslots[slotIndex].vehicle = self
                elif self.size==3:
                    self.lot.largeslots[slotIndex].empty = False
                    self.lot.largeslots[slotIndex].vehicle = self
                
                self.lot.occupiedSlots[self.plateNum] = slotIndex
                self.lot.num_empty_slots -= 1
                print self.plateNum + " parked at " + str(slotIndex) + "."

    def unpark(self):
    	if not self.parked:
    		print "Car " +self.plateNum+ " is not parked yet!"
    		exit()

        slotIndex = self.lot.occupiedSlots.pop(self.plateNum)

        if self.size==1:
        	self.lot.smallslots[slotIndex].vehicle = None
        	self.lot.smallslots[slotIndex].empty = True
        elif self.size==2:
        	self.lot.mediumslots[slotIndex].vehicle = None
        	self.lot.mediumslots[slotIndex].empty = True
        elif self.size==3:
        	self.lot.largeslots[slotIndex].vehicle = None
        	self.lot.largeslots[slotIndex].empty = True

        self.lot.parkWaiting(slotIndex, self.size)
        self.lot.num_empty_slots += 1
    	print self.plateNum + " left slot " + str(slotIndex)
    	self.setParked(False)

pl = parkingLot.getInstance()
pl.addSlots(5, 1)
pl.addSlots(5, 2)
pl.addSlots(5, 3)
pl.printSlots()

car1 = Vehicle(1,"Kitty")
car2 = Vehicle(1,"Nutty")
car3 = Vehicle(1,"Dutty")
car4 = Vehicle(1,"Zitty")
car5 = Vehicle(1,"Fitty")
car6 = Vehicle(1,"Xitty")

print "\n"

car1.park()
car2.park()
car3.park()
car4.park()
car5.park()
car6.park()

pl.printSlots()
pl.printWaiting()

car1.unpark()
# car1.unpark()
car2.unpark()
# car2.unpark()
# car3.unpark()
car4.unpark()
# car5.unpark()

pl.printSlots()


