def game_over_state(node):
    state = -1
    won = _check_winning(node)
    if(node.current=='hec' and won):
        state = 10
    elif(node.current =='player' and won):
        state = -10
    elif("+" not in node.board and not won):
        state = 0
    return state


def _check_winning(node):
    won =_check_all_rows(node) or _check_all_cols(node) or _check_all_diags(node)
    return won

def _check_all_rows(node):
    return ( node.board[:3].count(node.board[:3][0]) == 3 and 
    node.board[:3][0] != "+" ) or (node.board[3:6].count(node.board[3:6][0]) == 3 and 
    node.board[3:6][0] != "+" ) or (node.board[6:].count(node.board[6:][0]) == 3 and 
    node.board[6:][0] !="+") 

def _check_all_cols(node):
    return _check_cols(node,0) or _check_cols(node,2) or _check_cols(node,1)

def _check_cols(node,i):
    return (node.board[i] == node.board[i+3] and node.board[i+6] == node.board[3+i]) and node.board[i] != "+"

def _check_all_diags(node):
    return _check_diags(node,0) or _check_diags(node,2)

def _check_diags(node,diag):
    return  (node.board[0+diag] == node.board[4]  and node.board[8-diag] == node.board[4]) and node.board[4]!="+"
