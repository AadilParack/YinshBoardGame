import pygame

# Initialize Pygame
pygame.init()

# Set up the window
screen_size = (900, 900)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("YINSH")
background_color = (164, 0, 54)
screen.fill(background_color)
font = pygame.font.Font(None, 36)

# Set up the button
start_button_text = font.render("Play", True, (255, 255, 255))
start_button_rect = start_button_text.get_rect(center=screen.get_rect().center)

# Scale up the image
image = pygame.image.load("C:/Users/aadil/Desktop/hhh.png")
image_rect = image.get_rect(center=screen.get_rect().center)
scale_factor = 2
scaled_size = (image.get_width() * scale_factor, image.get_height() * scale_factor)
scaled_image = pygame.transform.scale(image, scaled_size)
scaled_rect = scaled_image.get_rect(center=screen.get_rect().center)

#board
brd = [[0 for j in range(11)] for i in range(19)]
i=0
for i in range(0,19,2):
    brd[i][4]=1
    brd[i][6]=1
for i in range(2,17,2):
    brd[i][2]=1
    brd[i][8]=1
for i in range(6,13,2):
    brd[i][0]=1
    brd[i][10]=1
for i in range(1,18,2):
    brd[i][3]=1
    brd[i][5]=1
    brd[i][7]=1
for i in range(3,16,2):
    brd[i][1]=1
    brd[i][9]=1
    
