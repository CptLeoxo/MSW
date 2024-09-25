import numpy as np
import sympy
import matplotlib.pyplot as plt
from scipy.misc import derivative

def f(x):
    return x**3 - x - 2

# Analyticka derivace
def analyticka_derivace(x):
    return x**3 - x - 2

# Numericka derivace s adaptabilnim krokem
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


# Staticka derivace s konstantnim krokem
def staticka_derivace(f, x, h=0.01):
    return (f(x + h) - f(x - h)) / (2 * h)


hodnoty = np.linspace(0, 2 * np.pi, 100)

analyticka = analyticka_derivace(hodnoty)
adaptivni = np.array([adaptivni_derivace(f, x) for x in hodnoty])
staticka = np.array([staticka_derivace(f, x) for x in hodnoty])

plt.plot(hodnoty, analyticka, label='Analytická derivace', color='blue')
plt.plot(hodnoty, adaptivni, label='Adaptabilní krok', linestyle='--', color='green')
plt.plot(hodnoty, staticka, label='Statický krok', linestyle='--', color='red')
plt.legend()
plt.title('Porovnání derivace')
plt.xlabel('x')
plt.ylabel('Derivace')
plt.grid(True)
plt.show()
