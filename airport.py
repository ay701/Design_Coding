
class Airport:

	airport = None
    
    # singleton
    @staticmethod
    def getAirport():
    	if Airport.airport is None:
    		Airport.airport = Airport()

    	return Airport.airport

    def __init__(self):
    	self.controlCenter = ControlCenter()
    	self.runways = []
    	
    def addRunways(self,cnt):
    	for i in cnt:
    		self.runways.append(Runway(i,False,Airplane(str(i)+str(i))))

class ControlCenter:

    def __init__(self):
    	self.airport = Airport.getAirport()
    	self.occupiedRunways = {}   # flight Number -> Runway Number
        self.emptyRunways = 0
        self.waitingQueue = []
        
	def findRunway(self):
	    for runway in self.airport.runways 
		    if runway.available
		        return runway

		return None
    
    def depart(self, airplane):

        location = self.occupiedRunways[airplane.flight_num]
    	self.airport.runways[location].leave()
    	
    	self.occupiedRunways.pop(airplane.flight_num)
        airplane.landed = False
        self.emptyRunways += 1

        if len(self.waitingQueue)>0:
            self.land(self.waitingQueue.pop(0))

    def land(self, airplane):

        runway = self.findRunway()
        if runway is not None:
        	runway.occupy(airplane)
        	self.occupiedRunways[airplane.flight_num] = runway.location
        	airplane.landed = True
            self.emptyRunways -= 1
        else:
        	self.waitingQueue.append()

class Airplane:

    def __init__(self, flight_num, landed=True):
    	self.airport = Airport.getAirport()
    	self.flight_num = flight_num
    	self.landed = landed

class Runway:

	def __init__(self, location, available=False, airplane=None):
    	self.location = location
    	self.available = available
    	self.airplane = airplane

    def occupy(self, airplane):
    	self.airplane = airplane
    	self.available = False

    def leave(self):
    	self.airplane = None
    	self.available = True