import time
import random

def measure_time(operation, *args):
    start = time.time()
    result = operation(*args)
    end = time.time()
    return result, end - start

def add_elements(array, elements):
    array.extend(elements)
    pass

def find_elements(array, elements):
    results = []
    for el in elements:
        results.append(el in array)
        return results
    pass

if __name__ == "__main__":
    array = []
    data = list(range(1, 100001))
    random.shuffle(data)

    # Přidávání po dávkách
    for i in range(0, len(data), 10000):
        batch = data[i:i+10000]
        _, duration = measure_time(add_elements, array, batch)
        print(f"Adding batch {i//10000 + 1}: {duration:.6f} s")

    # Hledání po dávkách
    random.shuffle(data)
    for i in range(0, len(data), 10000):
        batch = data[i:i+10000]
        _, duration = measure_time(find_elements, array, batch)
        print(f"Finding batch {i//10000 + 1}: {duration:.6f} s")
