import time
import random

class ChainingHashMap:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        # Jednoduchá hashovací funkce
        return key % self.size

    def add(self, key, value):
        # Přidá klíč a hodnotu do hashmapy
        index = self.hash_function(key)
        # Kontrola, zda klíč už existuje, pokud ano, aktualizuje hodnotu
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        # Jinak přidá nový pár
        self.table[index].append([key, value])

    def find(self, key):
        # Najde hodnotu podle klíče
        index = self.hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None  # Pokud klíč neexistuje

def measure_time(operation, *args):
    start = time.time()
    result = operation(*args)
    end = time.time()
    return result, end - start

if __name__ == "__main__":
    hash_map = ChainingHashMap(1000)  # Velikost hashmapy je 1000
    data = list(range(1, 100001))  # Data od 1 do 100000
    random.shuffle(data)

    # Přidávání po dávkách
    for i in range(0, len(data), 10000):
        batch = data[i:i+10000]
        _, duration = measure_time(lambda b: [hash_map.add(key, f"value{key}") for key in b], batch)
        print(f"Přidání dávky {i//10000 + 1}: {duration:.6f} s")

    # Hledání po dávkách
    random.shuffle(data)
    for i in range(0, len(data), 10000):
        batch = data[i:i+10000]
        _, duration = measure_time(lambda b: [hash_map.find(key) for key in b], batch)
        print(f"Hledání dávky {i//10000 + 1}: {duration:.6f} s")
