data = ['test', 90, 80, (1995, 8, 30)]


if __name__ == "__main__":
    _, start, end, (_, _, day) = data
    print(start)
    print(end)
    print(day)