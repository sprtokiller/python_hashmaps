import time
import random

def measure_time(operation, *args):
    start = time.time()
    result = operation(*args)
    end = time.time()
    return result, end - start

def add_elements(hash_map, keys, values):
    for key, value in zip(keys, values):
        hash_map[key] = value

def find_elements(hash_map, keys):
    return [hash_map.get(key, None) for key in keys]

if __name__ == "__main__":
    hash_map = {}
    data = list(range(1, 100001))
    random.shuffle(data)

    # Přidávání po dávkách
    for i in range(0, len(data), 10000):
        batch = data[i:i+10000]
        _, duration = measure_time(lambda b: add_elements(hash_map, b, [f"value{k}" for k in b]), batch)
        print(f"Adding batch {i//10000 + 1}: {duration:.6f} s")

    # Hledání po dávkách
    random.shuffle(data)
    for i in range(0, len(data), 10000):
        batch = data[i:i+10000]
        _, duration = measure_time(lambda b: find_elements(hash_map, b), batch)
        print(f"Finding batch {i//10000 + 1}: {duration:.6f} s")
