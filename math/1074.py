import sys; input = sys.stdin.readline

n,r,c = map(int, input().split())
cost = 0
group = 1

while n >= 1:
      line = 2 ** (n-1)
      if r < line and c < line: 
            group = 1
      if r < line and c >= line: 
            group = 2
            c -= line
      if r >= line and c < line: 
            group = 3
            r -= line
      if r >= line and c >= line: 
            group = 4
            r -= line
            c -= line
      cost += line ** 2 * (group - 1)
      n-=1

print(cost)