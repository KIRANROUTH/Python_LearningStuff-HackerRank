#Question Link: https://www.hackerrank.com/challenges/swap-case/problem.

def swap_case(s):
    str_ = ""
    for letter in s:
        if letter.isupper():
            str_ += letter.lower()
        elif letter.islower():
            str_ += letter.upper()
        else:
            str_ += letter

    return str_

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
