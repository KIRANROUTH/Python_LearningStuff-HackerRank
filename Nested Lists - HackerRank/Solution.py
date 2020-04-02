#Question Link: https://www.hackerrank.com/challenges/nested-list/problem

#My some test case are right but shown wrong.
"""
their output must be in
harry
berry

but mine
berry
harry

both are same but shown as wrong in two test cases.
"""

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

for name_, grade in dicti.items():
    if grade == needed_grade:
        print(name_)
