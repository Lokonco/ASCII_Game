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
key = False         # contributes to progress being made
fight = False
standing = True
boss = False
############ Variables ###################
HP = 50
maxHP = HP
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
e_list = ['Goblin', 'Feral Wild Child', 'Sad Wizard',]    # add more mobs
b_list = ['Erlick the Grand Wizard']
mobs = {
    'Goblin': {
        'Hp': 15,
        'Atk': 3,
        'Gold': 8,
    },
    'Feral Wild Child': {
        'Hp': 10,
        'Atk': 3,
        'Gold': 5,
    },
    'Sad Wizard': {
        'Hp':30,
        'Atk':10,
        'Gold':15,
    },
    'Erlick the Grand Wizard': {
        'Hp': 100,
        'Atk': 20,
        'Gold':50
    }
}










################################ Save loop ###########################
def save():
    list = [
        name,
        str(HP),
        str(ATK),
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
########### HEAL Function #########
def heal(amount):
    global HP
    if HP + amount < maxHP:
        HP += amount
    else:
        HP = maxHP
    print(name + 's HP restored to ' + str(HP) + '!')

##############Battle Function #####################
def battle():
    global fight, play, run, HP, ATK, pot, elix, gold, boss
    if not boss:
        enemy = random.choice(e_list)
    else:
        enemy = random.choice(b_list)
    Hp = mobs[enemy]['Hp']
    hpmax = Hp
    atk = mobs[enemy]['Atk']
    g = mobs[enemy]['Gold']

    while fight:
        clear()
        draw()
        print('Defeat the ' + enemy + '!')
        draw()
        print(name + "s Hp: " + str(HP) + '/' + str(maxHP))
        print(enemy + "'s Hp: " + str(Hp) + '/' + str(hpmax))
        print('Potions: ' + str(pot))
        print('Elixer: ' + str(elix))
        draw()
        print('1- Attack')
        if pot > 0:
            print('2 - Use Potion (30Hp)')
        if elix > 0:
            print('3 - Use Elixer (50Hp)')
        draw()
        choice = '# '

        if choice == '1':
            Hp -= ATK
            print(name + ' Dealt ' + str(ATK) + ' damage to the ' + enemy + '.')
            if Hp > 0:
                HP -= atk
                print(enemy + ' Dealt ' + str(atk) + ' damage to the ' + name + '.')
            input('> ')

        elif choice == '2':
            if pot > 0:
                pot -= 1
                heal(30)
                HP -= ATK
                print(enemy + ' Dealt ' + str(atk) + ' damage to ' + name + '.')
            else:
                print('No Potions!!!')
                input('> ')

        elif choice == '3':
            if elix > 0:
                elix -= 1
                heal(50)
                HP -= atk
                print(enemy + ' Dealt ' + str(atk) + ' damage to the ' + name + '.')
            else:
                print('No Elixers!!!')
                input('> ')


        if HP <= 0:
            print(enemy + 'Defeated' + name)
            draw()
            fight = False
            play = False
            run = False
            print('GAME OVER BOZO')
            input('> ')

        if Hp <= 0:
            print(name + 'Defeated the ' + enemy)
            draw()
            fight = False
            gold += g
            print("You've found " + str(g) + ' Gold! ')
            if random.randint(0, 100) < 30:
                pot += 1
                print("You've found a Potion!!")
            if enemy == 'Erlick the Grand Wizard':
                draw()
                print('Congrats on defeating Erlick, Yet Your journey is far from over!')
                boss = False
                play = False
                run = False
            input('>')
            clear()




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
            name = input(' Whats your name stranger? ')
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
                if random.randint(0, 100) <= 40:
                    fight = True
                    battle()

        if play:
            draw()
            print('Location: ' + biom[map[y][x]]['t'])
            print('Xx--------------Stats---------------xX')
            print('Name: ' + name)
            print('Health: ' + str(HP) + '/' + str(maxHP))
            print('Potions: ' + str(pot))
            print('Elixers: ' + str(elix))                      # display more stats in future
            print('Gold: ' + str(gold))
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
            standing = False
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
#############################
        else:
            standing = True