# 상하좌우
n = int(input())
x, y = 1, 1
routes = input().split()

direction = ["L", "R", "U", "D"]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for route in routes:
    for i in range(len(direction)):
        if route == direction[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x, y = nx, ny

print(x, y)