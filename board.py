import pdb, traceback

class Board:
    
    def __init__(self):
    
        self.board = ["r1", "n1", "b1", "q ", "k ", "b2", "n2", "r2", "x1", "x2", "x3", "x4", "x5", "x6", "x7", "x8", "  ", "  ",
                      "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ",
                      "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "X8", "X7", "X6", "X5", "X4", "X3",
                      "X2", "X1", "R2", "N2", "B2", "Q ", "K ", "B1", "N1", "R1"]
    
    
    # translates a letter-number coordinate such as e4 to a position on the board, eg 28
    def coordinate(self, letter, number,notation):
        location = (ord(notation[letter]) - 97) + 8 * (int(notation[number]) - 1)
        return location
       
    def get_pawn_move(self,player,notation):
        #origin =-1
        if notation[1] == "x":
            destination = self.coordinate(2,3,notation)
            if player == 0:
                origin = self.coordinate(0,3,notation) - 8
            if player == 1:
                origin = self.coordinate(0,3,notation) + 8
        else:
            if player == 0:
                destination = self.coordinate(0,1,notation)
                if self.board[destination - 8][0] == "x":
                    origin = destination - 8
                elif self.board[destination - 16][0] == "x":
                    origin = destination - 16
            if player == 1:
                destination = self.coordinate(0,1,notation)
                if self.board[destination + 8][0] == "X":
                    origin = destination + 8
                elif self.board[destination + 16][0] == "X":
                    origin = destination + 16   
                                          
        return origin, destination
    
    def get_bishop_move(self,player,notation):
        #origin =-1
        if notation[1] == "x":
            destination = self.coordinate(2,3,notation)
        else:
            destination = self.coordinate(1,2,notation)
        if player == 0:  
            j = destination+9
            while j < 64:
                if j in [16,24,32,40,48,56,64]:
                    break
                if self.board[j][0] == "b":
                    origin = j
                    return origin, destination
                j += 9
            
            j = destination+7
            while j < 64:
                if j in [7,15,23,31,39,47,55,63]:
                    break
                if self.board[j][0] == "b":
                    origin = j
                    return origin, destination
                j += 7

            j = destination-7
            while j >= 0:
                if j in [8,16,24,32,40,48,56]:
                    break
                if self.board[j][0] == "b":
                    origin = j
                    return origin, destination
                j -= 7                     
                
            j = destination-9
            while j >= 0:
                if j in [-1,7,15,23,31,39,47,55]:
                    break
                if self.board[j][0] == "b":
                    origin = j
                    return origin, destination
                j -= 9       
                
        if player == 1:
            j = destination+9
            while j < 64:
                if j in [16,24,32,40,48,56,64]:
                    break
                if self.board[j][0] == "B":
                    origin = j
                    return origin, destination
                j += 9
            
            j = destination+7
            while j < 64:
                if j in [7,15,23,31,39,47,55,63]:
                    break
                if self.board[j][0] == "B":
                    origin = j
                    return origin, destination
                j += 7

            j = destination-7
            while j >= 0:
                if j in [8,16,24,32,40,48,56]:
                    break
                if self.board[j][0] == "B":
                    origin = j
                    return origin, destination
                j -= 7                     
                
            j = destination-9
            while j >= 0:
                if j in [-1,7,15,23,31,39,47,55]:
                    break
                if self.board[j][0] == "B":
                    origin = j
                    return origin, destination
                j -= 9  
    
    def get_queen_move(self, player, notation):
        destination = self.coordinate(len(notation)-2,len(notation)-1,notation)