#buttons
buttons = []
buttons.append({"rect": pygame.Rect(112+25, 303+25, 50, 50), "text": (6,0)})
buttons.append({"rect": pygame.Rect(112+25, 368+25, 50, 50), "text": (8,0)})
buttons.append({"rect": pygame.Rect(112+25, 433+25, 50, 50), "text": (10,0)})
buttons.append({"rect": pygame.Rect(112+25, 498+25, 50, 50), "text": (12,0)})
buttons.append({"rect": pygame.Rect(170+25, 205+25, 50, 50), "text": (3,1)})
buttons.append({"rect": pygame.Rect(170+25, 270+25, 50, 50), "text": (5,1)})
buttons.append({"rect": pygame.Rect(170+25, 335+25, 50, 50), "text": (7,1)})
buttons.append({"rect": pygame.Rect(170+25, 400+25, 50, 50), "text": (9,1)})
buttons.append({"rect": pygame.Rect(170+25, 465+25, 50, 50), "text": (11,1)})
buttons.append({"rect": pygame.Rect(170+25, 530+25, 50, 50), "text": (13,1)})
buttons.append({"rect": pygame.Rect(170+25, 595+25, 50, 50), "text": (15,1)})
buttons.append({"rect": pygame.Rect(227+25, 173+25, 50, 50), "text": (2,2)})
buttons.append({"rect": pygame.Rect(227+25, 238+25, 50, 50), "text": (4,2)})
buttons.append({"rect": pygame.Rect(227+25, 303+25, 50, 50), "text": (6,2)})
buttons.append({"rect": pygame.Rect(227+25, 368+25, 50, 50), "text": (8,2)})
buttons.append({"rect": pygame.Rect(227+25, 433+25, 50, 50), "text": (10,2)})
buttons.append({"rect": pygame.Rect(227+25, 498+25, 50, 50), "text": (12,2)})
buttons.append({"rect": pygame.Rect(227+25, 563+25, 50, 50), "text": (14,2)})
buttons.append({"rect": pygame.Rect(227+25, 628+25, 50, 50), "text": (16,2)})
buttons.append({"rect": pygame.Rect(285+25, 140+25, 50, 50), "text": (1,3)})
buttons.append({"rect": pygame.Rect(285+25, 205+25, 50, 50), "text": (3,3)})
buttons.append({"rect": pygame.Rect(285+25, 270+25, 50, 50), "text": (5,3)})
buttons.append({"rect": pygame.Rect(285+25, 335+25, 50, 50), "text": (7,3)})
buttons.append({"rect": pygame.Rect(285+25, 400+25, 50, 50), "text": (9,3)})
buttons.append({"rect": pygame.Rect(285+25, 465+25, 50, 50), "text": (11,3)})
buttons.append({"rect": pygame.Rect(285+25, 530+25, 50, 50), "text": (13,3)})
buttons.append({"rect": pygame.Rect(285+25, 595+25, 50, 50), "text": (15,3)})
buttons.append({"rect": pygame.Rect(285+25, 660+25, 50, 50), "text": (17,3)})
buttons.append({"rect": pygame.Rect(342+25, 108+25, 50, 50), "text": (0,4)})
buttons.append({"rect": pygame.Rect(342+25, 173+25, 50, 50), "text": (2,4)})
buttons.append({"rect": pygame.Rect(342+25, 238+25, 50, 50), "text": (4,4)})
buttons.append({"rect": pygame.Rect(342+25, 303+25, 50, 50), "text": (6,4)})
buttons.append({"rect": pygame.Rect(342+25, 368+25, 50, 50), "text": (8,4)})
buttons.append({"rect": pygame.Rect(342+25, 433+25, 50, 50), "text": (10,4)})
buttons.append({"rect": pygame.Rect(342+25, 498+25, 50, 50), "text": (12,4)})
buttons.append({"rect": pygame.Rect(342+25, 563+25, 50, 50), "text": (14,4)})
buttons.append({"rect": pygame.Rect(342+25, 628+25, 50, 50), "text": (16,4)})
buttons.append({"rect": pygame.Rect(342+25, 693+25, 50, 50), "text": (18,4)})
buttons.append({"rect": pygame.Rect(400+25, 140+25, 50, 50), "text": (1,5)})
buttons.append({"rect": pygame.Rect(400+25, 205+25, 50, 50), "text": (3,5)})
buttons.append({"rect": pygame.Rect(400+25, 270+25, 50, 50), "text": (5,5)})
buttons.append({"rect": pygame.Rect(400+25, 335+25, 50, 50), "text": (7,5)})
buttons.append({"rect": pygame.Rect(400+25, 400+25, 50, 50), "text": (9,5)})
buttons.append({"rect": pygame.Rect(400+25, 465+25, 50, 50), "text": (11,5)})
buttons.append({"rect": pygame.Rect(400+25, 530+25, 50, 50), "text": (13,5)})
buttons.append({"rect": pygame.Rect(400+25, 595+25, 50, 50), "text": (15,5)})
buttons.append({"rect": pygame.Rect(400+25, 660+25, 50, 50), "text": (17,5)})
buttons.append({"rect": pygame.Rect(457+25, 108+25, 50, 50), "text": (0,6)})
buttons.append({"rect": pygame.Rect(457+25, 173+25, 50, 50), "text": (2,6)})
buttons.append({"rect": pygame.Rect(457+25, 238+25, 50, 50), "text": (4,6)})
buttons.append({"rect": pygame.Rect(457+25, 303+25, 50, 50), "text": (6,6)})
buttons.append({"rect": pygame.Rect(457+25, 368+25, 50, 50), "text": (8,6)})
buttons.append({"rect": pygame.Rect(457+25, 433+25, 50, 50), "text": (10,6)})
buttons.append({"rect": pygame.Rect(457+25, 498+25, 50, 50), "text": (12,6)})
buttons.append({"rect": pygame.Rect(457+25, 563+25, 50, 50), "text": (14,6)})
buttons.append({"rect": pygame.Rect(457+25, 628+25, 50, 50), "text": (16,6)})
buttons.append({"rect": pygame.Rect(457+25, 693+25, 50, 50), "text": (18,6)})
buttons.append({"rect": pygame.Rect(515+25, 140+25, 50, 50), "text": (1,7)})
buttons.append({"rect": pygame.Rect(515+25, 205+25, 50, 50), "text": (3,7)})
buttons.append({"rect": pygame.Rect(515+25, 270+25, 50, 50), "text": (5,7)})
buttons.append({"rect": pygame.Rect(515+25, 335+25, 50, 50), "text": (7,7)})
buttons.append({"rect": pygame.Rect(515+25, 400+25, 50, 50), "text": (9,7)})
buttons.append({"rect": pygame.Rect(515+25, 465+25, 50, 50), "text": (11,7)})
buttons.append({"rect": pygame.Rect(515+25, 530+25, 50, 50), "text": (13,7)})
buttons.append({"rect": pygame.Rect(515+25, 595+25, 50, 50), "text": (15,7)})
buttons.append({"rect": pygame.Rect(515+25, 660+25, 50, 50), "text": (17,7)})
buttons.append({"rect": pygame.Rect(572+25, 173+25, 50, 50), "text": (2,8)})
buttons.append({"rect": pygame.Rect(572+25, 238+25, 50, 50), "text": (4,8)})
buttons.append({"rect": pygame.Rect(572+25, 303+25, 50, 50), "text": (6,8)})
buttons.append({"rect": pygame.Rect(572+25, 368+25, 50, 50), "text": (8,8)})
buttons.append({"rect": pygame.Rect(572+25, 433+25, 50, 50), "text": (10,8)})
buttons.append({"rect": pygame.Rect(572+25, 498+25, 50, 50), "text": (12,8)})
buttons.append({"rect": pygame.Rect(572+25, 563+25, 50, 50), "text": (14,8)})
buttons.append({"rect": pygame.Rect(572+25, 628+25, 50, 50), "text": (16,8)})
buttons.append({"rect": pygame.Rect(630+25, 205+25, 50, 50), "text": (3,9)})
buttons.append({"rect": pygame.Rect(630+25, 270+25, 50, 50), "text": (5,9)})
buttons.append({"rect": pygame.Rect(630+25, 335+25, 50, 50), "text": (7,9)})
buttons.append({"rect": pygame.Rect(630+25, 400+25, 50, 50), "text": (9,9)})
buttons.append({"rect": pygame.Rect(630+25, 465+25, 50, 50), "text": (11,9)})
buttons.append({"rect": pygame.Rect(630+25, 530+25, 50, 50), "text": (13,9)})
buttons.append({"rect": pygame.Rect(630+25, 595+25, 50, 50), "text": (15,9)})
buttons.append({"rect": pygame.Rect(687+25, 303+25, 50, 50), "text": (6,10)})
buttons.append({"rect": pygame.Rect(687+25, 368+25, 50, 50), "text": (8,10)})
buttons.append({"rect": pygame.Rect(687+25, 433+25, 50, 50), "text": (10,10)})
buttons.append({"rect": pygame.Rect(687+25, 498+25, 50, 50), "text": (12,10)})

    
playerscore = 0
pcscore = 0

