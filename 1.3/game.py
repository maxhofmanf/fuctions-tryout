print("welcome to lightsouls")
beginning = input("type 'start' to start playing  ")
if beginning == ("start"):
    print(" ")
    print("rules, just use the words at the end of the sentence to continue")
    print(" ")
    wakeup = input("you wake up, and walk outside. infront of you is a sword will you take it? yes/no? ")
    if wakeup == ("no"):
        print(" ")
        print("you left the sword and you went on your day,")
        print("never seeing the sword again.")
        print("you lived a normal boring life and died.")
        print(" ")
        print("The End")
    elif wakeup == ("yes"):
        print(" ")
        print("you pick up the sword and it starts to glow and shines a beam to a direction and you start follow it")
        sword = input("it leats you to a cave, you see 2 red glowing eyes will you trow a rock at it? yes/no? ")
        if sword == ("no"):
            print(" ")
            print("a bunny came out of the cave... it hopped closer, its jaw unhinges and it eats you in 1 bite")
            print(" ")
            print("you died")
            print("The End")
        elif sword == ("yes"):
                print(" ")
                print("you trew the rock the eyes scream and you hear a the animel dropping to the ground")
                print("you walk closer and see that you accidentally killed a bunny")
                print("you monster, you killed an innocent bunny!")
                print("but you have to continue on your journey so you venture into the cave")
                chest = input("you see a chest, it makes weird noises and it moves will you open it? open/dont open ")
                if chest == ("open"):
                    print("you walk closer to the chest... you are about to open the chest but the chest opens by itself!")
                    print("the inside of the chest has sharp teeth ")
                    print("the chest stands up and it reveals that it has arms and legs, its a mimic!")
                    print("it leaps and you and bites your head off")
                    print(" ")
                    print(" you died")
                    print("The End")
                elif chest == ("dont open"):
                    print(" ")
                    print("you walk by the chest, and you venture out into a gaint open room with a statue of a Hydra.")
                    print("under the statue there is a small chest, and surrounding the statue are skeletons bowing to the statue")
                    hydra = input("will you approach the hydra? yes/no ")
                    if hydra ==("yes"):
                        print(" ")
                        print("you approach the statue but then, all the skeletons come to life")
                        print("they surround you... you have 3 choices.")
                        print("run for the statue and hopefully get the box and whats inside of it")
                        print("swing around with the sword and hopefully take as many skeletons with you")
                        print("accept your faith")
                        choice = input(" run/fight/accept ")
                        if choice == ("run"):
                            print(" ")
                            print("you run for the statue!")
                            print("you make it!!")
                            print("you grab and open the box...")
                            print("there is a small slimey egg in the box")
                            print("the skeletons stop and bow for you")
                            print("you had enough and you walk out of the cave.")
                            print("the egg hatches. and a baby hydra's head pop's out. it scared you and you drop it")
                            print("you killed another innocent animal, you are a monster!")
                            print(" you return home and go to bed")
                            print("this was your first and last quest")
                            print(" ")
                            print("The neutral Ending")
                        elif choice == ("fight"):
                            print("you grab your sword and start swinging at the skeletons")
                            print("wow you mananged to destroy 20 skeletons!!!")
                            print("but then the box starts moving")
                            print("the box explodes and a baby hydra pops out")
                            print("it runs to you and its trying to attack")
                            baby = input("what will you do, kick/run ")
                            if baby == ("kick"):
                                print(" ")
                                print("you tried to kick the hydra but one of its heads grabs bites you leg straight off")
                                print("you fall to the ground and the other heads feed on your body")
                                print(" ")
                                print("you died")
                                print("The End")
                            elif baby == ("run"):
                                print("you run out of the cave")
                                print("you feel defeated")
                                print("you go home and sleep while feeling like a loser")
                                print(" ")
                                print ("The loser Ending")
                            print("only use a vaild command")
                        if choice == ("accept"):
                            print(" ")
                            print("you accept your faith")
                            print("you get brutally ripped apart by the skeletons")
                            print(" ")
                            print("you died")
                            print("The End")
                        else:
                            print("only use a vaild command")
                    elif hydra ("no"):
                        print("you ignore the statue and walk 3 meters forward...")
                        print("you drop into a pit with spikes at the bottom")
                        print(" ")
                        print("you died")
                        print("the end")
                else:
                    print("only use a vaild command")
        else:
            print("only use a vaild command")
    else:
        print("only use a vaild command")
elif beginning == ("stop"):
    print("you had 1 job and you failed, congratulations.")
else:
    print("please type start, dont type anything else.")