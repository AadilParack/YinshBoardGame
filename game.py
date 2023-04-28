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
button_text = font.render("Play", True, (255, 255, 255))
button_rect = button_text.get_rect(center=screen.get_rect().center)


# Scale up the image
image = pygame.image.load("C:/Users/aadil/Desktop/hhh.png")
image_rect = image.get_rect(center=screen.get_rect().center)
scale_factor = 2
scaled_size = (image.get_width() * scale_factor, image.get_height() * scale_factor)
scaled_image = pygame.transform.scale(image, scaled_size)
scaled_rect = scaled_image.get_rect(center=screen.get_rect().center)

#buttons
buttons = []
buttons.append({"rect": pygame.Rect(400, 400, 100, 100), "text": (1,2)})
buttons.append({"rect": pygame.Rect(515, 400, 100, 100), "text": (2,2)})
buttons.append({"rect": pygame.Rect(285, 400, 100, 100), "text": (3,2)})
buttons.append({"rect": pygame.Rect(400, 465, 100, 100), "text": (4,6)})
buttons.append({"rect": pygame.Rect(400, 335, 100, 100), "text": (5,6)})
buttons.append({"rect": pygame.Rect(400, 335, 100, 100), "text": (5,6)})
buttons.append({"rect": pygame.Rect(400, 335, 100, 100), "text": (5,6)})
buttons.append({"rect": pygame.Rect(400, 335, 100, 100), "text": (5,6)})
buttons.append({"rect": pygame.Rect(400, 335, 100, 100), "text": (5,6)})
buttons.append({"rect": pygame.Rect(400, 335, 100, 100), "text": (5,6)})
buttons.append({"rect": pygame.Rect(400, 400, 100, 100), "text": (1,2)})
buttons.append({"rect": pygame.Rect(515, 400, 100, 100), "text": (2,2)})
buttons.append({"rect": pygame.Rect(285, 400, 100, 100), "text": (3,2)})
buttons.append({"rect": pygame.Rect(400, 465, 100, 100), "text": (4,6)})
buttons.append({"rect": pygame.Rect(400, 335, 100, 100), "text": (5,6)})
buttons.append({"rect": pygame.Rect(400, 335, 100, 100), "text": (5,6)})
buttons.append({"rect": pygame.Rect(400, 335, 100, 100), "text": (5,6)})
buttons.append({"rect": pygame.Rect(400, 335, 100, 100), "text": (5,6)})
buttons.append({"rect": pygame.Rect(400, 335, 100, 100), "text": (5,6)})
buttons.append({"rect": pygame.Rect(400, 335, 100, 100), "text": (5,6)})
buttons.append({"rect": pygame.Rect(400, 400, 100, 100), "text": (1,2)})
buttons.append({"rect": pygame.Rect(515, 400, 100, 100), "text": (2,2)})
buttons.append({"rect": pygame.Rect(285, 400, 100, 100), "text": (3,2)})
buttons.append({"rect": pygame.Rect(400, 465, 100, 100), "text": (4,6)})
buttons.append({"rect": pygame.Rect(400, 335, 100, 100), "text": (5,6)})
buttons.append({"rect": pygame.Rect(400, 335, 100, 100), "text": (5,6)})
buttons.append({"rect": pygame.Rect(400, 335, 100, 100), "text": (5,6)})
buttons.append({"rect": pygame.Rect(400, 335, 100, 100), "text": (5,6)})
buttons.append({"rect": pygame.Rect(400, 335, 100, 100), "text": (5,6)})
buttons.append({"rect": pygame.Rect(400, 335, 100, 100), "text": (5,6)})
buttons.append({"rect": pygame.Rect(400, 400, 100, 100), "text": (1,2)})
buttons.append({"rect": pygame.Rect(515, 400, 100, 100), "text": (2,2)})
buttons.append({"rect": pygame.Rect(285, 400, 100, 100), "text": (3,2)})
buttons.append({"rect": pygame.Rect(400, 465, 100, 100), "text": (4,6)})
buttons.append({"rect": pygame.Rect(400, 335, 100, 100), "text": (5,6)})
buttons.append({"rect": pygame.Rect(400, 335, 100, 100), "text": (5,6)})
buttons.append({"rect": pygame.Rect(400, 335, 100, 100), "text": (5,6)})
buttons.append({"rect": pygame.Rect(400, 335, 100, 100), "text": (5,6)})
buttons.append({"rect": pygame.Rect(400, 335, 100, 100), "text": (5,6)})
buttons.append({"rect": pygame.Rect(400, 335, 100, 100), "text": (5,6)})
buttons.append({"rect": pygame.Rect(400, 400, 100, 100), "text": (1,2)})
buttons.append({"rect": pygame.Rect(515, 400, 100, 100), "text": (2,2)})
buttons.append({"rect": pygame.Rect(285, 400, 100, 100), "text": (3,2)})
buttons.append({"rect": pygame.Rect(400, 465, 100, 100), "text": (4,6)})
buttons.append({"rect": pygame.Rect(400, 335, 100, 100), "text": (5,6)})
buttons.append({"rect": pygame.Rect(400, 335, 100, 100), "text": (5,6)})
buttons.append({"rect": pygame.Rect(400, 335, 100, 100), "text": (5,6)})
buttons.append({"rect": pygame.Rect(400, 335, 100, 100), "text": (5,6)})
buttons.append({"rect": pygame.Rect(400, 335, 100, 100), "text": (5,6)})
buttons.append({"rect": pygame.Rect(400, 335, 100, 100), "text": (5,6)})
buttons.append({"rect": pygame.Rect(400, 400, 100, 100), "text": (1,2)})
buttons.append({"rect": pygame.Rect(515, 400, 100, 100), "text": (2,2)})
buttons.append({"rect": pygame.Rect(285, 400, 100, 100), "text": (3,2)})
buttons.append({"rect": pygame.Rect(400, 465, 100, 100), "text": (4,6)})
buttons.append({"rect": pygame.Rect(400, 335, 100, 100), "text": (5,6)})
buttons.append({"rect": pygame.Rect(400, 335, 100, 100), "text": (5,6)})
buttons.append({"rect": pygame.Rect(400, 335, 100, 100), "text": (5,6)})
buttons.append({"rect": pygame.Rect(400, 335, 100, 100), "text": (5,6)})
buttons.append({"rect": pygame.Rect(400, 335, 100, 100), "text": (5,6)})
buttons.append({"rect": pygame.Rect(400, 335, 100, 100), "text": (5,6)})
buttons.append({"rect": pygame.Rect(400, 400, 100, 100), "text": (1,2)})
buttons.append({"rect": pygame.Rect(515, 400, 100, 100), "text": (2,2)})
buttons.append({"rect": pygame.Rect(285, 400, 100, 100), "text": (3,2)})
buttons.append({"rect": pygame.Rect(400, 465, 100, 100), "text": (4,6)})
buttons.append({"rect": pygame.Rect(400, 335, 100, 100), "text": (5,6)})
buttons.append({"rect": pygame.Rect(400, 335, 100, 100), "text": (5,6)})
buttons.append({"rect": pygame.Rect(400, 335, 100, 100), "text": (5,6)})
buttons.append({"rect": pygame.Rect(400, 335, 100, 100), "text": (5,6)})
buttons.append({"rect": pygame.Rect(400, 335, 100, 100), "text": (5,6)})
buttons.append({"rect": pygame.Rect(400, 335, 100, 100), "text": (5,6)})
buttons.append({"rect": pygame.Rect(400, 400, 100, 100), "text": (1,2)})
buttons.append({"rect": pygame.Rect(515, 400, 100, 100), "text": (2,2)})
buttons.append({"rect": pygame.Rect(285, 400, 100, 100), "text": (3,2)})
buttons.append({"rect": pygame.Rect(400, 465, 100, 100), "text": (4,6)})
buttons.append({"rect": pygame.Rect(400, 335, 100, 100), "text": (5,6)})
buttons.append({"rect": pygame.Rect(400, 335, 100, 100), "text": (5,6)})
buttons.append({"rect": pygame.Rect(400, 335, 100, 100), "text": (5,6)})
buttons.append({"rect": pygame.Rect(400, 335, 100, 100), "text": (5,6)})
buttons.append({"rect": pygame.Rect(400, 335, 100, 100), "text": (5,6)})
buttons.append({"rect": pygame.Rect(400, 335, 100, 100), "text": (5,6)})
buttons.append({"rect": pygame.Rect(400, 335, 100, 100), "text": (5,6)})
buttons.append({"rect": pygame.Rect(400, 335, 100, 100), "text": (5,6)})
buttons.append({"rect": pygame.Rect(400, 335, 100, 100), "text": (5,6)})
buttons.append({"rect": pygame.Rect(400, 335, 100, 100), "text": (5,6)})
buttons.append({"rect": pygame.Rect(400, 335, 100, 100), "text": (5,6)})

#board
brd = [[0 for j in range(11)] for i in range(19)]

def initboard():
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
    
    
initboard()

def updateboard():
    print("")

#gamerule
running = True
play_pressed = False
playerturn = True

#gamelogic
def gamefunction(arg1):
    x=arg1[0]
    y=arg1[1]
    playerturn = False

def computerturn():
    
    playerturn = True

# Main game loop
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if button_rect.collidepoint(mouse_pos):
                play_pressed = True

    # If play has been pressed, show the game screen
    if play_pressed:
        # Clear the screen
        screen.fill(background_color)
        screen.blit(scaled_image, scaled_rect)
        #updateboard()
        for event in pygame.event.get():
            #if playerturn:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    for button in buttons:
                        if button["rect"].collidepoint(mouse_pos):
                            print(button["text"])
                            #gamefunction(button["text"])
            #else:
                #computerturn()
            
        
        
    # If play hasn't been pressed, show the button
    else:
        # Draw the button
        pygame.draw.rect(screen, (78, 0, 45), button_rect)
        screen.blit(button_text, button_rect)
        

    # Update the screen
    pygame.display.flip()

# Quit Pygame
pygame.quit()



