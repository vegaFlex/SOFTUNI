from collections import deque

total_honey = 0

bees = deque(int(x)for x in input().split())
nectars = deque(int(x)for x in input().split())
operators = deque(input().split())


# def function(a, b):
#     if b > 0:
#         return a / b


operators_dict = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a / b,
    # '/': function
}
while bees and nectars:
    curr_bee = bees.popleft()
    curr_nectar = nectars.pop()

    # if curr_nectar == 0:
    #     continue
    #
    # if curr_bee == 0:
    #     continue

    if curr_nectar >= curr_bee:
        curr_operator = operators.popleft()
        total_honey += abs(operators_dict[curr_operator](curr_bee, curr_nectar))
    else:
        bees.appendleft(curr_bee)

print(f"Total honey made: {total_honey}")

if nectars:
    print(f"Nectar left: {', '.join(str(x)for x in nectars)}")
if bees:
    print(f"Bees left: {', '.join(str(x) for x in bees)}")
