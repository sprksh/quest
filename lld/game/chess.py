"""
Game of chess:
1. Piece: Definition, movement, methods
2. Board & cells
3. Players
4. Game Engine

"""
import enum

class Status(enum.Enum):
    StaleMate = "SM"
    TimeOut = "TO"
    Running = "R"
    Over = "O"

class PieceType(enum.Enum):
    Rook = "Rook"
    Pawn = "Pawn"
    King = "King"
    Queen = "Queen"
    Bishop = "Bishop"
    Knight = "Knight"

class BasePiece:

    def move(self):
        raise NotImplementedError


class Rook(PieceMixin):
    def __init__(self):
        self.piece_type = PieceType.Rook
        
    def movement_allowed(self, new_position):
        i, j = self.position
        ni, nj = new_position
        if (ni == i and nj != j) or (ni != i and nj == j):
            return True
        return False

class Knight(PieceMixin):
    def __init__(self):
        self.piece_type = PieceType.Knight

    def movement_allowed(self, new_position):
        i, j = self.position
        ni, nj = new_position
        if (ni-i == 1 and nj-j == 2) or (ni-i == 2 and nj-j == 1):
            return True
        return False

def Pawn(PieceMixin):
    pass
        

class Cell:
    def __init__(self, i=0, j=0):
        self.piece = None
        self.coordinates = (i, j)
        self.colour = (i+j)//2
    
    def __repr__(self):
        return "W" if self.colour else "B" + str(self.coordinates)

class Board:
    def __init__(self):
        self.cells = [[(i, j) for i in range(8)] for j in range(8)]

class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.moves = []
        self.status = Status.Running
        self.board = Board()

    def make_move(self, player, piece, to_cell):
        pass
    
    def undo(self):
        pass

    