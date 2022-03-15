from collections import deque

def push_(queue, data):
    queue.append(data)
    
def pop_(queue):
    if not queue:
        return -1
    return queue.popleft()

def size_(queue):
    return len(queue)

def empty_(queue):
    if not queue:
        return 1
    return 0

def front_(queue):
    # if not empty_(queue)
    if not queue:
        return -1
    return queue[0]

def back_(queue):
    if not queue:
        return -1
    return queue[-1]

def queue_program(command, queue):
    if command.startswith("push"):
        push_(queue, command.split()[-1])
    elif command == "pop":
        print(pop_(queue))
    elif command == "size":
        print(size_(queue))
    elif command == "empty":
        print(empty_(queue))
    elif command == "front":
        print(front_(queue))
    elif command == "back":
        print(back_(queue))
    else:
        RuntimeError()

import sys
        
command_cnt = int(input())
# 일반 list보다 pop(0)에 대해서 시간복잡도 낮다
# list -> pop(0): 시간복잡도 O(N) 다 왼쪽으로 한 칸씩, shift overhead 발생
# deque -> popleft(): 시간복잡도 O(1)
queue = deque([])

for i in range(command_cnt):
    # readline 줄 바꿈 제거
    command = sys.stdin.readline().rstrip()
    queue_program(command, queue)