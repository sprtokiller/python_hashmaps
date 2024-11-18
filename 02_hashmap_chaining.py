import time
import random

class ChainingHashMap:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        result = key % self.size
        return result

    def add(self, key, value):
        index = self.hash_function(key)

        chain = self.table[index]

        for i, (k, value) in enumerate(chain):
            if k == key:
                chain[i] = (key, value)
                return
        chain.append((key, value))

    def find(self, key):
        index = self.hash_function(key)
        chain = self.table[index]
        
        for i, value in chain:
            if i == key:
                return value
        return

def measure_time(operation, *args):
    start = time.time()
    result = operation(*args)
    end = time.time()
    return result, end - start

if __name__ == "__main__":
    hash_map = ChainingHashMap(1000)
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

