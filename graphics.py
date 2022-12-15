import random
import pygame
import main
# Global Variables
COLOR = (255, 100, 98)
SURFACE_COLOR = (167, 255, 100)
WIDTH = 500
HEIGHT = 500
current="images/east_plain.png"
#((main.L.loc(main.M.location).index(main.L.precise_location))) + 2 ==len(main.L.loc(main.M.location)) and  main.L.unlocked[(main.L.map.index(main.M.location)) + 1] != 1:
#checking if the area is enabled or not
def movement(direction,nx,ny,move):
    global current,encounter
    x=playerCar.rect.x
    y=playerCar.rect.y
    z=main.L.move(main.M.location)
    if direction == 'forward' and type(z) != tuple and move == True:
        bg='images/{0}.png'.format(z)
        current=bg
        playerCar.rect.y = ny
        playerCar.rect.x = nx
        main.L.precise_location = z
    elif direction == 'forward' and type(z) == tuple and ((main.L.loc(main.M.location).index(main.L.precise_location))) + 2 ==len(main.L.loc(main.M.location)) and  main.L.unlocked[(main.L.map.index(main.M.location)) + 1] == 1 and move == True:
            bg = 'images/{0}_open.png'.format(z[1])
            current = bg
            playerCar.rect.y = ny
            playerCar.rect.x = nx
            main.L.precise_location = z[1]
    elif direction == 'forward' and type(z) == tuple and ((main.L.loc(main.M.location).index(main.L.precise_location))) + 2 ==len(main.L.loc(main.M.location)) and  main.L.unlocked[(main.L.map.index(main.M.location)) + 1] != 1 and move == True:
            bg = 'images/{0}_closed.png'.format(z[1])
            current = bg
            playerCar.rect.y = ny
            playerCar.rect.x = nx
            main.L.precise_location = z[1]
    elif direction == 'forward' and type(z) == tuple and move == True:
        bg='images/{0}.png'.format(z[1])
        current=bg
        playerCar.rect.y = ny
        playerCar.rect.x = nx
        main.L.precise_location = z[1]
    elif direction == 'backward' and type(z) == tuple and move == True:
        bg='images/{0}.png'.format(z[0])
        current=bg
        playerCar.rect.y = ny
        playerCar.rect.x = nx
        main.L.precise_location = z[0]
    elif encounter[0] == True:
        bg=('images/battle_bg.png')
        current=bg
    else:
        print(current)
        return current
    return bg
def battle():
    global screen,current,encounter
    all_sprites_list.remove(playerCar)


def map_collision(current,dire):
    if current == 'images/east_plain.png':
        tela1 = telaport((0,0,0),1,500,0,0,'forward',playerCar.rect.x,470)
        barriers.add(tela1)
        tela1.collide()
    if current == 'images/south_plain.png':#fix the movement point location
        tela4 = telaport((0,0,0),500,1,0,0,'backward',450,playerCar.rect.y)
        barriers.add(tela4)
        tela4.collide()
        tela5 = telaport((0,0,0),500,1,480,0,'forward',30,playerCar.rect.y)
        barriers.add(tela5)
        tela5.collide()
        river1 = World_collide((0,0,0),180,160,210,0)
        barriers.add(river1)
        river1.collide(dire)
        river2 = World_collide((0,0,0),330,190,210,240)
        barriers.add(river2)
        river2.collide(dire)
    if current == 'images/west_plain_closed.png':
        tela8 = telaport((0,0,0),1,500,0,490,'backward',playerCar.rect.x,30)
        barriers.add(tela8)
        tela8.collide()
        wall1 = World_collide((0,0,0),20,200,10,50)
        barriers.add(wall1)
        wall1.collide(dire)
        gate = World_collide((0,0,0),20,120,200,50)
        barriers.add(gate)
        gate.collide(dire)
        wall2 = World_collide((0,0,0),20,200,320,50)
        barriers.add(wall2)
        wall2.collide(dire)
    if current == 'images/west_plain_open.png':
        wall1 = World_collide((0, 0, 0), 20, 200, 10, 50)
        barriers.add(wall1)
        wall1.collide(dire)
        wall2 = World_collide((0,0,0),20,200,320,50)
        barriers.add(wall2)
        wall2.collide(dire)
        tela9 = telaport((0,0,0),1,500,0,0,'forward',playerCar.rect.x,470)
        barriers.add(tela9)
        tela9.collide()
    if current =='images/north_plain.png':
        tela2 = telaport((0,0,0),1,500,0,490,'backward',playerCar.rect.x,30)
        barriers.add(tela2)
        tela2.collide()
        tela3 = telaport((0,0,0),500,1,470,0,'forward',30,playerCar.rect.y)
        barriers.add(tela3)
        tela3.collide()
        sea= World_collide((0,0,0),500,100,0,0)
        barriers.add(sea)
        sea.collide(dire)
    if current == 'images/central_plain.png':
        tela6 = telaport((0,0,0),500,1,0,0,'backward',450,playerCar.rect.y)
        barriers.add(tela6)
        tela6.collide()
        tela7 = telaport((0,0,0),10,500,0,0,'forward',playerCar.rect.x,470)
        barriers.add(tela7)
        tela7.collide()
