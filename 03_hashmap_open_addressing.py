import time
import random

class OpenAddressingHashMap:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return key % self.size

    def add(self, key, value):
        # Přidá prvek s klíčem "key" a hodnotou "value" do hashmapy
        table_index = self.hash_function(key)
        for i in range(self.size):
            index = (i + table_index) % self.size
            if(self.table[index] == None):
                self.table[index] = {key: key, value:value}
                return
        OverflowError()

    def find(self, key):
        # Najde prvek s klíčem "key" v hashmapě a vrátit jeho hodnotu
        table_index = self.hash_function(key)
        for i in range(self.size):
            index = (i + table_index) % self.size
            if(key in self.table[index]):
                return self.table[index]
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
