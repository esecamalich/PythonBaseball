# Baseball Game
# By: Sergio Camalich
# Website: www.camali.ch

# Import modules
import sys
import random
import time

# Playing?
playing = 'y'

# Agreements
yes = ('y','yes')
no = ('n', 'no')

loses = 0
ties = 0

# Throws
strikes = 0
balls = 0
fouls = True

# Pitches
pitches = 0

# Hits
hits = ('catch', 'single', 'double', 'triple', 'homerun')
options = ('strike', 'ball', 'foul', 'hit', 'miss')

# Runs
position = 0
runs = 0

# Outs
outs = 0

# Are we playing?
def Play():

    global playing
    global yes
    global no

    # YES WE ARE
    while playing in yes:

        # Swing
        Swing()

        # Play Again?
        PlayAgain()

def Swing():

    global options

    human = input('Press \'enter\' to swing or write \'q\' and enter to quit: ')

    if human == 'q':
        print ('\nThanks for playing!')
        sys.exit()

    global playing
    global strikes
    global balls

    while strikes < 3 or balls < 4:

        # Random choice
        batter = random.choice(options)
        pitcher = random.choice(options)

        if batter != pitcher:
            # That's a strike!
            if batter == options[0]:
                Strike()
            # That's a ball!
            elif batter == options[1]:
                Ball()
            # That's a foul!
            elif batter == options[2]:
                Foul()
            # That's a hit!
            elif batter == options[3]:
                Hit()
            # That's a miss!
            elif batter == options[4]:
                Miss()
        # THAT'S A HOOOOOOOOOOOMMMMMMMMEEEEEE RUUUUUUNNNN!!!!!!!
        elif batter == pitcher:
            HomeRun()

        if strikes == 3:
            Out()
        elif balls == 4:
            print ('\nBASEBALL!\n')

        # Strikes/Balls Status
        Count()
        
        PlayAgain()

# What is Strike()?
def Strike():

    print ('\nThats:')

    global strikes

    while strikes <= 3:

        # This is a strike
        strikes += 1

        # Indeed it is...
        print ('STRIKE ', strikes, '!\n', sep='')

        # Strike 3!
        if strikes == 3:
            Out()

        Count()

        Swing()

# What is Ball()?
def Ball():

    print ('\nThats:')

    global balls

    while balls <= 4:

        # This is a ball
        balls += 1

        # Indeed it is...
        print ('BALL ', balls, '!\n', sep='')

        # Ball 4!
        if balls == 4:
            Single()

        Count()

        Swing()

# What is Foul()?
def Foul():

    print ('\nFoul Ball!')

    global strikes
    global fouls

    while strikes < 2:

        Strike()

        Swing()

    Count ()

    Swing()

# What is Hit()?
def Hit():

    global hits
    
    baseball = random.choice(hits)

    if baseball == hits[0]:
        print()  
        Catch()  

    elif baseball == hits[1]:
        print()
        Single()

    elif baseball == hits[2]:
        print()
        Double()

    elif baseball == hits[3]:
        print()
        Triple()

    elif baseball == hits[4]:
        print()
        HomeRun()

    PlayAgain()

# What is a Miss()?
def Miss():

    print ('\nYou missed the ball!')

    Strike()

# What is the count?
def Count():

    global pitches

    pitches += 1

    print ('Strikes: ', strikes, sep='')
    print ('Balls: ', balls, '\n', sep='')
    print ('Outs: ', outs)
    print ('Runs: ', runs, '\n')

    Pitches()

def Pitches():
    
    print('Pitches this batter: ', pitches, '\n')

# What is BaseBall()?
def BaseBall():

    global position

    position += 1

    print ('BAAAAAAAASSSSSEEEEEE BAAAAAAAALLL!')

    Position()

    PlayAgain()

# What is a HomeRun()?
def HomeRun():

    global position
    global strikes
    global balls

    print ('\nTHAT\'S A HOOOOOOOOOOOMMMMMMMMEEEEEE RUUUUUUNNNN!!!!!!!\n')

    position += 4

    strikes = 0
    balls = 0

    Position()

    NextBatter()    

# What is Triple()?
def Single():

    global position

    position += 1

    print ('SINGLE!')

    Position()

    NextBatter()

# What is Double()?
def Double():

    global position

    position += 2

    print ('DOUBLE!')

    Position()

    NextBatter()

# What is Triple()?
def Triple():

    global position

    position += 3

    print ('TRIPLE!')

    Position()

    NextBatter()

# What is Position()?
def Position():

    global position

    if position <= 3:
        print ('\nYou reached base', position, '\n')

    elif position >= 4:
        AddRun()

# What is Run()?
def AddRun():
    
    global runs
    global strikes
    global balls

    strikes = 0
    balls = 0

    print ('You scored a run!\n')

    runs += 1

# What is Catch()?
def Catch():

    print ('The fielder caught the ball.')

    Out()

# What is Out()?
def Out():

    global outs

    print ('You are OUT!\n')

    while outs <= 3:

        outs += 1

        print ('Outs: ', outs, '\n')

        if outs == 3:
            print ('End of inning')
            sys.exit()

        NextBatter()

# What is NextBatter()?
def NextBatter():
    
    global playing
    global yes
    global no
    global pitches

    pitches = 0

    # Next batter?
    playing = input('Bring next batter?(y/n): ')

    # YAY! :D
    while playing in yes:        
        print()
        Play()

    # NAY! :(
    if playing in no:
        print ('\nThanks for playing!')
        sys.exit()

# What is PlayAgain()?
def PlayAgain():

    global playing
    global yes
    global no

    global pitches

    pitches = 0

    # Play again?
    playing = input('Would you like to play again?(y/n): ')

    # YAY! :D
    while playing in yes:        
        print()
        Play()

    # NAY! :(
    if playing in no:
        print ('\nThanks for playing!')
        sys.exit()

# Can we FINALLY play?    
Play()
