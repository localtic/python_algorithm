# 아스키 대문자 65~90 -> -64
# 아스키 소문자 97~122 -> -96

now = input()
x = ord(now[0]) - 96
y = int(now[1])

locations = [[-2, -1], [-2, 1], [2, 1], [2, -1], [1, 2], [1, -2], [-1, 2], [-1, -2]]

cnt = 8
for i in range(len(locations)):
    nx = x + locations[i][0]
    ny = y + locations[i][1]
    if nx > 8 or ny > 8 or nx < 1 or ny < 1:
        cnt -= 1
print(cnt)