# Object class
class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, height, width):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(SURFACE_COLOR)
        self.image.set_colorkey(COLOR)

        pygame.draw.rect(self.image,
                         color,
                         pygame.Rect(0, 0, width, height))

        self.rect = self.image.get_rect()
        self.rect.y=50
        self.speed = 0

    def moveRight(self, pixels):
        if not self.rect.x >= 480:
            self.rect.x += self.speed+pixels
    def moveLeft(self, pixels):
        if not  self.rect.x <= 0:
            self.rect.x -= self.speed+pixels
    def moveForward(self, speed):
        if not self.rect.y >= 470:
            self.rect.y += self.speed + speed

    def moveBack(self, speed):
        if not self.rect.y <= 0:
            self.rect.y -= self.speed + speed
pygame.init()
class Sprite_NPC(pygame.sprite.Sprite):
    def __init__(self, color, height, width,questgive):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(SURFACE_COLOR)
        self.image.set_colorkey(COLOR)

        pygame.draw.rect(self.image,
                         color,
                         pygame.Rect(0, 0, width, height))

        self.rect = self.image.get_rect()
        self.rect.x= 100
        self.rect.y=200
        self.queest = questgive
    def get_quest(self):
        print(self.queest)
    def collide(self):
        if playerCar.rect.x == self.rect.x and playerCar.rect.y == self.rect.y:
            print(self.queest)
class Sprite_enermy(pygame.sprite.Sprite):
    def __init__(self, enermy):
        super().__init__()
        spite = pygame.image.load('images/enermy.png')
        all_sprites_list.add(spite)
    #def collide(self):
        #if playerCar.rect.x == self.rect.x and playerCar.rect.y == self.rect.y:
            #print('r')
class telaport(pygame.sprite.Sprite):
    def __init__(self, color, height, width,x,y,forward,posx,posy):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(SURFACE_COLOR)
        self.image.set_colorkey(COLOR)

        pygame.draw.rect(self.image,
                         color,
                         pygame.Rect(0, 0, width, height))

        self.rect = self.image.get_rect()
        self.rect.x= x
        self.rect.y=y
        self.forward = forward
        self.posx = posx
        self.posy = posy
    def collide(self):
        if playerCar.rect.colliderect(self.rect) == True:
            movement(self.forward,self.posx,self.posy,True)
class World_collide(pygame.sprite.Sprite):
    def __init__(self, color, height, width,x,y):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(SURFACE_COLOR)
        self.image.set_colorkey(COLOR)

        pygame.draw.rect(self.image,
                         color,
                         pygame.Rect(0, 0, width, height))

        self.rect = self.image.get_rect()
        self.rect.x= x
        self.rect.y=y
    def collide(self,direction):
        if playerCar.rect.colliderect(self.rect) == True:
            if direction == 'x':
                playerCar.rect.x -= 20
            elif direction == 'x-':
                playerCar.rect.x += 20
            elif direction == '-y':
                playerCar.rect.y +=20
            else:
                playerCar.rect.y -= 20

RED = (255, 0, 0)

size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("PYRPG")

all_sprites_list = pygame.sprite.Group()
barriers = pygame.sprite.Group
playerCar = Sprite(RED, 30, 20)
playerCar.rect.x = 200
playerCar.rect.y = 300
one_NPC = Sprite_NPC((0,0,255),30,20,'help needed')
one_NPC.get_quest()
enermy = Sprite_enermy('enermy')
all_sprites_list.add(enermy)
all_sprites_list.add(playerCar)
#all_sprites_list.add(one_NPC)
exit = True
clock = pygame.time.Clock()
screen2 = False
resentdirection = ''
encounter = False,0
imp=''
while exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                exit = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        playerCar.moveLeft(10)
        resentdirection = 'x-'
        encounter=main.B.encounter(False)
    if keys[pygame.K_RIGHT]:
        playerCar.moveRight(10)
        resentdirection = 'x'
        encounter=main.B.encounter(False)
    if keys[pygame.K_DOWN]:
        playerCar.moveForward(10)
        resentdirection = 'y'
        encounter=main.B.encounter(False)
    if keys[pygame.K_UP]:
        playerCar.moveBack(10)
        resentdirection = '-y'
        encounter = main.B.encounter(False)
    if encounter[0] == True:
        battle()
    imp = pygame.image.load(movement('', 0, 0, False))
    mouse = pygame.mouse.get_pos()
    map_collision(current,resentdirection)
    all_sprites_list.update()
    screen.blit(imp, (0, 0))
    one_NPC.collide()
#    print('x{0}'.format(playerCar.rect.x))
#    print('y{0}'.format(playerCar.rect.y))
    all_sprites_list.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()

#x250y10- x330-y10,x350-y110, x330, y460-x250,y460, x250,y270