#gamerule
running = True
play_pressed = False
playerturn = True
player_win= False
pc_win=False

def renderboard():
    screen.fill(background_color)
    screen.blit(scaled_image, scaled_rect)
    for button in buttons:
        arg=button["text"]
        if brd[arg[0]][arg[1]] == 2:
            pcringimgrect = button["rect"]
            screen.blit(pcringimg, pcringimgrect)
        elif brd[arg[0]][arg[1]] == 3:
            plringimgrect = button["rect"]
            screen.blit(plringimg, plringimgrect)
        elif brd[arg[0]][arg[1]] == 4:
            pctokimgrect = button["rect"]
            screen.blit(pctokimg, pctokimgrect)
        elif brd[arg[0]][arg[1]] == 5:
            pltokimgrect = button["rect"]
            screen.blit(pltokimg, pltokimgrect)
    pygame.display.flip()

def playerplays():
    playerturn=False

def pcplays():
    playerturn=True
    

def checkline():
    print()
    

def scorerender():
    scoretext = font.render("Score: ", True, (255, 255, 255))
    start_button_rect = start_button_text.get_rect(center=screen.get_rect().center)
    print()


while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if start_button_rect.collidepoint(mouse_pos):
                play_pressed = True
    # If play has been pressed, show the game screen
    if play_pressed:
        break
    # If play hasn't been pressed, show the button
    else:
        # Draw the button
        pygame.draw.rect(screen, (78, 0, 45), start_button_rect)
        screen.blit(start_button_text, start_button_rect)
    # Update the screen
    pygame.display.flip()


print("k")

screen.fill(background_color)
screen.blit(scaled_image, scaled_rect)
pygame.display.flip()
#computerplace
pcringimg = pygame.image.load("C:/Users/aadil/Desktop/redring.png")
pctokimg = pygame.image.load("C:/Users/aadil/Desktop/redtok.png")

pcringimgrect = pygame.Rect(572+25, 303+25, 50, 50)
screen.blit(pcringimg, pcringimgrect)
pcringimgrect = pygame.Rect(285+25, 400+25, 50, 50)
screen.blit(pcringimg, pcringimgrect)
pcringimgrect = pygame.Rect(400+25, 270+25, 50, 50)
screen.blit(pcringimg, pcringimgrect)
pcringimgrect = pygame.Rect(400+25, 530+25, 50, 50)
screen.blit(pcringimg, pcringimgrect)
pcringimgrect = pygame.Rect(285+25, 595+25, 50, 50)
screen.blit(pcringimg, pcringimgrect)
brd[6][8]=2
brd[9][3]=2
brd[5][5]=2
brd[13][5]=2
brd[15][3]=2
print("l")
pygame.display.flip()

#playerplacement
plringimg = pygame.image.load("C:/Users/aadil/Desktop/bluering.png")
pltokimg = pygame.image.load("C:/Users/aadil/Desktop/bluetok.png")
placing= True
placed=0
while placing:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            print(mouse_pos)
            
            for button in buttons:
                if button["rect"].collidepoint(mouse_pos):
                    print(button["rect"])
                    arg=button["text"]
                    print(arg[0])
                    print(arg[1])
                    plringimgrect = button["rect"]
                    screen.blit(plringimg, plringimgrect)
                    placed=placed+1
                    brd[arg[0]][arg[1]]=3
                    pygame.display.flip()
    if placed >= 5:
        break

print("done")

for r in brd:
   for c in r:
      print(c,end = " ")
   print()
   
running=True
   
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
    # Draw the board
    renderboard()
    # Update the screen
    pygame.display.flip()
    

"""
while running:
    renderboard()
    if playerturn:
        playerplays()
    else:
        pcplays()
    checkline()
    scorerender()
    if player_win:
        
        break
    if pc_win:
        
        break

"""

pygame.quit()

#0=void
#1=placeable
#2=pcring
#3=plring
#4=pctok
#5=pltok
