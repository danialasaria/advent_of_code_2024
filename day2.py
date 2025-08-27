# from typing import List
# with open('data2.txt', 'r') as file:
#     reports: List[List] = []
#     for line in file:
#         reports.append(list(map(int, line.split())))
        
#     total_safe = 0
#     for level in reports:
#         mode = "Increasing"
#         safe = 1
#         if level[0] > level[1]:
#             mode = "Decreasing"
#         if not 1<=abs(level[0]-level[1])<=3:
#             safe-=1
#         for i in range(1,len(level)):
#             if mode == "Increasing" and (level[i] < level[i-1] or not 1<=abs(level[i]-level[i-1])<=3):
#                 safe-=1
#             elif mode == "Decreasing" and (level[i] > level[i-1] or not 1<=abs(level[i]-level[i-1])<=3):
#                 safe-=1
#         if safe>=0: total_safe+=1
#     print(total_safe)
from typing import List

def is_safe(levels: List[int]) -> bool:
    direction = 0  # 0 unknown, 1 increasing, -1 decreasing
    for i in range(1, len(levels)):
        diff = levels[i] - levels[i - 1]
        if diff == 0 or not 1 <= abs(diff) <= 3:
            return False
        if direction == 0:
            direction = 1 if diff > 0 else -1
        elif (direction == 1 and diff < 0) or (direction == -1 and diff > 0):
            return False
    return True

def is_safe_with_dampener(levels: List[int]) -> bool:
    if is_safe(levels):
        return True
    return any(is_safe(levels[:i] + levels[i+1:]) for i in range(len(levels)))

with open('data2.txt', 'r') as file:
    # reports: List[List] = []
    total=0
    for line in file:
        total+=is_safe_with_dampener((list(map(int, line.split()))))
    print(total)