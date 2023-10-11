import random
import pygame
import main,time,mutagen
from mutagen.wave import WAVE
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





def typing_(string):#later plans for cleaner text
    lst = []
    for letter in string:
        lst.append(letter)
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
        bg=(f'images/battle_bg_{main.M.location}.png') 
        current=bg
        now = True
    elif now == True and encounter[0] == False:
        now = False
        current=previous
        bg=current
        return current
    else:
        first = True
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
        self.font = pygame.font.SysFont('Comic Sans MS',24)
        self.img3 = self.font.render('', True, (224, 3, 23))
        self.img5 = self.font.render('',True,(0,0,255))
    def start_ui(self):
        self.run_texture = Sprite_button_image('images/Run.png',374,381)
        self.runbutton = Sprite_button((0,23,0),35,94,'run',374,381)
        barriers.add(self.runbutton)
        self.fight_texture = Sprite_button_image('images/Fight.png',74,381)
        self.fight_button = Sprite_button((0,0,0),41,97,'fight',74,381)
        barriers.add(self.fight_button)
    def hpbar(self,current,max,length,xx,y):
        try:
            hpratio = length/max
            x = current//hpratio
            pygame.draw.rect(screen,(255,0,0),(xx,y,x,25))
        except:
            return False
    def battle(self):
        global screen,current,encounter,start,starthp,action
        run = False
        er = False
        img4 = self.font.render('^ player HP ^', True, (224, 3, 23))
        screen.blit(img4, (300, 30))
        img = self.font.render('^ enemy HP ^', True, (224,3,23))
        screen.blit(img, (20, 40))
        img2 = self.font.render(f'magic count:{self.magic_count}', True, (224,3,23))
        screen.blit(img2, (20, 60))
        screen.blit(self.img3, (20, 300))
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
                if run == False:
                    self.img5 = self.font.render('you attempted to run but it failed', True, (0, 255, 0))
                    screen.blit(self.img5, (20, 340))
                    pygame.display.flip()
                    time.sleep(2)
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
                pre = encounter[1][0]
                encounter[1][0] = main.B.attack(encounter[1][0],main.C.damage,main.T.crit(main.C.type_,encounter[1][2]),'you')
                self.img3 = self.font.render(f'you did {pre - encounter[1][0]} phyical damage', True, (224, 3, 23))
                screen.blit(self.img3, (20, 300))
                self.fight_mode = False
                self.enermy_turn = True
                self.last = self.fight_command
                time.sleep(1)
            if self.fight_command == 'Attack' and self.last == self.fight_command:
                    self.enermy_turn = True
                    self.fight_mode = False
                    self.held = True
                    self.command = ''
            if self.fight_command == 'heal'and self.last != self.fight_command:
                pre = self.player_hp
                self.player_hp=main.B.heal(self.player_hp,self.magic_count, main.C.magic,'you')
                self.img3 = self.font.render(f'you healed {self.player_hp- pre} hp', True, (224, 3, 23))
                self.fight_mode = False
                self.enermy_turn = True
                if self.magic_count != 0 and self.magic_count >= 2:
                    self.magic_count -= 2
                else:
                    self.img3 = self.font.render('couldnt heal due to lacking 2 magic', True,(224, 3, 23))
                    self.magic_count = self.magic_count
                time.sleep(0.1)
                self.last = self.fight_command
            if self.fight_command == 'heal' and self.last == self.fight_command:
                    self.enermy_turn = True
                    self.fight_mode = False
                    self.held = True
                    self.command = ''
            if self.fight_command == 'magic'and self.last != self.fight_command:
                pre = encounter[1][0]
                encounter[1][0]=main.B.magic_damage(main.B.magic_count, self.magic_count, encounter[1][0], 'you')
                self.img3 = self.font.render(f'you did {pre - encounter[1][0]} magic damage', True, (224, 3, 23))
                self.fight_mode = False
                self.enermy_turn = True
                self.last = self.fight_command
                if self.magic_count !=0 and self.magic_count >= 3:
                    self.magic_count -= 3
                else:
                    self.img3 = self.font.render('couldnt use a magic attack due to lacking 3 magic', True, (224, 3, 23))
                    self.magic_count = self.magic_count
                time.sleep(0.1)
            if self.fight_command == 'magic' and self.last == self.fight_command:
                    self.enermy_turn = True
                    self.fight_mode = False
                    self.held = False
                    self.command = ''
            if self.enermy_turn == True:
                damage = main.B.AI_turn(self.player_hp,main.C.stats()[1],encounter[1][0])
                if damage[0] == 'attack':
                    pre = self.player_hp
                    self.player_hp = damage[1]
                    self.img5 = self.font.render(f'enermy did {pre-damage[1]}damage', True, (0, 0, 225))
                self.enermy_turn = False
                if damage[0]== 'heal':
                    pre = encounter[1][0]
                    encounter[1][0] = damage[1]
                    self.img5 = self.font.render(f'enermy healed {damage[1]-pre} hp', True, (0, 0, 225))
                if damage[0] == 'run':
                    if damage[1] == True:
                        self.img3 = self.font.render('', True, (224, 3, 23))
                        screen.blit(self.img3, (20, 300))
                        self.img5= self.font.render('enermy ran from you', True, (0, 0, 225))
                        screen.blit(self.img5,(20,340))
                        pygame.display.flip()
                        run = True
                        time.sleep(2)
                        er= True
                    else:
                        self.img5 = self.font.render('enermy attempted to run but failed', True, (0, 0, 225))
        screen.blit(self.img5, (20, 340))
        if start == True:
            starthp = encounter[1][0]
            start = False
        self.hpbar(encounter[1][0],starthp,1000,10,10)
        self.hpbar(self.player_hp, main.C.hp, 1000, 300, 10)
        if encounter[1][0] <= 0 or run == True:
            if run == True and er == False:
                self.img5 = self.font.render('you ran from the enermy', True, (0, 255, 0))
                screen.blit(self.img5, (20, 340))
                pygame.display.flip()
                time.sleep(2)
                x = list(encounter)
                x[0] = False
                x[1][0] = starthp
                all_sprites_list.add(playerCar)
            if encounter[1][0] <= 0:
                main.C.xp_gain(encounter[1][3])
                self.img3 = self.font.render('', True, (224, 3, 23))
                screen.blit(self.img3, (20, 300))
                self.img5 = self.font.render(f'you gained {encounter[1][3]} XP', True, (0, 255, 0))
                screen.blit(self.img5, (20, 340))
                pygame.display.flip()
                time.sleep(2)
                self.img5 = self.font.render('', True, (0, 0, 255))
            x = list(encounter)
            x[0] = False
            x[1][0] = starthp
            x[1][7] += 1
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
    quest = Q.activate(current)
    return quest
