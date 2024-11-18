import time
import random

class OpenAddressingHashMap:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size  # Tabulka inicializovaná na None
        self.deleted = object()  # Speciální marker pro smazané prvky

    def hash_function(self, key):
        # Jednoduchá hashovací funkce
        return key % self.size

    def add(self, key, value):
        index = self.hash_function(key)
        original_index = index
        while self.table[index] is not None and self.table[index] is not self.deleted:
            stored_key, _ = self.table[index]
            if stored_key == key:  # Aktualizace hodnoty, pokud klíč existuje
                self.table[index] = (key, value)
                return
            index = (index + 1) % self.size
            if index == original_index:  # Pokud se vrátíme na původní index
                raise Exception("HashMap is full")

        # Přidání nového prvku
        self.table[index] = (key, value)

    def find(self, key):
        index = self.hash_function(key)
        original_index = index
        while self.table[index] is not None:
            if self.table[index] is not self.deleted:
                stored_key, stored_value = self.table[index]
                if stored_key == key:
                    return stored_value
            index = (index + 1) % self.size
            if index == original_index:  # Pokud se vrátíme na původní index
                break
        return None  # Klíč nebyl nalezen

    def delete(self, key):
        index = self.hash_function(key)
        original_index = index
        while self.table[index] is not None:
            if self.table[index] is not self.deleted:
                stored_key, _ = self.table[index]
                if stored_key == key:
                    self.table[index] = self.deleted  # Označit jako smazané
                    return True
            index = (index + 1) % self.size
            if index == original_index:
                break
        return False  # Klíč nebyl nalezen pro smazání

def measure_time(operation, *args):
    start = time.time()
    result = operation(*args)
    end = time.time()
    return result, end - start

if __name__ == "__main__":
    hash_map = OpenAddressingHashMap(200000)  # Velikost tabulky
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
