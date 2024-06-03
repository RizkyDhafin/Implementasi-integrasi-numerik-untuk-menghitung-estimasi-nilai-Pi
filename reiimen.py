import numpy as np
import time

# Fungsi f(x)
def f(x):
    return 4 / (1 + x**2)

# Integrasi Reimann
def reimann_integral(f, a, b, N):
    dx = (b - a) / N
    total = 0
    for i in range(N):
        total += f(a + i * dx) * dx
    return total

# Testing
N_values = [10, 100, 1000, 10000]
true_pi = 3.14159265358979323846

for N in N_values:
    start_time = time.time()
    pi_approx = reimann_integral(f, 0, 1, N)
    execution_time = time.time() - start_time
    error = np.sqrt((true_pi - pi_approx)**2)
    print(f"N = {N}, Approximated pi = {pi_approx}, Error (RMS) = {error}, Execution Time = {execution_time} seconds")