class Quests:
    def __init__(self):
        self.one_NPC = Sprite_NPC((0, 0, 255), 30, 20, 'help needed',100,200)
        self.steve = Sprite_NPC((7, 34, 9), 30, 20, 'impressive progress',290,150)
    def activate(self,location):
        quest = ''
        if location == 'images/central_plain.png':
            all_sprites_list.add(self.one_NPC)
            quest=self.one_NPC.collide()
            if quest != '' and quest != None:
                quest = Q.quest_handle(quest)
                return quest
            all_sprites_list.add(self.steve)
            quest=self.steve.collide()
            if quest != '' and quest != None:
                quest = Q.quest_handle(quest)
                return quest
        else:
            self.remove_npc()
    def quest_handle(self,quest):
        global quest_set
        x = main.Q.questlist[main.L.precise_location]
        stats=(x[x.index(quest)+1])
        quest_set = True
        return stats,quest
    def set(self,quest):
        x = main.Q.questlist[main.L.precise_location]
        stats=(x[x.index(quest)+1])
        main.Q.set_quest(quest,stats)
    def remove_npc(self):
        all_sprites_list.remove(self.one_NPC)
        all_sprites_list.remove(self.steve)
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
    def __init__(self, color, height, width,questgive,x,y):
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
        self.quest = questgive
    def get_quest(self):
        return self.quest
    def collide(self):
        if playerCar.rect.colliderect(self.rect) == True:
            return self.quest

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
        spite = pygame.image.load(f'images/{enermy}.png')
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

def text_speech(text : str,color,background,x,y, bold : bool):
    SCREEN = width, height = 900, 600
    font = pygame.font.SysFont('Comic Sans MS', 24)
    font.set_bold(bold)
    textSurf = font.render(text, True, color).convert_alpha()
    textSize = textSurf.get_size()
    bubbleSurf = pygame.Surface((textSize[0]*2., textSize[1]*2))
    bubbleRect = bubbleSurf.get_rect()
    bubbleSurf.fill(background)
    bubbleSurf.blit(textSurf, textSurf.get_rect(center = bubbleRect.center))
    bubbleRect.center = (x,y)
    screen.blit(bubbleSurf, bubbleRect)

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

