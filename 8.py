import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

def f(x):
    return x**3 - x - 2

# Analytická derivace
x = sp.symbols('x')
analyticka_vyraz = f(x)
analyticka_derivace = sp.diff(analyticka_vyraz, x)


def analyticka_derivace_fce(hodnota):
    return float(analyticka_derivace.subs(x, hodnota))

# Staticka derivace
def staticka_derivace(f, x, h=0.01):
    return (f(x + h) - f(x - h)) / (2 * h)

# Adaptivni derivace
def adaptivni_derivace(f, x, tol=1e-6):
    h = 0.1
    diff = (f(x + h) - f(x - h)) / (2 * h)
    
    while True:
        h_new = h / 2
        diff_new = (f(x + h_new) - f(x - h_new)) / (2 * h_new)
        
        if np.abs(diff_new - diff) < tol:
            return diff_new
        diff = diff_new
        h = h_new


hodnoty = np.linspace(-2, 2, 100)
analyticka = np.array([analyticka_derivace_fce(val) for val in hodnoty])
adaptivni = np.array([adaptivni_derivace(f, val) for val in hodnoty])
staticka = np.array([staticka_derivace(f, val) for val in hodnoty])


plt.plot(hodnoty, analyticka, label='Analytická derivace', color='blue')
plt.plot(hodnoty, adaptivni, label='Adaptivní krok', linestyle='--', color='green')
plt.plot(hodnoty, staticka, label='Statický krok', linestyle='--', color='red')
plt.legend()
plt.title('Porovnání derivací')
plt.xlabel('x')
plt.ylabel('Derivace')
plt.grid(True)
plt.show()
