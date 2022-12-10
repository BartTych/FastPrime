import Prime
import numpy as np
import pickle
import datetime

start = datetime.datetime.now()

# super cool rozwiazanie wolnego algorytmu reszty z dzielenia

B = np.ones(10**9)
B = B + 134

print(np.mod(10**18,B))

koniec = datetime.datetime.now()
print(f"Czas obliczen: {koniec - start}" )