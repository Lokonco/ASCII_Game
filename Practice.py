
import os, random
def clear():       #clear screen function after input
    os.system('cls')
###################################
def draw():        # line drawing function to seperate
    print('Xx--------------------------------xX')
##########################
# bools
run = True
menu = True
play = False
rules = False
key = False
fight = False
standing = True
boss = False
buy = False
speak = False

############ Variables ###################
HP = 50
maxhp = HP
ATK = 3
pot = 1                 #add armor and other stats
elix = 0
gold = 0
x = 0
y = 0
##################### Map ##############################
        # X - 0                                             X - 5
map = [['forest', 'forest', 'forest', 'shack', 'forest', 'mountain'], # Y - 0
        ['forest', 'shack', 'forest', 'plain', 'forest', 'cave'],
        ['forest', 'forest', 'shop', 'mayor', 'forest', 'mountain'],
        ['plain', 'bridge', 'town', 'shack', 'forest', 'shack'],
        ['plain', 'forest', 'forest', 'forest', 'plain', 'mountain'],
        ['forest', 'forest', 'shack', 'forest', 'mountain', 'mountain']] #y - 5
y_len = len(map)-1
x_len = len(map[0])-1

biom = {
    'forest': {
        't': 'FOREST',
        'e': True},
    'plain': {
        't': 'PLAINS',
        'e': False},
    'bridge': {
        't': 'BRIDGE',
        'e': True},
    'town': {
        't': 'TOWN',
        'e': False},
    'shop': {
        't': 'SHOP',
        'e': False},
    'shack': {
        't': 'SHACK',
        'e': False},
    'cave': {
        't': 'CAVE',
        'e': True},
    'mountain': {
        't': 'MOUNTAIN',
        'e': False},
    'mayor': {
        't': 'MAYOR',
        'e': False,
        }
    }
####################### Enemy List ###################################
e_list = ['Goblin', 'Feral Wild Child', 'Sad Wizard']    # add more mobs

mobs = {
    'Goblin': {
        'Hp': 15,
        'Atk': 3,
        'Go': 8,
    },
    'Feral Wild Child': {
        'Hp': 10,
        'Atk': 3,
        'Go': 5,
    },
    'Sad Wizard': {
        'Hp':30,
        'Atk':10,
        'Go':15,
    },
    'Erlick the Grand Wizard': {
        'Hp': 50,
        'Atk': 25,
        'Go': 100
    }
}


######### Heal Func ############3##
def heal(amount):
    global HP
    if HP + amount < maxhp:
        HP += amount
    else: HP = maxhp
    print(name + 'has restored Hp!')
#################### Shop ##################################
def shop():
    global buy, gold, pot, elix, ATK
    while buy:
        clear()
        draw()
        print('Welcome to the shop!')
        draw()
        print('Gold: ' + str(gold))
        print('Potions ' + str(pot))
        print('Elixers ' + str(elix))
        draw()
        print('1 - Buy potion - 5 Gold ')
        print('2 - Buy Elixer - 8 Gold ')
        print('3 - Upgrade Weapon (+2 ATK) - 15 Gold ')
        print('4 - Leave Shop ')

        if choice == '1':
            if gold >= 5:
                gold -= 5
                pot += 1
                print('Potion Purchased')
            else:
                print('Not enough funds')
        elif choice =='2':
            if gold >= 8:
                gold -= 8
                elix += 1
                print('Elixer purchased')
            else:
                print('Not enough funds')
        elif choice == '3':
            if gold >= 15:
                gold -= 15
                ATK += 2
                print('Weapon Upgraded!!')
            else:
                print('Not enough Funds')
        elif choice == '4':
            print('Thank you for shopping!')


################################ Save loop ###########################
def save():
    list = [
        name,
        str(HP),
        str(ATK),
        str(pot),
        str(elix),
        str(pot),
        str(elix),
        str(gold),
        str(x),
        str(y),
        str(key)
    ]
    f = open('load.txt', 'w')

    for item in list:
        f.write(item + '\n')
    f.close()
############## Mayor ######################
def mayor():
    pass
############### Cave ###################
def cave():
    pass
#####################

