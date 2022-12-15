import random,math,time
print("welcome to max's text based rpg")
#add ability to unlock new areas
#@todo
###fix movement system so it works both ways

class Dungouns:
     def __init__(self):
         self.dungons=['grassland well','castle walls','dark clouds']

class Locations:
    def __init__(self):
        self.map =['plains',['east_plain','north_plain','south_plain','central_plain','west_plain'],'eastern desert',['oasis','small northern town','central desert fortress','hunted wasteland'],'town','deep cave','dark clouds']
        self.precise_location = 'east_plain'
        self.start = True
        self.unlocked = [1,0,0,0,0]
        self.different_provence = False
    def loc(self,local):
        where = self.map.index(local)
        return self.map[where+1]
    def move(self,local):
        self.different_provence = False
      #  if self.start == False:
      #      B.encounter(False)
        self.start = False
        where_to_go_from_here = self.loc(local).index(self.precise_location)
        if where_to_go_from_here == 0:
            findme = self.map.index(M.location) - 1
            if M.location != 'plains':
                choice = self.map[findme][len(self.map[findme])-1],self.loc(local)[where_to_go_from_here+1]
                self.different_provence = True
                return choice
            else:
                choice = self.loc(local)[where_to_go_from_here + 1]
                return choice
        if where_to_go_from_here == len(self.loc(local))-1:
            findme = self.map.index(M.location) + 1
            if self.map != 'dark clouds':
                choice = self.map[findme][len(self.map[findme])-2],self.map[findme+2][0]
                self.different_provence = True
                return choice
            else:
                choice = self.loc(local)[where_to_go_from_here + 1]
                return choice
        elif where_to_go_from_here == len(self.loc(local)) or where_to_go_from_here == len(self.loc(local))-1:
            choice = self.loc(local)[where_to_go_from_here - 1]
        else:
            choice = self.loc(local)[where_to_go_from_here - 1],self.loc(local)[where_to_go_from_here + 1]
        return choice
#def spescial_location(self):

#    def new_unlock(self):

class Quest:
    def __init__(self):
        self.questlist = {'central plain':['impressive progress',['place','west plain',40,False,False,False,'move to the west plain'],'help needed',['monster',120,False,False,False,'plains','kill 4 thiefs','thief',4]],'west plain':['a new world',['level',10,100,False,True,False,'des']]}
        self.questname =''
        self.currentquest = []
        self.quest_set = False
        self.currentquestlocaton = ''
    def set_quest(self,quest,details):
        self.currentquest = details
        self.questname = quest
        self.quest_set = True
        self.currentquestlocaton = L.precise_location
    def finish_quest(self):
        self.quest_set = False
        C.xp_gain(self.currentquest[2])
        self.currentquest[3] = True
        self.questlist[self.currentquestlocaton][self.questlist[self.currentquestlocaton].index(self.currentquest)] = self.currentquest
        if self.currentquest[4] == True:
            findlocatoion = L.map.index(M.location)
            L.unlocked[findlocatoion+1] = 1
    def update_quest(self):
        self.stuff=3
    def check_quest(self):
        if self.quest_set == True:
            if self.currentquest[0]=='place':
                if L.precise_location == self.currentquest[1]: 
                    print('you finished the quest {0}'.format(self.questname))
                    self.currentquest[3] = True
                    self.finish_quest()
            elif self.currentquest[0]=='monster':
                if B.enermy[self.currentquest[5]][self.currentquest[7]][7] >= self.currentquest[8]:
                    print('you finished the quest {0}'.format(self.questname))
                    self.currentquest[5] = True
                    self.finish_quest()
            elif self.currentquest[0]=='level':
                if C.stats()[8] == self.currentquest[1]:
                    print('you finished the quest {0}'.format(self.questname))
                    self.currentquest[5] = True
                    self.finish_quest()

    def start_quest(self):
        try:
            name = []
            details = []
            avliable = []
            choices = list(self.questlist[L.precise_location])
            for i in range(len(choices)):
                if (i % 2) == 0:
                    name.append(choices[i])
                else:
                    details.append(choices[i])
            for i in range(len(name)):
                if details[i][3] == False:
                    avliable.append(name[i])
            print('---currently available quests---')
            for i in range(len(avliable)):
                print('{0}:{1}'.format(avliable[i],details[i][6]))
            questogofor = input('which quest do you want to embark on')
            if questogofor in avliable:
                self.set_quest(questogofor,details[name.index(questogofor)])
            else:
                print('sorry thar quest doesnt exist')

        except:
            print('there is no quests here')
