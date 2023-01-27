import random
import pygame
import main,time
# Global Variables
COLOR = (255, 100, 98)
SURFACE_COLOR = (167, 255, 100)
WIDTH = 500
HEIGHT = 500
current="images/east_plain.png"
previous =''
now = False
old = ''
first=False
#((main.L.loc(main.M.location).index(main.L.precise_location))) + 2 ==len(main.L.loc(main.M.location)) and  main.L.unlocked[(main.L.map.index(main.M.location)) + 1] != 1:
#checking if the area is enabled or not
def movement(direction,nx,ny,move):
    global current,encounter,previous,now,old,bg,first
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
        if first == True:
            old = current
            previous = current
            first = False
        bg=('images/battle_bg.png')
        current=bg
        now = True
    elif now == True and encounter[0] == False:
        now = False
        current=previous
        bg=current
        return current
    else:
        first = True
        print(current)
        return current
    return bg
class Battle:#finish class
    def __init__(self):
        self.x, self.y = pygame.mouse.get_pos()
        self.run_texture = 0
        self.runbutton = 0
        self.fight_texture = 0
        self.fight_button = 0
        self.command = ''
        self.fight_mode = False
        self.magic_button = 0
        self.magic_texture = 0
        self.fight_command = ''
        self.player_hp = main.C.hp
        self.enermy_turn = False
        self.last = ''
        self.held = False
        self.magic_count = 0
        print('s')
    def start_ui(self):
        self.run_texture = Sprite_button_image('images/Run.png',374,381)
        self.runbutton = Sprite_button((0,23,0),35,94,'run',374,381)
        barriers.add(self.runbutton)
        self.fight_texture = Sprite_button_image('images/Fight.png',74,381)
        self.fight_button = Sprite_button((0,0,0),41,97,'fight',74,381)
        barriers.add(self.fight_button)
    def hpbar(self,current,max,length):
        hpratio = length/max
        x = current//hpratio
        pygame.draw.rect(screen,(255,0,0),(10,10,x,25))
    def battle(self):
        global screen,current,encounter,start,starthp,action
        run = False
        if self.command == '':
            self.last = ''
            self.start_ui()
        all_sprites_list.remove(playerCar)
        if self.fight_mode == False:
            self.command=self.fight_button.collide()
            if self.command == '':
                self.command=self.runbutton.collide()
            if self.command != 'run' and self.command != '':
                self.magic_count += 1
                self.fight_UI(action,self.command)
                time.sleep(0.3)
            if self.command == 'run':
                run = main.B.run()
        else:
            if self.held == True:
                self.held = False
                time.sleep(0.1)
                return encounter
            self.fight_UI(action,self.command)
            self.fight_command = self.fight_button.collide()
            if self.fight_command == '':
                self.fight_command = self.runbutton.collide()
            if self.fight_command == '':
                self.fight_command = self.magic_button.collide()
            if self.fight_command == 'Attack' and self.last != self.fight_command:
                encounter[1][0] = main.B.attack(encounter[1][0],main.C.damage,main.T.crit(main.C.type_,encounter[1][2]),'you')
                self.fight_mode = False
                self.enermy_turn = True
                self.last = self.fight_command
                time.sleep(0.1)
            if self.fight_command == 'Attack' and self.last == self.fight_command:
                    self.enermy_turn = True
                    self.fight_mode = False
                    self.held = True
                    self.command = ''
            if self.fight_command == 'heal'and self.last != self.fight_command:
                self.player_hp=main.B.heal(self.player_hp,self.magic_count, main.C.magic,'you')
                self.fight_mode = False
                self.enermy_turn = True
                time.sleep(0.1)
                self.last = self.fight_command
            if self.fight_command == 'heal' and self.last == self.fight_command:
                    self.enermy_turn = True
                    self.fight_mode = False
                    self.held = True
                    self.command = ''
            if self.fight_command == 'magic'and self.last != self.fight_command:
                encounter[1][0]=main.B.magic_damage(main.B.magic_count, self.magic_count, encounter[1][0], 'you')
                self.fight_mode = False
                self.enermy_turn = True
                self.last = self.fight_command
                print(self.enermy_turn)
                time.sleep(0.1)
            if self.fight_command == 'magic' and self.last == self.fight_command:
                    self.enermy_turn = True
                    self.fight_mode = False
                    self.held = False
                    self.command = ''
            print(self.enermy_turn)
            if self.enermy_turn == True:
                damage = main.B.AI_turn(main.C.stats()[0],main.C.stats()[1])
                print(damage)
                if damage[0] == 'attack':
                    self.player_hp -= damage[1]
                self.enermy_turn = False
                if damage[0]== 'heal':
                    encounter[1][0] += damage[1]
        if start == True:
            starthp = encounter[1][0]
        self.hpbar(encounter[1][0],starthp,1000)
        if encounter[1][0] <= 0 or run == True:
            x = list(encounter)
            x[0] = False
            x[1][0] = starthp
            all_sprites_list.add(playerCar)
            return x
        return encounter
    def fight_UI(self,action,buttons):
        self.run_texture = Sprite_button_image('images/Attack.png',374,381)
        self.runbutton = Sprite_button((0,23,0),35,94,'Attack',374,381)
        barriers.add(self.runbutton)
        self.fight_texture = Sprite_button_image('images/Heal.png',74,381)
        self.fight_button = Sprite_button((0,0,0),41,97,'heal',74,381)
        barriers.add(self.fight_button)
        self.magic_texture = Sprite_button_image('images/magic.png',220,381)
        self.magic_button = Sprite_button((0,0,0),41,97,'magic',220,381)
        barriers.add(self.magic_button)
        self.fight_mode = True
        return True

