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
        ['forest', 'shack', 'forest', 'plain', 'forest', 'cave'],                   #issue in code only displaying forest and plains FIX THIS
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
################### Battle Function ###########################
def battle():
    pass
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


        draw()
        print('Location: ' + biom[map[y][x]]['t'])
        print('Xx--------------Stats---------------xX')
        print('Name: ' + name)
        print('Health: ' + str(HP) + '/' + str(maxhp))
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


        dest = input('# ')
############# Map Movement ( open borders )#######################
        if dest == '0':
            play = False
            menu = True
            save()
        elif dest == '1':
            if y > 0:
                 y -= 1
            else: y = y_len
        elif dest == '2:':
            pass
        elif dest == '3':
            if y < y_len:
                y += 1
            else: y = 0
        elif dest == '4':
            if x > 0:
                x -= 1
#############################
