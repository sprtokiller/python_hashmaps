import time
import random

def measure_time(operation, *args):
    start = time.time()
    result = operation(*args)
    end = time.time()
    return result, end - start

def add_elements(array, elements):
    array.extend(elements)

def find_elements(array, elements):
    return [el for el in elements if el in array]

if __name__ == "__main__":
    array = []
    data = list(range(1, 100001))
    random.shuffle(data)

    for i in range(0, len(data), 10000):
        batch = data[i:i+10000]
        _, duration = measure_time(add_elements, array, batch)
        print(f"Adding batch {i//10000 + 1}: {duration:.6f} s")

    random.shuffle(data)
    for i in range(0, len(data), 10000):
        batch = data[i:i+10000]
        found, duration = measure_time(find_elements, array, batch)
        print(f"Finding batch {i//10000 + 1}: {duration:.6f} s, Found: {len(found)}")
