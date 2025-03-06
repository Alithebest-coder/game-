import  pygame
pygame.init()

screen=pygame.display.set_mode ((800,600))
pygame.display.set_caption("space invader")
icon=pygame.image.load("ufo.png")
pygame.display.set_icon(icon)

playerImg=pygame.image.load("player.png")
playerX=370
playerY=480
player_change=0
def player(x,y):
    screen.blit(playerImg,(x,y))

enemyImg=pygame.image.load("enemy.png")
enemyX=370
enemyY=50
enemy_change=0
def enemy(x,y):
    screen.blit(enemyImg,(x,y))

running=True

while running:

    screen.fill((255,192,203))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                player_change=-0.3
            if event.key==pygame.K_RIGHT:
                player_change=0.3

    playerX+=player_change
    player(playerX,playerY)
    enemy(enemyX,enemyY)
    pygame.display.update()
