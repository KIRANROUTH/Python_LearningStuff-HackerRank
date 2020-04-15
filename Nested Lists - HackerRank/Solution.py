#Question Link: https://www.hackerrank.com/challenges/nested-list/problem

students = []

if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
    
dicti = dict(students)
grade = []
for _, grade_ in dicti.items():
    grade.append(grade_)

grade = set(grade)

grade = list(grade)

grade.sort()
needed_grade = grade[1]

i = 0

name = []
for name_, grade in dicti.items():
    
    if grade == needed_grade:
        name.append(name_)

name.sort()

for name in name:
    print(name)