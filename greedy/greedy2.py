n, m, k = map(int, input().split())
numbers = list(map(int, input().split()))

numbers.sort(reverse=True)
first = numbers[0]
second = numbers[1]

result = 0

while True:
    for i in range(k):
        if m == 0:
            break
        result += first
        m -= 1
    if m == 0:
        break
    result += second
    m-= 1
print(result)