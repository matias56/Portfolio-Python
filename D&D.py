import sys
import keyboard
import random
import time
i = 0
print(f"Press Space to play or Esc to exit.")
while i < 5:
    if keyboard.is_pressed('Space'):
        name = input('Enter your name: ')
        print(f'Greetings {name}!')
        print(f'Welcome to Dungeons & Dragons!')
        character = input(f'Choose your character! Fighter, Wizard or Rogue.')
        Start = False

        #Fighter
        if character == 'Fighter':
            st = 18
            de = 10
            co = 16
            i = 8
            wi = 11
            ch = 12

            stMod = +4
            deMod = 0
            coMod = +3
            iMod = -1
            wiMod = 0
            chMod = +2

            HP = 10
            AC = 13

            att = ('Melee')
            Att = random.randint(1, 20) + stMod
            dmg = random.randint(2, 6) + stMod

            

            exp = 0

            print(f'STR ', st, ' ', 'MOD ', stMod)
            print(f'DEX ', de, ' ', 'MOD ', deMod)
            print(f'CON ', co, ' ', 'MOD ', coMod)
            print(f'INT ', i, ' ', 'MOD ', iMod)
            print(f'WIS ', wi, ' ', 'MOD ', wiMod)
            print(f'CHA ', ch, ' ', 'MOD ', chMod)
            print(f'HP ', HP)
            print(f'AC ', AC)
            print(f'Attack ', att)
            print(f'Experience: ', exp)
            Start = True

            # Wizard
        elif character == 'Wizard':
            st = 8
            de = 10
            co = 9
            i = 18
            wi = 16
            ch = 11

            stMod = -1
            deMod = 0
            coMod = -1
            iMod = +4
            wiMod = +3
            chMod = 0

            HP = 12
            AC = 9

            att = ('Spell')
            Att = random.randint(1, 20) + iMod
            dmg = random.randint(3, 6) + iMod

           

            exp = 0

            print(f'STR ', st, ' ', 'MOD ', stMod)
            print(f'DEX ', de, ' ', 'MOD ', deMod)
            print(f'CON ', co, ' ', 'MOD ', coMod)
            print(f'INT ', i, ' ', 'MOD ', iMod)
            print(f'WIS ', wi, ' ', 'MOD ', wiMod)
            print(f'CHA ', ch, ' ', 'MOD ', chMod)
            print(f'HP ', HP)
            print(f'AC ', AC)
            print(f'Attack ', att)
            print(f'Experience: ', exp)

            Start = True

            # Rogue
        elif character == 'Rogue':
            st = 11
            de = 18
            co = 10
            i = 15
            wi = 8
            ch = 16

            stMod = 0
            deMod = +4
            coMod = 0
            iMod = +2
            wiMod = -1
            chMod = +3

            HP = 13
            AC = 10

            att = ('Crossbow & Dagger')
            Att = random.randint(1, 20) + deMod
            dmg = random.randint(1, 4) + deMod

           

            exp = 0

            print(f'STR ', st, ' ', 'MOD ', stMod)
            print(f'DEX ', de, ' ', 'MOD ', deMod)
            print(f'CON ', co, ' ', 'MOD ', coMod)
            print(f'INT ', i, ' ', 'MOD ', iMod)
            print(f'WIS ', wi, ' ', 'MOD ', wiMod)
            print(f'CHA ', ch, ' ', 'MOD ', chMod)
            print(f'HP ', HP)
            print(f'AC ', AC)
            print(f'Attack ', att)
            print(f'Experience: ', exp)

            Start = True
        else:
         print(f'Choose Again!')
         i = 0

         #Game Start
        while Start == True:
            lev1 = False
            #Cell
            option1 = input(
                'You find yourself in a cell of a dungeon, then, from a wall, a key slips underneath. What will you do? STAY or GO?')
                #Game Over
            if option1 == 'STAY':
                print(
                    f'Hours later, rats will come to your cell and will start to eat you. Game Over.')
                time.sleep(5.5)
                sys.exit(0)
                #Go
            elif option1 == 'GO':
                #First Level
                lev1 = True
            else:
                print(f'Choose Again!')
                Start = True
            while lev1 == True:
                Level2 = False
                #DeadGuard
                option2 = input(
                    'You are outside the cell and find a dead guard. TAKE his sword or NO?')
                    #Better Melee
                if option2 == 'TAKE':
                    print(f'You have taken the sword with you.')
                    stMod + 2
                    Level2 = True
                    #Don't take sword
                elif option2 == 'NO':
                    print(f'You leave the sword there.')
                    Level2 = True
                else:
                    print(f'Choose Again!')
                    lev1 = True
                    #Level 2
                while Level2 == True:

                    Fight = False

                    level3 = False

                    #Goblin
                    what = input(
                        f"On the way you find a goblin, he didn't notice you and you can make a stealth check to pass without being unnoticed or fight him. FIGHT or PASS? You can sneak KILL him too.")
                    #Choose
                    if what == 'FIGHT':
                        print(f'The goblin notices you. Fight!')
                        gDeMod = 1

                        gStMod = 1

                        gAC = 11

                        

                        

                        

                        gHP = 8
                        Fight = True
                        #Pass
                    elif what == 'PASS':
                        print(f'You try to sneak and walk unnoticed. Can you succeed?')
                        print(f"Press Enter to Roll 1d20")
                        d20 = random.randint(1, 20) + deMod
                        print(d20)
                        if d20 >= 12:
                          print(f"You sneaked away from him!")
                          level3 = True
                        elif d20 < 12:
                          print(f"You failed! Now, battle!")
                          Fight = True

                    #Kill
                    elif what == 'KILL':
                        print(f'Will you kill him easily or will you be noticed?')
                        print(f"Press Enter to Roll 1d20")
                        
                        d20 = random.randint(1, 20) + deMod
                        print(d20)
                        if d20 >= 15:
                          print(f"You killed him!")
                          exp = exp + 100
                          print(f'Now your experience is ', exp)
                          level3 = True
                        elif d20 < 15:
                          print(f"You failed! Now, battle!")
                          Fight = True

                    else:
                        print(f'Choose Again!')
                        Level2 = True

                        #Fight

                    while Fight == True:
                        Start == False
                        
                        YTurn = False
                        GTurn = False

                         

                         

                        initiative = random.randint(1, 20) + deMod

                        gInit = random.randint(1, 20) + gDeMod

                        if initiative == gInit:

                            print(initiative, gInit)
                            print(f'Roll again!')

                            Fight = True

                        elif initiative > gInit:
                            print(initiative, gInit)

                            print(f'You go first!')
                            YTurn = True

                        elif initiative < gInit:

                            print(initiative, gInit)

                            print(f'Goblin goes first!')
                            
                            GTurn = True

                        

                        while YTurn == True:
                            
                            Att

                            if Att >= gAC:

                                print(Att)

                                print(f'You hit your opponent!')
                               

                                dmg

                                print(dmg)

                                gHP = gHP - dmg

                                if gHP <= 0:
                                    Fight = False
                                    YTurn = False
                                    GTurn = False
                                    print(f'You have slain the goblin!')
                                    
                                    exp = exp + 100
                                    print(f'Now your experience is ', exp)
                                    
                                    level3 = True

                                else:
                                    print(f"Goblin's turn!")
                                   
                                   
                                    GTurn = True
                                    YTurn = False
                            else:
                                print(f"You missed! Goblin's turn!")
                                
                                
                                GTurn = True
                                YTurn=False

                        while GTurn == True:

                            
                           
                            gAtt = random.randint(1, 20) + gStMod

                            if gAtt >= AC:
                                print(gAtt, AC)
                                print(f'The goblin hits you!')
                               
                                gDMG = random.randint(1, 20) + gStMod

                               

                                HP = HP - gDMG
                                print(f'You take ', gDMG, ' damage, and now you have ', HP, ' left!')
                                if HP <= 0:

                                    print(f"You died! It's Game Over, man!")
                                    time.sleep(5.5)
                                    sys.exit(0)
                                else:
                                     print(f'Your turn!')
                                    
                                    
                                     YTurn = True
                                     GTurn=False
                            else:

                                print(gAtt, AC)
                                print(f'Goblin misses you!')
                               
                                
                                YTurn = True
                                GTurn=False

                    while level3 == True:
                        print(f'You find a bridge.')
                        
                        print(f'The end')
                        time.sleep(5.5)
                        sys.exit(0)

    if keyboard.is_pressed('Esc'):
        sys.exit(0)
