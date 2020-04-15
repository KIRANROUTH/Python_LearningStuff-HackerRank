#Question Link: https://www.hackerrank.com/challenges/finding-the-percentage/problem?h_r=next-challenge&h_v=zen
n = int(input())

dicti = dict()

for _ in range(n):
    name, math, physics, chemistry = input().split(" ")
    dicti[name] = [float(math), float(physics), float(chemistry)]

targetname = str(input())

for name, marks in dicti.items():
    if name == targetname:
        result = float(sum(marks)/len(marks))
        print("{:0.2f}".format(result))
