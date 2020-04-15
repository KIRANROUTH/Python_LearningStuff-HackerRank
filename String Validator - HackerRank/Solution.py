#Question Link: https://www.hackerrank.com/challenges/string-validators/problem

string = input()
print(any(val.isalnum()  for val in string))
print(any(val.isalpha() for val in string))
print(any(val.isdigit() for val in string))
print(any(val.islower() for val in string))
print(any(val.isupper() for val in string))
