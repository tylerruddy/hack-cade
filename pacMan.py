# Simple pygame program

# Import and initialize the pygame library
import pygame
from random import shuffle
pygame.init()

square = 20
blockM = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 0, 0, 0, 0, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1],
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
pacman = {"row": 7,
          "col": 13,
          "dir": "none",
          "score": 0,
          "lives": 3,
          "tt": 0
}
life = [24, 12]
num_enemies = 4
enemies = [{"row": 12, "col": 11, "dead": 0, "dir": "None", "weak": 0},
           {"row": 12, "col": 12, "dead": 0, "dir": "None", "weak": 0},
           {"row": 13, "col": 2, "dead": 0, "dir": "None", "weak": 0},
           {"row": 13, "col": 24, "dead": 0, "dir": "None", "weak": 0}
]

def randomTurn(enemy):
    if enemy["dir"] == "right" and enemy["col"] == len(blockM[0])-1:
        enemy["col"] = 0
    elif enemy["dir"] == "left" and enemy["col"] == 0:
        enemy["col"] = len(blockM[0])-1
    else:
        deck = ""
        if enemy["col"] - 1 >= 0 and blockM[enemy["row"]][enemy["col"]-1] != 1 and enemy["dir"] != "right":
            deck += "left "
        if enemy["col"] + 1 < len(blockM[0]) and blockM[enemy["row"]][enemy["col"]+1] != 1 and enemy["dir"] != "left":
            deck += "right "
        if enemy["row"] - 1 >= 0 and blockM[enemy["row"]-1][enemy["col"]] != 1 and enemy["dir"] != "down":
            deck += "up "
        if enemy["row"] + 1 < len(blockM) and blockM[enemy["row"]+1][enemy["col"]] != 1 and enemy["dir"] != "up":
            deck += "down "

        deck = deck.split()
        shuffle(deck)

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
            enemy["row"] += 1
            enemy["dir"] = "down"

def renderM():
    # Fill with black
    screen.fill((0, 0, 0))
    # Wall == blue == 1
    # Tic-Tac == small white == 2
    # Big white == 3
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
        pacman["score"] += 10
        pacman["tt"] += 1
        blockM[pacman["row"]][pacman["col"]] = 0
    elif blockM[pacman["row"]][pacman["col"]] == 3:
        pacman["score"] += 100
        pacman["tt"] += 1
        blockM[pacman["row"]][pacman["col"]] = 0
        for en in enemies:
            en["weak"] = 5000

    for en in enemies:
        if en["weak"] > 0:
            pygame.draw.circle(screen, (0, 255, 255), (en["col"] * square + square / 2, en["row"] * square + square / 2), square / 3)
        else:
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

    if count == 125:
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
                
        if pacman["tt"] == 248:
            running = False
    
    if count == 124:
        for en in enemies:
            randomTurn(en)
                
    for en in enemies:
        if en["weak"] > 0:
            en["weak"] -= 1
            
        if en["dead"] > 0:
            en["dead"] -= 1
            if en["dead"] == 0:
                en["row"] = 12
                en["col"] = 12
                
        if pacman["row"] == en["row"] and pacman["col"] == en["col"]:
            if en["weak"] > 0:
                en["row"] = 14
                en["col"] = 12
                en["dead"] = 2500
                en["weak"] = 0
                pacman["score"] += 200
            else:
                enemies[0]["row"] = 12
                enemies[0]["col"] = 11
                enemies[1]["row"] = 12
                enemies[1]["col"] = 12
                enemies[2]["row"] = 13
                enemies[2]["col"] = 2
                enemies[3]["row"] = 13
                enemies[3]["col"] = 24
                
                pacman["row"] = 7
                pacman["col"] = 13
                pacman["lives"] -= 1;
                pacman["dir"] = None
                if pacman["lives"] == 0:
                    running = False
                    # gameover screen
            
    # Fill the background with black
    screen.fill((0, 0, 0))
    count += 1


# Done! Time to quit.
print(pacman["score"])
pygame.quit()
