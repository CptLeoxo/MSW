import time
import timeit
from scipy.integrate import quad
import numpy as np
import sympy as sp
import random
import math


# 1) Skalarni soucin

# Cisty Python
def skalar_python(a, b):
    return sum(x * y for x, y in zip(a, b))

# NumPy
def skalar_np(a, b):
    return np.dot(a, b)

a = np.random.rand(1000)
b = np.random.rand(1000)

# Cas pro cisty Python
start = time.time()
result_sp = skalar_python(a, b)
time_sp = time.time() - start

# Cas pro NumPy
start = time.time()
result_np = skalar_np(a, b)
time_np = time.time() - start

print(f"Skalární součin čistý Python: {time_sp} vteřin.")
print(f"Skalární součin NumPy: {time_np} vteřin.")


# 2) Urcity integral 

# Cisty Python
def integral_cp(n):
    dx = 1 / n
    return sum((i * dx) ** 2 for i in range(n)) * dx


# Funkce pro SciPy
def integral_scipy():
    return quad(lambda x: x**2, 0, 1)[0]


n = 1000000

# Cas pro cisty Python
start = time.time()
result_cp = integral_cp(n)
time_cp = time.time() - start

# Cas pro SciPy
start = time.time()
result_scipy = integral_scipy()
time_scipy = time.time() - start

print(f"Vypočet určitého integrálu s pomocí čistého Pythonu: {time_cp} vteřin.")
print(f"Vypočet určitého integrálu s pomocí SciPy: {time_scipy} vteřin.")


# 3) Matice nasobeni

# Cisty Python
def matice_nas_cp(A, B):
    return [[sum(a * b for a, b in zip(A_row, B_col)) for B_col in zip(*B)] for A_row in A]

# NumPy
def matice_nas_np(A, B):
    return np.dot(A, B)

# Matice
A = np.random.rand(500, 500)
B = np.random.rand(500, 500)

# Cas pro cisty Python
start = time.time()
result_cp = matice_nas_cp(A.tolist(), B.tolist())
time_cp = time.time() - start

# Cas pro NumPy
start = time.time()
result_np = matice_nas_np(A, B)
time_np = time.time() - start

print(f"Vypočet násobení matic s pomocí čistého Pythonu: {time_cp} vteřin.")
print(f"Vypočet násobení matic s pomocí NumPy: {time_np} vteřin.")


# 4) Generator nahodnych cisel

# Cisty Python
def random_cp(n):
    return sum(random.random() for _ in range(n)) / n

# NumPy
def random_mean_np(n):
    return np.mean(np.random.rand(n))


# Cas pro cisty Python
n = 1000000
start = time.time()
result_cp = random_cp(n)
time_cp = time.time() - start

# Cas pro NumPy
start = time.time()
result_np = random_mean_np(n)
time_np = time.time() - start

print(f"Generování nahodných císel s pomocí čistého Pythonu: {time_cp} vteřin.")
print(f"Generování nahodných císel s pomocí NumPy: {time_np} vteřin.")


# 5) Vypocet faktorialu

# Cisty Python
def faktorial_cp(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Math knihovna
def faktorial_math(n):
    return math.factorial(n)

n = 100000

# Cas pro cisty Python
start = time.time()
result_cp = faktorial_cp(n)
time_cp = time.time() - start

# Cas pro math
start = time.time()
result_math = faktorial_math(n)
time_math = time.time() - start

print(f"Vypocet faktorialu s pomoci cisteho Pythonu: {time_cp:.6f} vteřin.")
print(f"Vypocet faktorialu s pomoci knihovny math: {time_math:.6f} vteřin.")
