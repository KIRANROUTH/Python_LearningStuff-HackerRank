#Question Link: https://www.hackerrank.com/challenges/designer-door-mat/problem

row, column = input().split(" ")
row, column = int(row), int(column)
c = ".|."
i = 0
for x in range(1, (row - 1)//2 + 1):
    print((c*(x + i)).center(column, "-"))
    i += 1

print(("WELCOME").center(column, "-"))

for y in range((row - 1)//2, 0, -1):
    i -= 1
    print((c*(y + i)).center(column, "-"))
