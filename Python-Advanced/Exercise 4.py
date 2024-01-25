n = int(input())
mtrx = [[j for j in input().split()] for i in range(n)]

alisa_row, alisa_col = 0, 0

directions = {
    "right": lambda r, c: (r, c + 1),
    "left": lambda r, c: (r, c - 1),
    "up": lambda r, c: (r - 1, c),
    "down": lambda r, c: (r + 1, c)
}

for row in range(n):
    for col in range(n):
        if mtrx[row][col] == 'A':
            alisa_row, alisa_col = row, col

tea = 0
while tea < 10:
    command = input()
    next_row, next_col = directions[command](alisa_row, alisa_col)
    curr_el = mtrx[alisa_row][alisa_col]
    mtrx[alisa_row][alisa_col] = '*'
    # alisa_row, alisa_col = next_row, next_col

    if curr_el.isdigit():
        tea += int(curr_el)

    elif curr_el == 'R' or next_row not in range(n) and next_col not in range(n):
        # mtrx[alisa_row][alisa_col] = '*'
        print("Alice didn't make it to the tea party.")
        [print(*row) for row in mtrx]
        break

    alisa_row, alisa_col = next_row, next_col

if tea > 9:
    # mtrx[alisa_row][alisa_col] = '*'
    print("She did it! She went to the party.")
    [print(*row) for row in mtrx]
