import sys

def solve():
    input = sys.stdin.read
    data = input().split()

    if not data:
        return
    t = int(data[0])
    results = []
    idx = 1
    for _ in range(t):
        a = int(data[idx])
        b = int(data[idx+1])
        idx = idx + 2

        if a <= b:
            results.append("-1")

        else:
            results.append(str(a-b))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()