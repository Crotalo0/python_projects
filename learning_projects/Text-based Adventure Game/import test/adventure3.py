#Text-based Adventure Game Idea
#Progetto numero 3 

import adventurePrint
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
 



scene1(adventurePrint.introPrint, adventurePrint.helpPrint, adventurePrint.watchAroundPrint,adventurePrint.northPrint,adventurePrint.southPrint,adventurePrint.eastPrint,adventurePrint.westPrint,adventurePrint.inv_input,adventurePrint.CageKey,adventurePrint.QuestTopo,adventurePrint.mushroom,adventurePrint.oggettoMisterioso)

"""
DA Fare:
-Dizionario
-Classi Zone
    



"""