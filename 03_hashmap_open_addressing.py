import time
import random

class OpenAddressingHashMap:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return hash(key) % self.size
        

    def add(self, key, value):
        index = self.hash_function(key)
        for _ in range(self.size):
            if self.table[index] is None or self.table[index]:
                self.table[index] = (key, value)
                return
            elif self.table[index][0] == key:
                self.table[index] = (key, value)
                return
            index = (index + 1) % self.size
        pass

    def find(self, key):
        index = self.hash_function(key)
        for _ in range(self.size):
            if self.table[index] is None:
                return None
            if self.table[index] and self.table[index][0] == key:
                return self.table[index][1]
            index = (index + 1) % self.size

        return None

def measure_time(operation, *args):
    start = time.time()
    result = operation(*args)
    end = time.time()
    return result, end - start

if __name__ == "__main__":
    hash_map = OpenAddressingHashMap(200000)
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
