from random import choice
from board import Board, Space, Coordinate

#computer for mattock
class TreeNode:
    def __init__ (self, value):
        self.value = value
        self.children = []
        self.parents = []
    def add_child(self, child):
        self.children.append(child)


class oracle:

    count = 0

    def __init__(self):
        self.name = f"rando_{oracle.count}"
        oracle.count += 1

    def mine(self, board: Board, color: Space) -> Coordinate:
        mineable = board.mineable_by_player(color)
        return choice(tuple(mineable)) 
        #the two prior lines can be ignored this is from the previous randombot

    def move(self, board: Board, color: Space) -> tuple[Coordinate, Coordinate] | None:
        pieces = board.find_all(color)
        start = choice(tuple(pieces))
        ends = board.walkable_from_coord(start)
        if len(ends) == 0:
            return None
        return start, choice(tuple(ends))
        #the six prior lines can be ignored this is from the previous randombot

    def minimax(self, board: Board, color: Space):
        #ok here's the plan: We're gonna score each position based on the player's possible moves and the opponents possible moves.
        #this is just for mining because dealing with mining is harder.

        opposing_color = Space.BLUE if color == Space.RED else Space.RED

        # possible_mines = board.mineable_by_player(color) #all the possible places in the current board.
        # root = TreeNode(board.mineable_by_player(color) - board.mineable_by_player(opposing_color))

        # root.children = [x for x in possible_mines if True] #adding all possible mines into the children list


    def oracle_method(self, board: Board, color:Space)->int:
        """
        Evaluation function  that hopefully evaluates a position.
        Factors in play:
        We deemed its more important to make a complex eval function rather than just  base it on how many spaces
        the opponent has that way we can make the best move possible.
        Whether specific move can capture a piece/save one of ours.
        Possible moves for us
        Possible moves for opponent
        centralizing pieces without making them capturable (less importance)

         
        """
        opposing_color = Space.BLUE if color == Space.RED else Space.RED
        possible_mines = board.mineable_by_player(color) #all the possible places in the current board.
        opponent_possible_mines = board.mineable_by_player(opposing_color)
        mineability_score = possible_mines-opponent_possible_mines


        #hopefully this makes some sort of sense but essentially we find all of our miners in any specific position 
        #and if our miner is dead then it just returns 0 we don't want to kill our miners unless we have to.
        miners_safe = self.miner_dead(board, color)
        score = miners_safe*(mineability_score + ...) 
        return score 
    
    def miner_dead(self, board: Board, color: Space)->int:
        miner_locations = board.find_all(color)
        for miner in miner_locations:
            if board.is_miner_dead(miner):
                return 0
        return 1
    
    def are_miners_connected(self, board: Board, color: Space)-> bool:
        ...
        