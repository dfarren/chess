import networkx as nx
import pdb, traceback

class Graph(nx.DiGraph):
    
    def __init__(self, board, *args, **kwargs):
        super(Graph, self).__init__(*args, **kwargs)
        try:
            for i in range(len(board)):
                #rook
                if board[i][0].lower() == 'r':
                    #check horizontals
                    j = i+1
                    while j < (int(i/8)+1)*8:
                        if board[j] != "  ":
                            self.add_edge(board[i], board[j])
                            break
                        j += 1
                    j = i-1
                    while j >= int(i/8)*8:
                        if board[j] != "  ":
                            self.add_edge(board[i], board[j])
                            break
                        j -= 1    
                    
                    #check verticals
                    j = i+8
                    while j < 64:
                        if board[j] != "  ":
                            self.add_edge(board[i], board[j])
                            break
                        j += 8
                    j = i-8
                    while j >= 0:
                        if board[j] != "  ":
                            self.add_edge(board[i], board[j])
                            break
                        j -= 8
                #knight
                if board[i][0].lower() == 'n':
                    knightMoves = [15,17,6,10,-10,-6,-17,-15]
                    for j in [15,17,6,10,-10,-6,-17,-15]:

                        if i+j <= 15:
                            if knightMoves.count(-17) == 1:
                                knightMoves.remove(-17)
                            if knightMoves.count(-15) == 1:
                                knightMoves.remove(-15)
                        if i+j <= 7:
                            if knightMoves.count(-10) == 1:
                                knightMoves.remove(-10)
                            if knightMoves.count(-6) == 1:
                                knightMoves.remove(-6)
                        if i+j >= 48:
                            if knightMoves.count(15) == 1:
                                knightMoves.remove(15)
                            if knightMoves.count(17) == 1:
                                knightMoves.remove(17)
                        if i+j >= 56:
                            if knightMoves.count(6) == 1:
                                knightMoves.remove(6)
                            if knightMoves.count(10) == 1:
                                knightMoves.remove(10)
                        if i+j % 8 == 0 or i+j % 8 == 1:
                            if knightMoves.count(6) == 1:
                                knightMoves.remove(6)
                            if knightMoves.count(-10) == 1:
                                knightMoves.remove(-10)
                        if i+j % 8 == 0:
                            if knightMoves.count(15) == 1:
                                knightMoves.remove(15)
                            if knightMoves.count(-17) == 1:
                                knightMoves.remove(-17)
                        if i+j % 8 == 6 or i+j % 8 == 7:
                            if knightMoves.count(10) == 1:
                                knightMoves.remove(10)
                            if knightMoves.count(-6) == 1:
                                knightMoves.remove(-6)
                        if i+j % 8 == 7:
                            if knightMoves.count(17) == 1:
                                knightMoves.remove(17)
                            if knightMoves.count(-15) == 1:
                                knightMoves.remove(-15)
                        
                    for j in knightMoves:
                        if board[i+j] != "  ":
                            self.add_edge(board[i], board[i+j])
                
                #bishop
                if board[i][0].lower() == 'b':
                    j = i+9
                    while j < 64:
                        if board[j] != "  ":
                            self.add_edge(board[i], board[j])
                            break
                        j += 9
                    
                    j = i+7
                    while j < 64:
                        if board[j] != "  ":
                            self.add_edge(board[i], board[j])
                            break
                        j += 7
    
                    j = i-7
                    while j >= 0:
                        if board[j] != "  ":
                            self.add_edge(board[i], board[j])
                            break
                        j -= 7                     
                        
                    j = i-9
                    while j >= 0:
                        if board[j] != "  ":
                            self.add_edge(board[i], board[j])
                            break
                        j -= 9
                
                #queen
                if board[i][0].lower() == 'q':
                    #check horizontals
                    j = i+1
                    while j < (int(i/8)+1)*8:
                        if board[j] != "  ":
                            self.add_edge(board[i], board[j])
                            break
                        j += 1
                    j = i-1
                    while j >= int(i/8)*8:
                        if board[j] != "  ":
                            self.add_edge(board[i], board[j])
                            break
                        j -= 1    
                    
                    #check verticals
                    j = i+8
                    while j < 64:
                        if board[j] != "  ":
                            self.add_edge(board[i], board[j])
                            break
                        j += 8
                    j = i-8
                    while j >= 0:
                        if board[j] != "  ":
                            self.add_edge(board[i], board[j])
                            break
                        j -= 8    
                                        
                    #check diagonals
                    j = i+9
                    while j <= 63:
                        if board[j] != "  ":
                            self.add_edge(board[i], board[j])
                            break
                        j += 9
                    
                    j = i+7
                    while j <= 63:
                        if board[j] != "  ":
                            self.add_edge(board[i], board[j])
                            break
                        j += 7
    
                    j = i-7
                    while j >= 0:
                        if board[j] != "  ":
                            self.add_edge(board[i], board[j])
                            break
                        j -= 7                     
                        
                    j = i-9
                    while j >= 0:
                        if board[j] != "  ":
                            self.add_edge(board[i], board[j])
                            break
                        j -= 9
                        
                #king
                if board[i][0].lower() == 'k':
                    #check horizontals
                    if (i+1)%8 != 0:
                        if board[i+1] != "  ":
                            self.add_edge(board[i], board[i+1])
                    if i%8 != 0:
                        if board[i-1] != "  ":
                            self.add_edge(board[i], board[i-1])
                    #check verticals
                    if int(i/8) != 7:
                        if board[i+8] != "  ":
                            self.add_edge(board[i], board[i+8])    
                    if int(i/8) != 0:
                        if board[i-8] != "  ":
                            self.add_edge(board[i], board[i-8])  
                                        
                    #check diagonals
                    if (i+1)%8 != 0 and int(i/8) != 7:
                        if board[i+9] != "  ":
                            self.add_edge(board[i], board[i+9])
                    if i%8 != 0 and int(i/8) != 7:
                        if board[i+7] != "  ":
                            self.add_edge(board[i], board[i+7])
                    if (i+1)%8 != 0 and int(i/8) != 0:
                        if board[i-7] != "  ":
                            self.add_edge(board[i], board[i-7])    
                    if i%8 != 0 and int(i/8) != 0:
                        if board[i-9] != "  ":
                            self.add_edge(board[i], board[i-9])
                
                #pawn
                if board[i][0] == 'x':
                    if (i+1)%8 != 0 and int(i/8) != 7:
                        if board[i+9] != "  ":
                            self.add_edge(board[i], board[i+9])
                    if i%8 != 0 and int(i/8) != 7:
                        if board[i+7] != "  ":
                            self.add_edge(board[i], board[i+7])
                if board[i][0] == 'X':
                    if (i+1)%8 != 0 and int(i/8) != 0:
                        if board[i-7] != "  ":
                            self.add_edge(board[i], board[i-7])    
                    if i%8 != 0 and int(i/8) != 0:
                        if board[i-9] != "  ":
                            self.add_edge(board[i], board[i-9]) 
        except:
            traceback.print_exc()
            pdb.set_trace()                           
        
