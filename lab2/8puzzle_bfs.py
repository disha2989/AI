def bfs(src,target):
   
    visited=[]
    visited.append(src)
    a = [src]
    count = 0
    while a:
        count += 1
        print(a[0],'\n')
        if a[0] == target:                             
            return count
        a += possible_moves(a[0],visited)                    
        a.pop(0)                                                                    
    return False
def possible_moves(state,visited_states): 
    # Find index of empty spot and assign it to b
    
    b = state.index(-1)  
    
    #'d' for down, 'u' for up, 'r' for right, 'l' for left - directions array
    d = []
                                    
    #Add all possible direction into directions array - Hint using if statements
    
    if b+3 in range(9):
        d.append('d')
    if b-3 in range(9):
        d.append('u')
    if b not in [0,3,6]:
        d.append('l')
    if b not in [2,5,8]:
        d.append('r')
    
    # If direction is possible then add state to move
    pos_moves = []
    
    # for all possible directions find the state if that move is played
    ### Jump to gen function to generate all possible moves in the given directions
    for move in d:
        pos_moves.append(gen(state,move,b))
        
    # return all possible moves only if the move not in visited_states
    return [move for move in pos_moves if move not in visited_states]




def gen(state, direction, blank_spot):
    temp = state.copy()                            
    
    # if move is to slide empty spot to the left and so on
    
    if direction=='d':
        a = temp[blank_spot+3]
        temp[blank_spot+3]=temp[blank_spot]
        temp[blank_spot]=a
    elif direction=='u':
        a = temp[blank_spot-3]
        temp[blank_spot-3]=temp[blank_spot]
        temp[blank_spot]=a
    elif direction=='l':
        a = temp[blank_spot-1]
        temp[blank_spot-1]=temp[blank_spot]
        temp[blank_spot]=a
    elif direction=='r':
        a = temp[blank_spot+1]
        temp[blank_spot+1]=temp[blank_spot]
        temp[blank_spot]=a
    
   
    return temp

#Test 1
src = [1,2,3,-1,4,5,6,7,8]
target = [1,2,3,4,5,-1,6,7,8]       
       


bfs(src, target)

# Test 2
src = [1,2,3,-1,4,5,6,7,8] 
target=[1,2,3,6,4,5,-1,7,8]



bfs(src, target)
