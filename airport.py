
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
    	self.occupiedRunways = {}   # flight Number -> Runway Number
        self.emptyRunways = 0
    	self.waitingQueue = []
    	
    def addRunways(self,cnt):
    	for i in cnt:
            self.runways.append(Runway(i,False,Airplane(str(i)+str(i))))

class ControlCenter:

    def __init__(self):
    	self.airport = Airport.getAirport()
        
	def findRunway(self):
	    for runway in self.airport.runways 
	        if runway.available
                return runway

        return None
    
    def processRequest(self, airplane, reqType):
        if reqType == "landing":
            runway = self.findRunway()
            if runway is not None:
                airplane.landing(runway)
            else:
                self.waitingQueue.append(airplane)
        elif reqType == "depart":
            runway = airplane.depart()
            if len(self.waitingQueue)>0:
                airplane = self.airport.waitingQueue.pop(0)
                airplane.land(runway)
        
class Airplane:

    def __init__(self, flight_num, landed=True):
    	self.airport = Airport.getAirport()
    	self.flight_num = flight_num
    	self.landed = landed

    def landing(self,runway):
    	runway.occupy(self)
        self.airport.occupiedRunways[self.flight_num] = runway
        self.airport.emptyRunways -= 1
        self.landed = True
        
    def depart(self):
        runway = self.airport.occupiedRunways[self.flight_num]
        runway.clear()
        self.airport.occupiedRunways.pop(self.flight_num)
        self.airport.emptyRunways += 1
        airplane.landed = False

class Runway:

	def __init__(self, location, available=False, airplane=None):
    	self.location = location
    	self.available = available
    	self.airplane = airplane

    def occupy(self, airplane):
    	self.airplane = airplane
    	self.available = False

    def clear(self):
    	self.airplane = None
    	self.available = True