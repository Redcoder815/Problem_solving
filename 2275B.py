import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    iterator = iter(data)
    t = int(next(iterator))
    
    out = []
    for _ in range(t):
        n = int(next(iterator))
        s = next(iterator)
        
        stack_ = []
        used = [False] * n
        
        for i in range(n):
            if s[i] == '1':
                stack_.append(i)
            elif s[i] == '2':
                if not stack_:
                    used[i] = True
                else:
                    used[stack_[-1]] = True
                    stack_.pop()
            else:
                used[i] = True
                
        res = [i + 1 for i in range(n) if not used[i]]
        
        out.append(str(len(res)))
        out.append(" ".join(map(str, res)))
        
    print("\n".join(out))

if __name__ == '__main__':
    solve()
