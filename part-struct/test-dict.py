from collections import defaultdict


if __name__ == "__main__":
    d = {
        "1": 1,
        "2": 2,
        "5": 5,
        "4": 4,
    }
    print(d.keys())
    print(d.values())
    print(zip(d.values(), d.keys()))
    max_value = max(zip(d.values(), d.keys()))
    min_value = min(zip(d.values(), d.keys()))
    print(max_value)
    print(min_value)