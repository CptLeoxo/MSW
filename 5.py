import numpy as np
from scipy import optimize
import time

# Polynomialni fce
def pf(x):
    return x**3 - x - 2

# Exponenciilni fce
def ef(x):
    return np.exp(x) - 2

# Harmonicka fce
def hf(x):
    return np.sin(x) - 0.5

# Bisekce + kontrola znamenka
def bisekce(func, a, b, tol=1e-6):
    if np.sign(func(a)) == np.sign(func(b)):
        raise ValueError(f"f(a) a f(b) musi mit ruzna znamenka: f({a})={func(a)}, f({b})={func(b)}")
    koren = optimize.bisect(func, a, b, xtol=tol)
    return koren

# Newtonova metoda
def newton(func, x0, tol=1e-6):
    koren = optimize.newton(func, x0, tol=tol)
    return koren


start_time = time.time()
pf_bkoren = bisekce(pf, 1, 2)
pf_bcas = time.time() - start_time

start_time = time.time()
pf_nkoren = newton(pf, 1.5)
pf_ncas = time.time() - start_time


start_time = time.time()
ef_bkoren = bisekce(ef, 0, 1)
ef_bcas = time.time() - start_time

start_time = time.time()
ef_nkoren = newton(ef, 0.5)
ef_ncas = time.time() - start_time


start_time = time.time()
hf_bkoren = bisekce(hf, 0, np.pi/2)
hf_bcas = time.time() - start_time

start_time = time.time()
hf_nkoren = newton(hf, 1.0)
hf_ncas = time.time() - start_time


print(f"Polynomiální funkce (bisekce): {pf_bkoren}, čas: {pf_bcas}")
print(f"Polynomiální funkce (Newton): {pf_nkoren}, čas: {pf_ncas}")

print(f"Exponencialní funkce (bisekce): {ef_bkoren}, čas: {ef_bcas}")
print(f"Exponencialní funkce (Newton): {ef_nkoren}, čas: {ef_ncas}")

print(f"Harmonicka funkce (bisekce): {hf_bkoren}, čas: {hf_bcas}")
print(f"Harmonicka funkce (Newton): {hf_nkoren}, čas: {hf_ncas}")
