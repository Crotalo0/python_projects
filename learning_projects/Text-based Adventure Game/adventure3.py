#Text-based Adventure Game Idea
#Progetto numero 3 

from time import sleep

def scene1(intro,helpMessage,watchAround,north,south,east,west,invalid_message,key,quest1,mushs,item2):
    print(intro)
    quest1 = 'False'
    ans = 'incorrect'
    while ans == 'incorrect':
        c1 = input('So what you wanna do? ')
        sleep(2)
        
        if c1.lower() == 'help':
            print(helpMessage)
            continue
        
        elif c1.lower() == 'watch around':
            print(watchAround)
            continue
        
        elif c1.lower() == 'north':
            if key=="False":
                print(north)
                continue
            else:
                print(northPrintKey)
                ans ='correct'
                #scene2()   #Da completare...
                
        elif c1.lower() == 'east':
             print(east)
             if mushs == "False":
                
                if quest1 == "False":
                    continue
                elif quest1 == "True":
                    print("""                
    Maybe you can take those mushrooms for the rat!
                """)
                    ans2='incorrect'
                    while ans2=='incorrect':
                        c4=input('Take some mushrooms? ')
                        sleep(2)
                    
                        if c4.lower() == 'yes':
                            print("""
    You took some mushrooms.                    
                        """)
                            mushs = 'True'
                            ans2='correct'
                
             elif mushs == 'True':
                 print("    You already took the mushrooms.\n")
                
             else:
                print(invalid_message)
                continue
             continue
       
        elif c1.lower() == 'west':
            print(west)
            
            if mushs == 'False':
                ans2 = 'incorrect'
                while ans2=="incorrect":
                    c3=input('Do you wanna interact with one of them? Yes or no ')
                    sleep(2)
            
                    if c3.lower() == 'yes':
                        key = "True"
                        print("""
    You move in the direction of the rat that shouted before.
    He notices you and start talking in an incomprensible language:
    "We waglio', che vai facendo qui in giro!
    Se cerchi aiuto, portami dei funghi.
    Se poi trovi del cibo migliore, ben venga."
    """)
                        ans2='correct'
                        quest1='True'
                    elif c3.lower() == 'no':
                        print("""
    You simply go back.
    """)
                        break
                    else:
                        print(invalid_message)
                    continue
                continue
            elif mushs == "True":
                print("""
    The rats is patiently waiting for you.
    When he sees you approaching, he shout:
    "Wagliooo', grazie per i funghi.
    Tieni questo strao oggetto che ho trovato nell'intestino
    di quel corpo la dietro."
    He gives you a strange object.
    NOTE PROGRAMMATORE: Qua' poi vedro' cosa sara' in futuro.
    """)
                item2="True"
        elif c1.lower() == 'south':
            print(south)
            ans1 = 'incorrect'
            while ans1=="incorrect":
                c2=input('Search, yes or no? ')
                sleep(2)
            
                if c2.lower() == 'yes':
                    key = "True"
                    print("""
    You decide to search into the body.
    You search deeply, until you see something popping out in a wound in his chest.
    You try to remove carefully the item.
    You found a key!
    It's very rusty and old.
    """)
                    ans1='correct'
                elif c2.lower() == 'no':
                    print("""
    You decide to not touch the body.
    You go back.
    """)
                    break
                else:
                    print(invalid_message)
                continue
                  
        else:
            print(invalid_message)
            continue

#def scene2():
    

 
#Tutti i Print utili
inv_input="""
    Sorry, your input is not valid.
    """
introPrint ="""
    ---+---+---+---+---+---
    Welcome to the Text-based Adventure Game!
    Let's start with the story...
    
    You are in an old and small cage.
    (If you need help write help)
    """
helpPrint ="""
    This is an adventure game controlled only with words.
    There is no fixed objective, the story will be decided by your actions.
    For example, you can decide to watch around the cage by writing 'watch around'.
    The program doesn't care if it is written in uppercase or lowercase.
    If u wanna go east for example try east.
    Then try guessing and find out new things!
    """
watchAroundPrint="""   
    You decide to watch around you.
    The first thing you notice is the disgusting state of the cage.
    There are insects everywhere, rats escrements and other nasty things.
            
    You see a rusty cage door north to you.
    To the south, behind you, there is a dead body firmly secured with chain to the wall.
    To the east, there is only a wall with ruined blocks.
    To the west there are some rats wandering.
    """
northPrint="""
    You decide to go north.
    You see an old cage, sadly it is locked.
    Today you will not be able to escape! HAHA!!
    """
northPrintKey="""
    You decide to go north. 
    You try the key you found...
    Seems to work!
    You are now out of the cage...
    """

southPrint="""
    You decide to go south.
    You immediately see the dead body lying near you.
    The body has different and serious wounds.
    Seems also that the body is dead long time ago, because it is completely putrescent.
    You don't like the smell.
    Do you wanna scan the body? Maybe you'll find something useful... 
    Or maybe you will get some infection.
    """ 
eastPrint="""
    You decide to go east.
    There is a very deprecated wall full of different types of mildew and moss.
    In the very top you see some mushrooms growing.
    """ 
westPrint="""
    You decide to go west.
    Something strange is happening there.
    There is a small table with some rats playing some italian card game.
    Suddendly you hear one of them screaming: "SCOPAAA".
    Other rats seems pissed off and proceed to rage quit the game.
    You can't tell if it's your brain fooling you or the rats are real.
    """ 

CageKey= "False"
QuestTopo = "False"
mushroom = "False"
oggettoMisterioso="False"
scene1(introPrint, helpPrint, watchAroundPrint,northPrint,southPrint,eastPrint,westPrint,inv_input,CageKey,QuestTopo,mushroom,oggettoMisterioso)

"""
DA Fare:
-Dizionario
-Classi Zone
    



"""