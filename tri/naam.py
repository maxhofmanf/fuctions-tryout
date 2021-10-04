n=1

while n < 2:
        naam = input("wat is uw naam?  ")
        leeftijd = input ("hou oud bent u?  ")
        print("hallo", naam , "je bent", leeftijd, "jaar oud")
        door = input("wil je door gaan?  J/N  :")
        if door == "j":
                n+0
        elif door == "n":
                n+1
                break
        else:
                print("gebruik alleen j of n.")
        