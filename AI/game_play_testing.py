#for testing purposes
#You can play hector on the terminal!  XD


from node import Node
from Hector import Hector
from helpers import get_move, check_game_state

def print_game(node):
    print(game.board[:3])
    print(game.board[3:6])
    print(game.board[6:])


if __name__=="__main__":
    game = Node(['+']*9,'player')
    hector = Hector(game)
    while(True):
        print_game(game)
        x = int(input("Enter your choice 1-9 \n"))
        game.play_turn(x)
        message,state = check_game_state(game)
        if(state):
            print(message)
            break
        if(not bool(hector.moves)):
            hector.generate_move_tree(game)
        index  = get_move(game,hector)
        game._toggle_turn()
        game.play_turn(index)
       
        message,state = check_game_state(game)
        
        if(state):
            print(message)
            break
        game._toggle_turn()
