import pygame

# Initialize Pygame
pygame.init()

# Set up the window
screen_size = (900, 900)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("My Game")

background_color = (164, 0, 54)
screen.fill(background_color)

# Set up the font
font = pygame.font.Font(None, 36)

# Set up the button
button_text = font.render("Play", True, (255, 255, 255))
button_rect = button_text.get_rect(center=screen.get_rect().center)

# Set up the game screen
game_text = font.render("Welcome to the game!", True, (255, 255, 255))
game_rect = game_text.get_rect(center=screen.get_rect().center)

image = pygame.image.load("C:/Users/aadil/Desktop/hhh.png")
image_rect = image.get_rect(center=screen.get_rect().center)

# Scale up the image
scale_factor = 2
scaled_size = (image.get_width() * scale_factor, image.get_height() * scale_factor)
scaled_image = pygame.transform.scale(image, scaled_size)

# Get the rectangle for the scaled image
scaled_rect = scaled_image.get_rect(center=screen.get_rect().center)


buttons = []
buttons.append({"rect": pygame.Rect(400, 400, 100, 100), "text": (1,2)})
buttons.append({"rect": pygame.Rect(515, 400, 100, 100), "text": (2,2)})
buttons.append({"rect": pygame.Rect(285, 400, 50, 100), "text": (3,2)})
buttons.append({"rect": pygame.Rect(400, 465, 100, 100), "text": (4,6)})
buttons.append({"rect": pygame.Rect(400, 335, 100, 100), "text": (5,6)})

board = [[0 for j in range(11)] for i in range(19)]

def makeboard():
    i=0
    j=0
    for i in range(19):
        for j in range(11):
            break
    

makeboard()

def gamefunction(arg1):
    print(arg1)

def computerturn():
    print("")

# Main game loop
running = True
play_pressed = False
playerturn = True
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
        if playerturn:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    for button in buttons:
                        if button["rect"].collidepoint(mouse_pos):
                            gamefunction(button["text"])
        else:
            computerturn()
            playerturn=True
        
        
    # If play hasn't been pressed, show the button
    else:
        # Draw the button
        pygame.draw.rect(screen, (78, 0, 45), button_rect)
        screen.blit(button_text, button_rect)

    # Update the screen
    pygame.display.flip()

# Quit Pygame
pygame.quit()