#         if notation[1] == "x":
#             destination = self.coordinate(2,3,notation)
#         else:
#             destination = self.coordinate(1,2,notation)
            
        if player == 0:
            for i in range(64):
                if self.board[i][0] == "q":
                    origin = i
        if player == 1:                
            for i in range(64):
                if self.board[i][0] == "Q":
                    origin = i
        return origin, destination
    
    def get_king_move(self, player, notation):
        #origin =-1
        if notation[1] == "x":
            destination = self.coordinate(2,3,notation)
        else:
            destination = self.coordinate(1,2,notation)
        if player == 0:
            for i in range(64):
                if self.board[i][0] == "k":
                    origin = i
        if player == 1:
            for i in range(64):
                if self.board[i][0] == "K":
                    origin = i
        return origin, destination
    
    def get_knight_move(self,player,notation):
        knightMoves = [15,17,6,10,-10,-6,-17,-15]
        destination = self.coordinate(len(notation)-2, len(notation) - 1,notation)
        if player == 0:
            if len(notation) > 3 and notation[1] != "x":        
                if notation[1].isalpha() == True:
                    for e in knightMoves:
                        if destination+e >= 0 and destination+e < 64 and self.board[destination+e][0] == 'n' and destination+e in [(ord(notation[1]) - 97)+8*k for k in range(7)]:
                            origin = destination+e
                            return origin, destination
                else:
                    for e in knightMoves:
                        if destination+e >= 0 and destination+e < 64 and self.board[destination+e][0] == 'n' and destination+e in [8*(int(notation[1])-1)+k for k in range(7)]:
                            origin = destination+e
                            return origin, destination
            else:
                for e in knightMoves:
                    if destination+e >= 0 and destination+e < 64 and self.board[destination+e][0] == 'n':
                        origin = destination+e
                        return origin, destination          
  
        if player == 1:
            if len(notation) > 3 and notation[1] != "x":        
                if notation[1].isalpha() == True:
                    for e in knightMoves:
                        if destination+e >= 0 and destination+e < 64 and self.board[destination+e][0] == 'N' and destination+e in [(ord(notation[1]) - 97)+8*k for k in range(8)]:
                            origin = destination+e
                            return origin, destination
                else:
                    for e in knightMoves:
                        if destination+e >= 0 and destination+e < 64 and self.board[destination+e][0] == 'N' and destination+e in [8*(int(notation[1])-1)+k for k in range(8)]:
                            origin = destination+e
                            return origin, destination
            else:
                for e in knightMoves:
                    if destination+e >= 0 and destination+e < 64 and self.board[destination+e][0] == 'N':
                        origin = destination+e
                        return origin, destination              
    
    def get_rook_move(self, player, notation):
        try:
            destination = self.coordinate(len(notation)-2, len(notation) - 1,notation)
            if player == 0:                    
                if len(notation) > 3 and notation[1] != "x":
                    if notation[1].isalpha() == True:
                        for i in range(8):
                            if self.board[(ord(notation[1])-97)+i*8][0] == "r":
                                origin = (ord(notation[1])-97)+i*8
                                return origin, destination
                    else:
                        for i in range(8):
                            if self.board[(int(notation[1])-1)*8+i][0] == "r":
                                origin = (int(notation[1])-1)*8+i
                                return origin, destination
                        
                else:
                    #check horizontals
                    j = destination+1
                    while j < (int(destination/8)+1)*8:
                        if self.board[j] != "  ":
                            if self.board[j][0] == "r":
                                origin = j
                                return origin, destination
                            else: 
                                break
                        j += 1
                        
                    j = destination-1
                    while j >= int(destination/8)*8:
                        if self.board[j] != "  ":
                            if self.board[j][0] == "r":
                                origin = j
                                return origin, destination
                            else: 
                                break
                        j -= 1    
                    
                    #check verticals
                    j = destination+8
                    while j < 64:
                        if self.board[j] != "  ":
                            if self.board[j][0] == "r":
                                origin = j
                                return origin, destination
                            else: 
                                break
                        j += 8
                    j = destination-8
                    while j >= 0:
                        if self.board[j] != "  ":
                            if self.board[j][0] == "r":
                                origin = j
                                return origin, destination
                            else: 
                                break
                        j -= 8

            if player == 1:
                if len(notation) > 3 and notation[1] != "x":
                    if notation[1].isalpha() == True:
                        for i in range(8):
                            if self.board[(ord(notation[1])-97)+i*8][0] == "R":
                                origin = (ord(notation[1])-97)+i*8
                                return origin, destination
                    else:
                        for i in range(8):
                            if self.board[(int(notation[1])-1)*8+i][0] == "R":
                                origin = (int(notation[1])-1)*8+i
                                return origin, destination
                        
                else:
                    #check horizontals
                    j = destination+1
                    while j < (int(destination/8)+1)*8:
                        if self.board[j] != "  ":
                            if self.board[j][0] == "R":
                                origin = j
                                return origin, destination
                            else: 
                                break
                        j += 1
                        
                    j = destination-1
                    while j >= int(destination/8)*8:
                        if self.board[j] != "  ":
                            if self.board[j][0] == "R":
                                origin = j
                                return origin, destination
                            else: 
                                break
                        j -= 1    
                    
                    #check verticals
                    j = destination+8
                    while j < 64:
                        if self.board[j] != "  ":
                            if self.board[j][0] == "R":
                                origin = j
                                return origin, destination
                            else: 
                                break
                        j += 8
                    j = destination-8
                    while j >= 0:
                        if self.board[j] != "  ":
                            if self.board[j][0] == "R":
                                origin = j
                                return origin, destination
                            else: 
                                break
                        j -= 8

        except:
            traceback.print_exc()
            pdb.set_trace()  
            
        
        
        
    def move_piece(self, player, notation):
        try:
            if notation[0].islower() == True: 
                origin, destination = self.get_pawn_move(player,notation)
            if notation[0] == "B":
                origin, destination = self.get_bishop_move(player,notation)
            if notation[0] == "Q":
                origin, destination = self.get_queen_move(player,notation)    
            if notation[0] == "K":
                origin, destination = self.get_king_move(player,notation)
            if notation[0] == "N":
                origin, destination = self.get_knight_move(player,notation)
            if notation[0] == "R":
                origin, destination = self.get_rook_move(player,notation)
        
            if notation == "0-0" or notation == "O-O":
                if player == 0:
                    self.board[6] = "k "
                    self.board[5] = "r2"
                    self.board[7] = "  "
                    self.board[4] = "  "
                if player == 1:
                    self.board[62] = "K "
                    self.board[61] = "R1"
                    self.board[63] = "  "
                    self.board[60] = "  "
            elif notation == "0-0-0" or notation == "O-O-O":
                if player == 0:
                    self.board[2] = "k "
                    self.board[3] = "r1"
                    self.board[0] = "  "
                    self.board[4] = "  "
                if player == 1:
                    self.board[58] = "K "
                    self.board[59] = "R2"
                    self.board[56] = "  "
                    self.board[60] = "  "
                        
            else:
                self.board[destination] = self.board[origin]
                self.board[origin] = "  "
        
        except:
            traceback.print_exc()
            pdb.set_trace()         
    
    
    def showScreen(self):
        print(" -------------------------")
        print(" |  |  |  |  |  |  |  |  |")
        print("8|" + self.board[56] + "|" + self.board[57] + "|" + self.board[58] + "|" + self.board[59] + 
              "|" + self.board[60] + "|" + self.board[61] + "|" + self.board[62] + "|" + self.board[63] + "|")
        print(" |  |  |  |  |  |  |  |  |")
        print(" -------------------------")
        print(" |  |  |  |  |  |  |  |  |")
        print("7|" + self.board[48] + "|" + self.board[49] + "|" + self.board[50] + "|" + self.board[51] +
              "|" + self.board[52] + "|" + self.board[53] + "|" + self.board[54] + "|" + self.board[55] + "|")
        print(" |  |  |  |  |  |  |  |  |")
        print(" -------------------------")
        print(" |  |  |  |  |  |  |  |  |")
        print("6|" + self.board[40] + "|" + self.board[41] + "|" + self.board[42] + "|" + self.board[43] +
              "|" + self.board[44] + "|" + self.board[45] + "|" + self.board[46] + "|" + self.board[47] + "|")
        print(" |  |  |  |  |  |  |  |  |")
        print(" -------------------------")
        print(" |  |  |  |  |  |  |  |  |")
        print("5|" + self.board[32] + "|" + self.board[33] + "|" + self.board[34] + "|" + self.board[35] +
              "|" + self.board[36] + "|" + self.board[37] + "|" + self.board[38] + "|" + self.board[39] + "|")
        print(" |  |  |  |  |  |  |  |  |")
        print(" -------------------------")
        print(" |  |  |  |  |  |  |  |  |")
        print("4|" + self.board[24] + "|" + self.board[25] + "|" + self.board[26] + "|" + self.board[27] +
              "|" + self.board[28] + "|" + self.board[29] + "|" + self.board[30] + "|" + self.board[31] + "|")
        print(" |  |  |  |  |  |  |  |  |")
        print(" -------------------------")
        print(" |  |  |  |  |  |  |  |  |")
        print("3|" + self.board[16] + "|" + self.board[17] + "|" + self.board[18] + "|" + self.board[19] +
              "|" + self.board[20] + "|" + self.board[21] + "|" + self.board[22] + "|" + self.board[23] + "|")
        print(" |  |  |  |  |  |  |  |  |")
        print(" -------------------------")
        print(" |  |  |  |  |  |  |  |  |")
        print("2|" + self.board[8] + "|" + self.board[9] + "|" + self.board[10] + "|" + self.board[11] +
              "|" + self.board[12] + "|" + self.board[13] + "|" + self.board[14] + "|" + self.board[15] + "|")
        print(" |  |  |  |  |  |  |  |  |")
        print(" -------------------------")
        print(" |  |  |  |  |  |  |  |  |")
        print("1|" + self.board[0] + "|" + self.board[1] + "|" + self.board[2] + "|" + self.board[3] +
              "|" + self.board[4] + "|" + self.board[5] + "|" + self.board[6] + "|" + self.board[7] + "|")
        print(" |  |  |  |  |  |  |  |  |")
        print(" -------------------------")
        print("  a  b  c  d  e  f  g  h ")