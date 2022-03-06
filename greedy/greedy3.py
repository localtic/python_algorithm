M, N = map(int, input().split())

min_list = []
for _ in range(N):
    numbers = list(map(int, input().split()))
    min_list.append(min(numbers))

print(max(min_list))