import sys

def solve():
    # Read all input from standard input
    input = sys.stdin.read
    data = input().split()
    
    if not data:
        return
    
    # First element is the number of test cases
    t = int(data[0])
    
    results = []
    idx = 1
    for _ in range(t):
        x0 = int(data[idx])
        y0 = int(data[idx+1])
        R = int(data[idx+2])
        idx += 3
        
        # Simply shift the x-coordinate by R to stay on the boundary
        ans_x = x0 + R
        ans_y = y0
        
        results.append(f"{ans_x} {ans_y}")
        
    # Print all answers separated by newline
    print('\n'.join(results))

if __name__ == '__main__':
    solve()
