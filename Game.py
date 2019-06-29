import pygame, time, math, os, sys # Might need time, os, or sys
screen_width = 1000 #need to change the dimensions to add a menu and chess engine info, and to fit the screen better.
screen_height = 1000
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Game") #could change this to "Chess" or "Chess game"
#Image files:
R1 = pygame.image.load("C:\\Users/chris/OneDrive/Pictures/Rook1.png") #need to load images from github or downloaded ZIP file, not my computer 
N1 = pygame.image.load("C:\\Users/chris/OneDrive/Pictures/Knight1.png")
B1 = pygame.image.load("C:\\Users/chris/OneDrive/Pictures/Bishop1.png")
Q1 = pygame.image.load("C:\\Users/chris/OneDrive/Pictures/Queen1.png")
K1 = pygame.image.load("C:\\Users/chris/OneDrive/Pictures/King1.png")
P1 = pygame.image.load("C:\\Users/chris/OneDrive/Pictures/Pawn1.png")
R0 = pygame.image.load("C:\\Users/chris/OneDrive/Pictures/Rook0.png")
N0 = pygame.image.load("C:\\Users/chris/OneDrive/Pictures/Knight0.png")
B0 = pygame.image.load("C:\\Users/chris/OneDrive/Pictures/Bishop0.png")
Q0 = pygame.image.load("C:\\Users/chris/OneDrive/Pictures/Queen0.png")
K0 = pygame.image.load("C:\\Users/chris/OneDrive/Pictures/King0.png")
P0 = pygame.image.load("C:\\Users/chris/OneDrive/Pictures/Pawn0.png")
#Image offsets for diferent pieces:
Rxoff = 8 # Could do Roff = (xoff,yoff) as a tuple
Ryoff = 5
Nxoff = 3
Nyoff = 3
Bxoff = 5
Byoff = 3
Qxoff = 3
Qyoff = 4
Kxoff = 5
Kyoff = 5
Pxoff = 10
Pyoff = 5
board = [[R1,N1,B1,Q1,K1,B1,N1,R1],[P1,P1,P1,P1,P1,P1,P1,P1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[P0,P0,P0,P0,P0,P0,P0,P0],[R0,N0,B0,Q0,K0,B0,N0,R0]]
#so python doesnt error; will rearange functions and remove later
def setup():
    board = [[R1,N1,B1,Q1,K1,B1,N1,R1],[P1,P1,P1,P1,P1,P1,P1,P1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[P0,P0,P0,P0,P0,P0,P0,P0],[R0,N0,B0,Q0,K0,B0,N0,R0]]
    #Starting position for chess
    #add more to this
def redraw(): #Update the pygame window
    screen.fill((230,230,230)) #close to white, but not 100% white
    draw_board() #Draw the pieces and squares
    pygame.display.update() #Update display
def draw_board(): #Seperate function for pieces and squares
    for i in range(0,64):
        if math.floor(i/8)%2 == 0: #Whether it does a green square or a white one
            if i%2 == 1:
                color = (0,150,30)#can change to black or other color
            else:
                color = (255,255,255)
        else:
            color = (255,255,255)
            if i%2 == 0:
                color = (0,150,30)
        pygame.draw.rect(screen,color,((i%8)*48,math.floor((i/8)+1)*48,48,48))
    for i in range(0,64):
        piece = board[math.floor(i/8)][i%8] #Load correct image file for the piecce
        xoff = 0
        yoff = 0
        if piece == R1 or piece == R0:
            xoff = Rxoff
            yoff = Ryoff
        if piece == N1 or piece == N0:
            xoff = Nxoff
            yoff = Nyoff
        if piece == B1 or piece == B0:
            xoff = Bxoff
            yoff = Byoff
        if piece == Q1 or piece == Q0:
            xoff = Qxoff
            yoff = Qyoff
        if piece == K1 or piece == K0:
            xoff = Kxoff
            yoff = Kyoff
        if piece == P1 or piece == P0:
            xoff = Pxoff
            yoff = Pyoff
        if not piece == 0:
            screen.blit(piece,((i%8)*48+xoff,(math.floor(i/8)+1)*48+yoff)) #Put piece at the right place
def possible_moves(index):
    piece = board[math.floor(index/8)][index%8]
    possible_moves = []
    if piece == P0: #If piece is white pawn
        if math.floor(index/8) == 2: #If pawn is on rank 2 (starting position)
            if board[math.floor((index)/8)+1][index%8] == 0: #If no piece is directly in front of pawn
                possible_moves.append(index+8) #It can move to square in front
            if board[math.floor((index)/8)+2][index%8] == 0: #If no piece is two spaces in front of pawn
                possible_moves.append(index+16) #It can move two squares forward
        else: #If pawn is NOT on rank 2
            if board[math.floor((index)/8)+1][index%8] == 0: #If no piece is directly in front of pawn 
                possible_moves.append(index+8) #It can move 1 square forward
        #Add functions for black pawn (similar) and all other pieces
def mousepress():
    (mousex,mousey) = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:# Check if mouse is down
            pass #Need to add something checking which piece the mouse clicked, then wait until they click again in destination square
def main():
    setup()
    run = True
    while run:
        redraw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #If user closes the pygame window
                pygame.quit() #Closes the pygame window
                run = False
main() #Start the whole program
#Need to add:
#Engine.py (Chess engine)
#Piece movement
#Customization (maybe)