def map_collision(current,dire):
    if current == 'images/east_plain.png':
        tela1 = telaport((0,0,0),1,500,0,0,'forward',playerCar.rect.x,470)
        barriers.add(tela1)
        tela1.collide()
    if current == 'images/south_plain.png':
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
        self.quest = questgive
    def get_quest(self):
        print(self.quest)
    def collide(self):
        if playerCar.rect.x == self.rect.x and playerCar.rect.y == self.rect.y:
            print(self.quest)

class Sprite_button(pygame.sprite.Sprite):
    def __init__(self, color, height, width,functons,x,y):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(SURFACE_COLOR)
        self.image.set_colorkey(COLOR)

        pygame.draw.rect(self.image,
                         color,
                         pygame.Rect(0, 0, width, height))
        self.width = width
        self.rect = self.image.get_rect()
        self.function = functons
        self.mouse = pygame.mouse.get_pos()
        self.rect.x = x
        self.rect.y = y
    def collide(self):
        if (self.mouse[0] >= self.rect.x and self.mouse[0] <= self.rect.x+self.width) and (self.mouse[1] >= self.rect.y and self.mouse[1] <= self.rect.y+self.width) and pygame.mouse.get_pressed()[0] == True:
            return self.function
        return ''
class Sprite_enermy(pygame.sprite.Sprite):
    def __init__(self, enermy):
        super().__init__()
        spite = pygame.image.load('images/enermy.png')
        screen.blit(spite,(250,250))
class Sprite_button_image(pygame.sprite.Sprite):
    def __init__(self, button_image,x,y):
        super().__init__()
        global current
        spite = pygame.image.load(button_image)
        screen.blit(spite,(x,y))
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
all_sprites_list.add(playerCar)
#all_sprites_list.add(one_NPC)
exit = True
clock = pygame.time.Clock()
screen2 = False
resentdirection = ''
encounter = False,0
imp=''
start = True
starthp=3
action = ''
fiorrun = False
B = Battle()
while exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                exit = False

    keys = pygame.key.get_pressed()
    if current != 'images/battle_bg.png':
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
        if keys[pygame.K_m]:
            time.sleep(1)
            imp = pygame.image.load(f'images/{main.M.location}_map.png')
            screen.blit(imp,(0,0))
            all_sprites_list.draw(screen)
            pygame.display.flip()
            time.sleep(10)
            #something for future, put player sprite on the section of the map they are in
            if keys[pygame.K_m] == True:
                imp = pygame.image.load(movement('', 0, 0, False))
            else:
                time.sleep(2)
    imp = pygame.image.load(movement('', 0, 0, False))
    map_collision(current,resentdirection)
    all_sprites_list.update()
    screen.blit(imp, (0, 0))
    if encounter[0] == True:
        enermy = Sprite_enermy('theif')
        encounter = B.battle()
        start = False
        one_NPC.collide()
        #    print('x{0}'.format(playerCar.rect.x))
        #    print('y{0}'.format(playerCar.rect.y))
        all_sprites_list.draw(screen)
        pygame.display.flip()
        clock.tick(60)
    else:
        start=True
        one_NPC.collide()
        #    print('x{0}'.format(playerCar.rect.x))
        #    print('y{0}'.format(playerCar.rect.y))
        all_sprites_list.draw(screen)
        pygame.display.flip()
        clock.tick(60)
#if event.type == pygame.MOUSEBUTTONDOWN:
pygame.quit()
