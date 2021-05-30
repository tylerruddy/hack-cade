# Simple pygame program

# Import and initialize the pygame library
import pygame
from random import shuffle
pygame.init()

square = 20
blockM = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 2, 2, 2, 2, 2, 2, 2, 1, 1, 0, 0, 0, 0, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1],
    [1, 2, 1, 2, 1, 1, 1, 2, 2, 2, 1, 0, 0, 0, 0, 1, 2, 2, 2, 1, 1, 1, 2, 1, 2, 1],
    [1, 2, 1, 2, 3, 2, 2, 2, 1, 2, 1, 1, 0, 0, 1, 1, 2, 1, 2, 2, 2, 3, 2, 1, 2, 1],
    [1, 2, 1, 1, 2, 1, 1, 1, 1, 2, 2, 1, 0, 0, 1, 2, 2, 1, 1, 1, 1, 2, 1, 1, 2, 1],
    [1, 2, 2, 2, 2, 1, 2, 2, 2, 1, 2, 1, 0, 0, 1, 2, 1, 2, 2, 2, 1, 2, 2, 2, 2, 1],
    [1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1],
    [0, 0, 1, 2, 1, 1, 2, 1, 1, 2, 1, 2, 2, 2, 2, 1, 2, 1, 1, 2, 1, 1, 2, 1, 0, 0],
    [0, 0, 1, 2, 1, 1, 2, 1, 1, 2, 2, 1, 2, 2, 1, 2, 2, 1, 1, 2, 1, 1, 2, 1, 0, 0],
    [0, 0, 1, 2, 2, 2, 2, 1, 1, 1, 2, 1, 2, 2, 1, 2, 1, 1, 1, 2, 2, 2, 2, 1, 0, 0],
    [0, 0, 1, 2, 1, 1, 2, 1, 0, 1, 2, 2, 2, 2, 2, 2, 1, 0, 1, 2, 1, 1, 2, 1, 0, 0],
    [0, 0, 1, 2, 1, 2, 2, 1, 0, 1, 1, 2, 1, 1, 2, 1, 1, 0, 1, 2, 2, 1, 2, 1, 0, 0],
    [1, 1, 1, 2, 2, 2, 2, 1, 0, 0, 1, 2, 2, 2, 2, 1, 0, 0, 1, 2, 2, 2, 2, 1, 1, 1],
    [2, 2, 2, 2, 1, 2, 2, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 2, 2, 1, 2, 2, 2, 2],
    [1, 1, 1, 2, 2, 1, 2, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 2, 1, 2, 2, 1, 1, 1],
    [0, 0, 1, 2, 2, 2, 2, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 2, 2, 2, 2, 1, 0, 0],
    [0, 0, 1, 2, 2, 1, 2, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 2, 1, 2, 2, 1, 0, 0],
    [0, 0, 1, 2, 1, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 1, 1, 2, 1, 0, 0],
    [0, 0, 1, 2, 2, 2, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 2, 1, 0, 0],
    [0, 0, 1, 2, 1, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 1, 1, 2, 1, 0, 0],
    [1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1],
    [1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1],
    [1, 2, 1, 1, 2, 3, 2, 1, 2, 1, 0, 0, 0, 0, 0, 0, 1, 2, 1, 2, 3, 2, 1, 1, 2, 1],
    [1, 2, 1, 2, 2, 1, 2, 1, 2, 1, 0, 0, 0, 0, 0, 0, 1, 2, 1, 2, 1, 2, 2, 1, 2, 1],
    [1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

# Set up the drawing window
(width, height) = (len(blockM) * square, len(blockM[0]) * square)
screen = pygame.display.set_mode((width, height))
pygame.display.flip()
pacman = {"row": 1,
          "col": 1,
          "dir": "none",
          "score": 0,
          "cherry": False,
          "lives": 3
}
life = [24, 12]
num_enemies = 4
enemies = [{"row": 12, "col": 12, "alive": True, "dir": "None"},
           {"row": 12, "col": 12, "alive": True, "dir": "None"},
           {"row": 12, "col": 12, "alive": True, "dir": "None"},
           {"row": 12, "col": 12, "alive": True, "dir": "None"}
]

def randomTurn(enemy):
    deck = ""
    if enemy["col"] - 1 >= 0 and blockM[enemy["row"]][enemy["col"]-1] != 1:
        deck += "left "
    if enemy["col"] + 1 < len(blockM[0]) and blockM[enemy["row"]][enemy["col"]+1] != 1:
        deck += "right "
    if enemy["row"] - 1 >= 0 and blockM[enemy["row"]-1][enemy["col"]] != 1:
        deck += "up "
    if enemy["row"] + 1 < len(blockM) and blockM[enemy["row"]+1][enemy["col"]] != 1:
        deck += "down "

    deck = deck.split()
    shuffle(deck)
    enemy["dir"] = deck[0]
    
    if len(deck) == 2 and enemy["dir"] in deck:
        deck[0] = enemy["dir"]

    if deck[0] == "left":
        enemy["col"] -= 1
        enemy["dir"] = "left"
    if deck[0] == "right":
        enemy["col"] += 1
        enemy["dir"] = "right"
    if deck[0] == "up":
        enemy["row"] -= 1
        enemy["dir"] = "up"
    if deck[0] == "down":
        enemy["col"] += 1
        enemy["dir"] = "down"

def renderM():
    # Fill with black
    screen.fill((0, 0, 0))
    # Wall == blue == 1
    # Tic-Tac == small white == 2
    # Cherry == big white == 3
    for i in range(len(blockM)):
        for j in range(len(blockM[0])):
            if blockM[i][j] == 1:
                pygame.draw.rect(screen, (0, 0, 255), (j * square, i * square, square, square))
            elif blockM[i][j] == 2:
                pygame.draw.circle(screen, (255, 255, 255), (j * square + square / 2, i * square + square / 2), square / 6)
            elif blockM[i][j] == 3:
                pygame.draw.circle(screen, (255, 255, 255), (j * square + square / 2, i * square + square / 2), square / 3)
    
    pygame.draw.circle(screen, (255, 255, 0), (pacman["col"] * square + square / 2, pacman["row"] * square + square / 2), square / 3)

    if blockM[pacman["row"]][pacman["col"]] == 2:
        pacman["score"] += 1
        blockM[pacman["row"]][pacman["col"]] = 0
    elif blockM[pacman["row"]][pacman["col"]] == 3:
        pacman["score"] += 10
        blockM[pacman["row"]][pacman["col"]] = 0
        pacman["cherr"] = True

    for en in enemies:
        if en["alive"]:
            pygame.draw.circle(screen, (255, 0, 0), (en["col"] * square + square / 2, en["row"] * square + square / 2), square / 3)

    if pacman["lives"] >= 1:
        pygame.draw.circle(screen, (255, 0, 0), (life[1] * square + square / 2, life[0] * square + square / 2), square / 3)
    if pacman["lives"] >= 2:
        pygame.draw.circle(screen, (255, 0, 0), ((life[1]+1) * square + square / 2, life[0] * square + square / 2), square / 3)
    if pacman["lives"] == 3:
        pygame.draw.circle(screen, (255, 0, 0), ((life[1]+2) * square + square / 2, life[0] * square + square / 2), square / 3)
                
    pygame.display.update()

# Run until the user asks to quit
running = True
count = 0
while running:
    renderM()
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                pacman["dir"] = "up"
            elif event.key == pygame.K_d:
                pacman["dir"] = "right"
            elif event.key == pygame.K_s:
                pacman["dir"]= "down"
            elif event.key == pygame.K_a:
                pacman["dir"]= "left"
            elif event.key == pygame.K_q:
                running = False

    if count == 2000:
        count = 0
        if pacman["dir"] == "up" and blockM[pacman["row"]-1][pacman["col"]] != 1:
            pacman["row"] -= 1
        elif pacman["dir"] == "down" and blockM[pacman["row"]+1][pacman["col"]] != 1:
            pacman["row"] += 1
        elif pacman["dir"] == "left":
            if pacman["col"] == 0:
                pacman["col"] = len(blockM[0])-1
            elif blockM[pacman["row"]][pacman["col"]-1] != 1:
                pacman["col"] -= 1
        elif pacman["dir"] == "right":
            if pacman["col"] == len(blockM[0])-1:
                pacman["col"] = 0
            elif blockM[pacman["row"]][pacman["col"]+1] != 1:
                pacman["col"] += 1

        for en in enemies:
            if en["alive"]:
                randomTurn(en)
            
    # Fill the background with white
    screen.fill((0, 0, 0))
    count += 1
    # Draw a solid blue circle in the center
    # pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)

    # Flip the display

# Done! Time to quit.
print(pacman["score"])
pygame.quit()
