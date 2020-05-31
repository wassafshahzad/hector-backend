from evaluate import game_over_state

def _parse_board_to_key(board):
    return "".join(board)

def _get_key(node,hector):
    return hector.moves[_parse_board_to_key(node.board)]

def get_move(node,hector):
    score = -99
    index = None
    for x in _get_key(node,hector):
        if(x[1]>=score):
            index = x[2] 
            score = x[1]
    return index

def debug_moves_list(node,hector):
    move_list = _get_key(node,hector)
    print(move_list)




def check_game_state(game):
    state =  game_over_state(game)
    if(state == 0 ):
        return "Draw",True
    elif(abs(state) == 10 ):
        return "Winner is " + str(game.current),True
    else:
        return '_',False 
    