def music():
    global previous_loc
    current_loc=main.M.location
    if current_loc != previous_loc:
        bgm = 'music/{0}.wav'.format(main.M.location)
        pygame.mixer.music.load(bgm)
        pygame.mixer.music.play(-1)
    previous_loc=main.M.location
RED = (255, 0, 0)
size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("PYRPG")
previous_loc = ''
all_sprites_list = pygame.sprite.Group()
barriers = pygame.sprite.Group
playerCar = Sprite(RED, 30, 20)
playerCar.rect.x = 200
playerCar.rect.y = 300
Q= Quests()
all_sprites_list.add(playerCar)
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
quest_set = False
name = ''
xp = 0
hold = False
quest_completed = False
B = Battle()
main.C.xp_gain(700000000000000)
timers=0
while exit:
    timers += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                exit = False
    keys = pygame.key.get_pressed()
    if current != f'images/battle_bg_{main.M.location}.png' and quest_set == False:
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
        if keys[pygame.K_l]:
            text_speech(f'level {main.C.level}', (255, 255, 255), (0, 128, 0), WIDTH / 2, 400, False)
            all_sprites_list.draw(screen)
            pygame.display.flip()
            time.sleep(2)
    imp = pygame.image.load(movement('', 0, 0, False))
    quest = map_collision(current,resentdirection)
    music()
    all_sprites_list.update()
    screen.blit(imp, (0, 0))
    if encounter[0] == True:
        Q.remove_npc()
        enermy = Sprite_enermy(encounter[2])
        encounter = B.battle()
        start = False
        #    print('x{0}'.format(playerCar.rect.x))
        #    print('y{0}'.format(playerCar.rect.y))
        all_sprites_list.draw(screen)
        pygame.display.flip()
        clock.tick(60)
        just_battled = True
    if encounter[0] == False:
        font = pygame.font.SysFont('Comic Sans MS', 24)
        img5 = font.render(f'current quest: {main.Q.questname}', True, (224, 3, 23))
        screen.blit(img5, (20, 10))
    if quest_set == True:
        if quest[0][3] == True:
            text_speech('quest already completed', (255, 255, 255), (0, 128, 0), WIDTH / 2, 400, False)
            all_sprites_list.draw(screen)
            pygame.display.flip()
            time.sleep(1)
            quest_set = False
            playerCar.rect.y -= 10
        if main.Q.questname == quest[1]:
            text_speech('quest already taken', (255, 255, 255), (0, 128, 0), WIDTH / 2, 400, False)
            all_sprites_list.draw(screen)
            pygame.display.flip()
            time.sleep(1)
            quest_set = False
            playerCar.rect.y -= 10
        else:
            text_speech(f'{quest[1]}:{quest[0][6]}', (255, 255, 255), (0, 128, 0), WIDTH/2, 400, False)
            accept_texture = Sprite_button_image('images/Accept.png',374,411)
            acceptbutton = Sprite_button((0,23,0),35,94,'accept',374,411)
            reject_texture = Sprite_button_image('images/reject.png',74,411)
            rejectbutton = Sprite_button((0,0,0),41,97,'reject',74,411)
            y=acceptbutton.collide()
            x=rejectbutton.collide()
            if y != '':
                playerCar.rect.y -= 10
                Q.set(quest[1])
                quest_set = False
            if x != '':
                playerCar.rect.y -= 10
                quest_set = False
        pygame.display.flip()
    else:
        x=main.Q.check_quest()
        if quest_completed == True:
            text_speech(f'quest {name} completed, {xp} xp gained', (255, 255, 255),(0, 128, 0), WIDTH / 2, 400, False)
            all_sprites_list.draw(screen)
            pygame.display.flip()
            time.sleep(2)
            quest_completed = False
        if x == True:
            hold = True
        if x == True and encounter[1] == [] or hold == True and encounter[1]==[]:
            quest_completed = True
            name = main.Q.questname
            if main.Q.currentquest[0] == 'monster':
                xp = main.Q.currentquest[1]
            else:
                xp = main.Q.currentquest[2]
            main.Q.questname = ''
            all_sprites_list.draw(screen)
            pygame.display.flip()
            hold = False
        #    print('x{0}'.format(playerCar.rect.x))
        #    print('y{0}'.format(playerCar.rect.y))
        all_sprites_list.draw(screen)
        pygame.display.flip()
        clock.tick(60)
#if event.type == pygame.MOUSEBUTTONDOWN:
pygame.quit()
