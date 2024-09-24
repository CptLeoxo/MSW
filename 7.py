import random

znaky = ['A', 'B', 'C']

def slot(n):
    jackpot_vyhry = 0

    for _ in range(n):
        # simulace otacek valcu se tremi symboly
        tah = [random.choice(znaky) for _ in range(3)]
        
        # kontrola, zda hrac vyhral jackpot
        if tah[0] == tah[1] == tah[2]:
            jackpot_vyhry += 1

    return jackpot_vyhry

n = 10000
jackpot_vyhry = slot(n)

jackpot_pr = jackpot_vyhry / n

print(f"Vyhráli jackpot: {jackpot_vyhry} krát.")
print(f"Pravděpodobnost výhry jackpotu: {jackpot_pr:.2%}")
