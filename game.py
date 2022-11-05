# Global variables
BOARDWIDTH = 8

### Class of Chess Game ###
class Game:

    ## Classes of Piece ##
    class Piece:
        # Piece constructor
        def __init__(self, pos: list, owner: int):
            self.pos = pos      # position
            self.owner = owner  # owner
        
        # move a piece
        def move(newPos: list):
            # TODO
            pass
        
        # more functions
    
    # To be completed
    class King(Piece):
        pass

    class Queen(Piece):
        pass

    class Rook(Piece):
        pass

    class Bishop(Piece):
        pass

    class Knight(Piece):
        pass

    class Pawn(Piece):
        pass

    # constructor, starting a new game. 
    #   players: 2-element list: 1 - computer, 2 - human
    def __init__(self, players: list):
        self.roundCount = 0
        self.board = [[0 for i in range(BOARDWIDTH)] for i in range(BOARDWIDTH)]
        # TODO: 
        #   - decide type of elements in board
        #   - put the pieces
        self.players = players
        self.moves = []
    
    #   search for all possible moves for the player 
    def searchMoves(self):
        # TODO
        return 0
    
    #   print the board
    def __str__(self):
        out = ''
        for i in range(BOARDWIDTH-1, -1, -1):
            out += str(i+1) + ' ' + ' '.join([self.showPos(p) for p in self.board[i]]) + '\n'
        out += '  ' + ' '.join([chr(ord('a')+i) for i in range(BOARDWIDTH)]) + '\n'
        return out
    
    #   show a position
    def showPos(self, p:str):
        # TODO
        #   character representation of each piece
        if p == 0:
            return '-'

game = Game([1,2])
print(game)
