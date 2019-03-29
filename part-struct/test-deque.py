from collections import deque


def search(lines, pattern, history):
    pre_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            pre_lines.append(line)
    return pre_lines


if __name__ == "__main__":
    with open('tmp/test', 'r') as f:
        s = search(f, 'python', 5)
        print(s)
        s.append('python9')
        s.appendleft('python')
        s.pop()
        s.popleft()
        for line in s:
            print(line)
        print("end")