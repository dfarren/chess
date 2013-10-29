import networkx as nx
import pdb, traceback
from board import Board
from graph import Graph

game_header = ""
games_dict = {}
games_list = []
get_line = False
for line in open('IB1321.pgn'):
    if line[0] == '[':
        game_header+=line+"::"
    if line[:10] == '[EventDate':
        complete_header = game_header

    if line[:2] == '1.':
        get_line = True
        tmp_list = []
    elif line[:2] == '\r\n':
        if get_line == True:
            #save game without last element (the result, ex 1-0)
            games_dict[complete_header] = tmp_list[:len(tmp_list)-1] 
            #games_list.append(tmp_list)
        get_line = False
        game_header = ""
    
    if get_line == True:      
        tmp = line.split()
        #remove whitespace in the last move of the line
        tmp[len(tmp)-1] = tmp[len(tmp)-1].strip()
        #remove move number
        tmp = [e[len(e)-1] for e in [e.split(".") for e in tmp]]
        #remove empty element in cases where the end of line is the move number (ex 13.)
        tmp = filter(None, tmp)
        #remove the + sign
        tmp = [e.replace("+","") for e in tmp]
        
        tmp_list.extend(tmp)

my_graphs_dict = {}
game_nbr=0


try:
    for header, game in games_dict.iteritems():
        print(header)
        tmp_list = []
        my_board = Board()
        tmp_list.append(Graph(my_board.board))
        i=0
        for move in game:
            #if move[0]=="B": pdb.set_trace()
            print(i)
            print(move)
            my_board.move_piece(i, move)
                
            my_board.showScreen()
            #raw_input()
            tmp_list.append(Graph(my_board.board))
            i = (i+1) %2
        my_graphs_dict[game_nbr] = tmp_list
        game_nbr+=1
except:
    traceback.print_exc()
    pdb.set_trace()  

    