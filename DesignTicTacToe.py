

class TicTacToeGame(object):
    def __init__(self,n,p1,p2):
        self.size = n
        self.board = [[None for i in range(n)] for i in range(n)]
        self.p1 = p1
        self.p2 = p2

    def playGame(self):
        r,c = 0,0
        turn = self.p1
        result = False
        nTurns = 0

        while not result:
            x = input()
            nTurns += 1
            draw = False

            if turn == self.p1:
                self.move(r,c,self.p1)
                lastplayed = self.p1
                turn = self.p2

            else:
                self.move(r,c,self.p2)
                lastplayed = self.p2
                turn = self.p1

            if nTurns >= self.size:
                result = self.checkResult()
                if result:
                    if not draw:
                        winner = lastplayed
                    else:
                        winner = 'Draw'
                      

        def move(self,r,c,player):
            self.board[r][c] = player
    
        def checkResult(self):
            for row in self.board:
                if len(set(row)) == 1:
                    return True
                    break

            for j in range(self.size):
                st = set()
                for i in range(self.size):
                    st.add(self.board[i][j])
                if len(st) == 1:
                    return True
                    break
            
            i,j = 0,0
            x,y = 0,self.size-1
            while (i<self.size and j<self.size) or (x<self.size and y>=0):
                st_ij = set()
                st_ij.add(self.board[i][j])
                i += 1
                j += 1
                st_xy = set()
                st_ij.add(self.board[x][y])
                x += 1
                y -= 1

            if len(st_ij) == 1 or len(st_xy)==1:
                return True

            if nTurns == self.size * self.size:
                draw = True
                result = True



board = [[None for i in range(3)] for i in range(3)]
board[1][1] = 'x'
print(board[1][1],board[0][1])

