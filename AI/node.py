import copy


class Node:
    def __init__(self, board, player):
        self.board = board
        self.move = {
            'player': 'x',
            'hec': 'o'
        }
        self.current = player
        self.score=None
        self.agent={
            "player":max,
            "hec":min
        }
        

    def copy(self):
        cp = copy.deepcopy(self)
        return cp

    def play_turn(self, index):
        self.board[index] = self.move[self.current]
    
    def _toggle_turn(self):
        self.current = 'player' if self.current == 'hec' else 'hec'


if __name__ == '__main__':
    ##test code
    node = Node(['']*9,'player')
    node2 = node.copy()
    node.board[1]='X'
    print(node.current)

