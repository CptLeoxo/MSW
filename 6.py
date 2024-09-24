# Generovani nahodnych cisel a testovani generatoru
from pynput.mouse import Listener
import time
import random

mys_pozice = []

def pozice(x, y):
    mys_pozice.append((x, y))

def generator_seminka():
    seminko = sum([x + y for x, y in mys_pozice]) % (2**32)
    return seminko

def sber_dat(doba=5):
    print(f"Hybejte myši po dobu {doba} vteřin.")
    
    with Listener(on_move=pozice) as listener:
        time.sleep(doba)
        listener.stop()

    print(f"Nasbíráno {len(mys_pozice)} pozic myši.")
    # print(mys_pozice)
    return generator_seminka()

if __name__ == "__main__":
    seminko = sber_dat(5)
    
    random.seed(seminko)
    print(f"Vygenerované semínko: {seminko}")
    print(f"Náhodné číslo: {random.randint(1, 100)}")
