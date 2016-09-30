# Chess Game - 8x8 size board
# For each player, there are 8 pawns, 1 king, 1 queen, 2 bishops, 2 knights, 2 Rook

class Game:

    board = None
	player1, player2 = None

	def __init__(self):
		self.board = Board()
    
    def startGame(self):
    	enterPlayer(Player("Computer"))
    	enterPlayer(Player("Human"))

        while True:
        	processTurn(player1)
        	if board.getWin():
        		break

        	processTurn(player2)
        	if board.getWin():
        		break

    def enterPlayer(self, player):
    	board.initialize(player)

    def processTurn(self, player):
        executeMove(player)

class Board:

	squares = []
	win = False

	def executeMove(player):
	def getWin():

class Player:

	pieces = []
	commands = []
    color = None

    def __init__(self, color):
    	self.color = color
    	self.initializePieces()

    def initializePieces(self):
    	# populate pieces list by color
    	pieces.append() 
    	...

# abstract class
class Piece:

	available = True
	color = None
	x, y = -1, -1

    # this method is for overriding
    def isValid(board, f_x, f_y, t_x, t_y):
    def isAvailable():
    def setAvailable(status):

class Spot:

	x, y = -1
	piece = None

	def occupySpot(piece):
    def releaseSpot():
    def isOccupied():
    def getPiece():

class Command:

	piece = None
	f_x, f_y, t_x, t_y = -1

