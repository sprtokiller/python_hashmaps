import time
import random

class OpenAddressingHashMap:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        """Jednoduchá hashovací funkce."""
        return key % self.size

    def add(self, key, value):
        """Přidá prvek s klíčem `key` a hodnotou `value` do hashmapy."""
        index = self.hash_function(key)
        start_index = index  # Pro detekci plné tabulky

        while self.table[index] is not None:
            # Přepiš hodnotu, pokud se shoduje klíč
            existing_key, _ = self.table[index]
            if existing_key == key:
                self.table[index] = (key, value)
                return
            # Lineární probing
            index = (index + 1) % self.size
            if index == start_index:
                raise Exception("Hash table is full!")

        # Uložení nového páru (key, value)
        self.table[index] = (key, value)

    def find(self, key):
        """Najde a vrátí hodnotu spojenou s klíčem `key`. Pokud klíč neexistuje, vrátí `None`."""
        index = self.hash_function(key)
        start_index = index  # Pro detekci cyklu

        while self.table[index] is not None:
            existing_key, value = self.table[index]
            if existing_key == key:
                return value
            # Lineární probing
            index = (index + 1) % self.size
            if index == start_index:
                break

        return None

def measure_time(operation, *args):
    """Změří dobu trvání operace."""
    start = time.time()
    result = operation(*args)
    end = time.time()
    return result, end - start

if __name__ == "__main__":
    hash_map = OpenAddressingHashMap(200000)  # Velikost tabulky musí být větší než počet klíčů
    data = list(range(1, 100001))
    random.shuffle(data)

    # Přidávání po dávkách
    for i in range(0, len(data), 10000):
        batch = data[i:i+10000]
        _, duration = measure_time(lambda b: [hash_map.add(key, f"value{key}") for key in b], batch)
        print(f"Adding batch {i//10000 + 1}: {duration:.6f} s")

    # Hledání po dávkách
    random.shuffle(data)
    for i in range(0, len(data), 10000):
        batch = data[i:i+10000]
        _, duration = measure_time(lambda b: [hash_map.find(key) for key in b], batch)
        print(f"Finding batch {i//10000 + 1}: {duration:.6f} s")