class Battle:
    def __init__(self):
        self.enermy = {'plains':{'agressive plant':[200,5,T.type_ele(2),20,1,4,1,0],'thief':[300,2,T.type_ele(2),30,4,1,1,0]},'eastern desert':{'awakened sand':[150,10,T.type_ele(2),40,3,7,10,0]}}
        self.encounters = {'plains': 0.02,'eastern desert': 0.04,'dark clouds':0.06,'town': 0.03,'deep cave':0.05}
        self.enermy_hp = 0
        self.enermy_type_ = 0
        self.enermy_damage = 0
        self.enermy_xp = 0
        self.numdefeted = 0
    def encounter(self,searched):
        find = self.encounters[M.location] + random.random()
        if find >= 1 or searched == True:
            oppnent = random.choice(list(self.enermy[M.location]))
            stats =self.enermy[M.location][oppnent]
            self.enermy_hp = stats[0]
            self.enermy_type_ = stats[2]
            self.enermy_damage = stats[1]
            self.enermy_xp = stats[3]
            self.focus = stats[4]
            self.magic = stats[5]
            self.magic_count = stats[6]
            print('you have encountered a enermy {0}'.format(oppnent))
            return True,stats
        return False,[]
    def fight(self,stats,oppnent):
        hp = C.stats()[0]
        p_type_ = C.stats()[1]
        damage = C.stats()[2]
        xp = C.stats()[4]
        magic = C.stats()[5]
        no_xp = False
        magic_count = C.stats()[7]
        p_run = False
        print('{0}'.format(self.enermy_hp))
        modifier = T.crit(p_type_,self.enermy_type_) 
        while self.enermy_hp >= 1 and hp >= 1:
            turn = input('what do you want to do 1 = attack 2 = heal 3 = magic attack 4 = run')
            magic_count = magic_count + 1
            print('you have {0} magic'.format(magic_count))
            if turn == '1':
                self.enermy_hp = self.enermy_hp - (damage * modifier)
                print('you did {0} damage.enermy has {1} health left'.format((damage * modifier),self.enermy_hp))
            if turn == '2':
                if magic_count >= 2:
                    hp = hp + (magic * 2)
                    magic_count = magic_count - 2
                    print('you healed {0} damage.you have {1} health left'.format((magic * 2), hp))
            if turn == '3':
                if magic_count >= 3:
                    self.enermy_hp =self.enermy_hp - (magic * 2)
                    magic_count = magic_count - 3
                    print('you did {0} damage.enermy has {1} health left'.format((magic * 2), self.enermy_hp))
            if turn == '4':
                p_run = True
                run = random.randint(1,5)
                if run == 4:
                    self.enermy_hp = 0
                    no_xp = True
                    print('you were able to get away')
                else:
                    print('you tried to run but werent able to')
            choice = random.randint(1,7)
            if self.focus == 1 and choice in [5,6,7] or choice == 1:
                attack = (self.enermy_damage * T.crit(self.enermy_type_, p_type_))
                hp = hp- attack
                print('the enermy did {0} damage.you have {1} health left'.format(attack, hp))
            if self.focus == 2 and choice in [5,6,7] or choice == 2 or self.enermy_hp <= (self.enermy_hp / 4) and self.magic_count >= 2:
                if self.magic_count >= 2:
                    self.enermy_hp = self.enermy_hp+  self.magic * 2
                    self.magic_count =self.magic_count- 2
                    print('the enermy healed for {0} .it now has {1} health left'.format((self.magic * 2), self.enermy_hp))
            if self.focus == 3 and choice in [5,6,7] or choice == 3:
                if self.magic_count >= 3:
                    hp =hp - self.magic * 2
                    self.magic_count =self.magic_count- 3
                    print('you did {0} damage.enermy has {1} health left'.format((magic * 2), self.enermy_hp))
            if self.focus == 4 and choice in [5,6,7] or choice == 4:
                run = random.randint(1,5)
                if run == 4 or p_run == True:
                    self.enermy_hp = 0
                    no_xp = True
                    print('the enermy ran from you')
                else:
                    print('the enrmy tried to run but you caught them')
        if no_xp == True:
            M.start(),
        elif hp != 0:
            stats[7] += 1
            print(stats[7])
            self.enermy[M.location][oppnent]=stats
            C.xp_gain(self.enermy_xp)
        else:
            print('you died')
            return None