def battle():
    global fight, play, run, HP, pot, elix, gold, boss

    if not boss:
        enemy = random.choice(e_list)
    else:
        enemy = 'Erlick the Grand Wizard' # add more boss's im the future
    Hp = mobs[enemy]['Hp']
    Atk = mobs[enemy]['Atk']
    g = mobs[enemy]['Go']

    while fight:
        clear()
        draw()
        print('Defeat the ' + enemy)
        draw()
        print(enemy + "'s HP: " + str(Hp) + "/" + str(maxhp))
        print(name + "'s HP: " + str(HP) + "/" + str(maxhp))
        print("POTIONS: " + str(pot))
        print("ELIXIR: " + str(elix))
        draw()
        print("1 - ATTACK")
        if pot > 0:
            print("2 - USE POTION (30HP)")
        if elix > 0:
            print("3 - USE ELIXIR (50HP)")
        draw()

        choice = input("# ")

        if choice == '1':
            Hp -= ATK
            print(name + ' dealt ' + str(ATK) + ' damage to ' + enemy)
            if Hp > 0:
                HP -= Atk
                print(enemy + ' dealt ' + str(Atk) + ' to ' + name)
            input('> ')
        elif choice == '2':
            if pot > 0:
                heal(30)
                pot -= 1
            if pot <= 0:
                print('No Potions')
            # can add else statement to have enemy do dmg right after

        elif choice == '3':
            if elix > 0:
                heal(50)
                elix -= 1
            if elix <= 0:
                print('No Elixers')

        if Hp <= 0:
            print(name + 'Defeated ' + enemy)
            draw()
            fight = False
            gold += g
            if random.randint(0,100) <= 15:
                pot += 1
            elif random.randint(0,100) <=5:
                elix += 1

        elif HP <= 0:
            print(name + 'was Defeated by ' + enemy)
            draw()
            fight = False
            play = False
            run = False
            print('GAME OVER')
            input('> ')

############################################
while run:
    while menu:
        clear()
        draw()
        print('1. New Game')
        print('2. Load Game')
        print('3. Rules')
        print('4. Quit Game')
        draw()
        if rules:
            print('These are the rules do not break them')    # immplement funny rules
            rules = False
            choice = ''
            input('> ')
        else:
            choice = input('>')

        if choice == '1':
            clear()
            name = input('Whats your name stranger? ')
            menu = False
            play = True
        elif choice == '2':
            try:
                f = open('load.txt', 'r')
                load_list = f.readlines()
                if len(load_list) == 9:
                    name = (load_list[0][:-1])
                    HP = int(load_list[1][:-1])
                    ATK = int(load_list[2][:-1])
                    pot = int(load_list[3][:-1])
                    elix = int(load_list[4][:-1])
                    gold = int(load_list[5][:-1])
                    x = int(load_list[6][:-1])
                    y = int(load_list[7][:-1])
                    key = bool(load_list[8][:-1])
                    clear()
                    print('Welcome back ' + name + ' GoodLuck')  #add loop to make name comeback as capital first letter
                    input('> ')
                    menu = False
                    play = True
                else:
                    print('Somethings wrong with your file...RIP')
                    input('> ')


            except OSError:
                print('NO SUCH FILE EXIST!!! ')
                input('> ')
        elif choice == '3':
            rules = True
        elif choice == '4':
            quit()
        elif choice == '5':
            print('Why did you press 5 Dummy')
        elif choice == '420':
            pass       #Add easter egg for when 420 is typed




    while play:
        save()   #auto save function
        clear()

        if not standing:
            if biom[map[y][x]]['e']:
                if random.randint(0,100) <= 30:
                    fight = True
                    battle()
        if play:
            draw()
            print('Location: ' + biom[map[y][x]]['t'])
            print('Xx--------------Stats---------------xX')
            print('Name: ' + name)
            print('Health: ' + str(HP) + '/' + str(maxhp))
            print('Potions: ' + str(pot))
            print('Elixers: ' + str(elix))                      # display more stats in future
            print('Gold: ' + str(gold))
            if pot > 0:
                print('5 - Use Potion (30Hp)')
            if elix > 0:
                print('6 - Use Elixer (50Hp)')
            if map[y][x] == 'shop' or map[y][x] == 'Mayor' or map[y][x] == 'cave':
                print('7 - Enter')
            print('Xx------------Movement------------xX')
            print('1 - North')
            print('2 - East')
            print('3 - South')
            print('4 - West')

            draw()
            print('0 - Save and Quit')


            dest = input('> ')
    ############# Map Movement ( open borders )#######################
            if dest == '0':
                play = False
                menu = True
                save()
            elif dest == '1':
                standing =False
                if y > 0:
                     y -= 1
                else: y = y_len
            elif dest == '2':
                standing = False
                if x < x_len:
                    x += 1
                else: x = 0
            elif dest == '3':
                standing = False
                if y < y_len:
                    y += 1
                else: y = 0
            elif dest == '4':
                standing = False
                if x > 0:
                    x -= 1
                else: x = x_len
            elif dest == '5':
                if pot > 0:
                    pot -= 1
                    heal(30)
                else:
                    print('No Potions')
                input('> ')
            elif dest == '6':
                if elix > 0:
                    elix -= 1
                    heal(50)
                else:
                    print('No Potions')
                input('> ')
            elif dest == '7':
                if map[y][x] == 'shop':
                    buy =True
                if map[y][x] == 'Mayor':
                    speak = True
                if map[y][x] == 'cave':
                    boss = True
            else:
                standing = True