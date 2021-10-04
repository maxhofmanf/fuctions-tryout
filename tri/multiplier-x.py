
n = int(input("van welke getal wilt u de tafel zien? "))
def print_tafel(num):
    for m in range(1,11):
        print(num,'x', m , '=',num*m)
print_tafel(n)