class Main:
    def __init__(self):
        self.char = C.stats()
        self.location = 'plains'
        self.start_up = True
        self.stay = False
    def start(self):
        if self.start_up == True:
            print('you start with the charater of alice')
            print(random.choice(self.char[3]))
            self.start_up = False
        go = True
        while go:
            action = input('what do you want to do: 1:move 2:look for quests 3:hunt for enermys')
            Q.check_quest()
            if action == '1':
                self.moving()
            elif action == '2':
                Q.start_quest()
            elif action =='3':
                B.encounter(True)

    def moving(self):
            choices = L.move(self.location)
            if len(choices[0]) != 1:
                for i in range(len(choices)):
                    print(choices[i])
            else:
                print(choices)
            move = input('where do you want to move? ')
            if move in choices and move != '':
                if L.different_provence == True:#needs fixing to enable you to move backwards even if area isnt unlocked
                    check = L.loc(self.location)
                    for i in range(len(check)):
                        if check[i] == move:
                            self.stay = True
                    if self.stay == True:
                            L.precise_location = move
                            self.stay = False
                    else:
                        if move == choices[0]:
                            self.location = L.map[(L.map.index(self.location))-2]
                            L.precise_location = move
                            M.movement(move)
                        elif L.unlocked[(L.map.index(self.location))+1] == 1:
                            self.location = L.map[(L.map.index(self.location))+2]
                            L.precise_location = move
                            M.movement(move)
                        else:
                            print('cant get there')
                else:
                    L.precise_location = move
                    M.movement(move)
            else:
                print('cant get there')

    def movement(self,move):
        if move == 'hunted wasteland':
            sure = input('are you sure you want to go into the wasteland-it is highly dangerous and difficult to leave-type_ yes to agree to go into the wasteland')
            if sure == 'yes':
                L.precise_location = move
            else:
                return
        L.precise_location = move
class Charaters:
     def __init__(self):
         self.inventory_slots=20
         self.charater_selected=1
         self.unlocked=1
         self.hp = 300
         self.type_ = T.type_ele(5)
         self.damage= 20
         self.next_xp = 30
         self.magic = 3
         self.levelup_mod = [1.05,1.07,1.03,1.01]
         self.level = 1
         self.magic_amount = 3
         self.welcome = ['hello there I am glad to see you','how long will it take for you to get to the dark clouds?']
     def char_unlocked(self):
         if self.unlocked == 1:
             random.choice(self.welcome)
     def stats(self):
         return self.hp,self.type_,self.damage,self.welcome,self.next_xp,self.magic,self.levelup_mod,self.magic_amount,self.level
     def xp_gain(self,xp_gained):
         xp_needed = self.next_xp
         while xp_gained != 0 and xp_gained >= 0:
             xp_gained = xp_gained - xp_needed
             if xp_gained != 0 and xp_gained >= 0:
                 C.level_up()
         self.next_xp = xp_needed + xp_gained
         print(self.next_xp)
     def level_up(self):
         self.hp *= self.levelup_mod[0]
         self.damage *= self.levelup_mod[1]
         self.magic *= self.levelup_mod[2]
         self.magic_amount *= self.levelup_mod[3]
         self.next_xp *= 2
         self.level += 1
         print('you leved up to level {0}'.format(self.level))
class type_s():
    def __init__(self):
        self.type_s=['fire','water','earth','wind','dark','light','god']
        self.effective = {'fire': {'earth': 2.0,'water': 0.5,'fire': 1.0,'wind':1.0,'dark':1.0,'light':1.0,'god': 0.9}, 'water': {'fire': 2.0, 'dark': 0.5,'water':1.0,'earth':1.0,'wind':1.0,'light':1.0,'god': 0.9 },'earth': {'wind': 2.0, 'dark': 0.5,'fire': 1.0,'water':1.0,'god': 0.9,'earth':1.0,'light':1.0},'wind':{'fire': 2.0,'god': 0.9,'light': 0.5,'water':1.0,'earth':1.0,'dark':1.0},'dark':{'earth': 2.0,'wind': 0.5,'fire': 1.0,'water':1.0,'dark':1.0,'light':1.0,'god': 0.9},'light':{'dark': 2.0, 'fire': 0.5,'water':1.0,'earth':1.0,'wind':1.0,'light':1.0,'god': 0.9},'god':{'fire': 3.0,'water':3.0,'earth':3.0,'wind':3.0,'dark':3.0,'light':3.0,'god': 1.0}}
    def type_ele(self,element):
        int(element)
        return self.type_s[element]
    def crit(self,type__att,type__def):
        critical = self.effective[type__att][type__def]
        return critical
T = type_s()
C = Charaters()
D = Dungouns()
M = Main()
L = Locations()
B = Battle()
Q = Quest()


