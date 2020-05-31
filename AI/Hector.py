from .evaluate import game_over_state
from .node import Node


class Hector:

    def __init__(self, head):
        self.head = head
        self.tree = None
        self.moves = {}
    
    def find_optimal_move(self, node, index):
        node._toggle_turn()
        node.play_turn(index)
        game_state = game_over_state(node)
        if(game_state != -1):
            node.score = game_state
            return
        else:
            self.generate_move_tree(node)
            return

    def generate_move_tree(self, node):
        node_score = None
        for i in range(len(node.board)):
            if(node.board[i] == '+'):
                child_node = node.copy()
                self.find_optimal_move(child_node, i)
                self.save_move(node, child_node, i)
                node_score = self.get_parentnode_score(
                    node_score, child_node.score, node)
                del child_node
        node.score = node_score

    def get_parentnode_score(self, node_score, child_node_score, node):
        if(node_score == None):
            return child_node_score
        else:
            return node.agent[node.current](node_score, child_node_score)

    def save_move(self, node, child_node, index):
        if(not ''.join(node.board) in self.moves):
            self.moves[''.join(node.board)] = [
                [child_node.board, child_node.score, index]]
        self.moves[''.join(node.board)].append(
            [child_node.board, child_node.score, index])


if __name__ == "__main__":
    n = Node(['+']*9, 'player')
    n.board[0] = "x"
    n.board[8] = "o"
    n.play_turn(1)
    hec = Hector(n)
    hec.generate_move_tree(n)
    print(hec.moves)
