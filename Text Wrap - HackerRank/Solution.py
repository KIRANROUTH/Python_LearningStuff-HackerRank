#Question Link: https://www.hackerrank.com/challenges/text-wrap/problem
import textwrap

def wrap(string, max_width):
    test = textwrap.wrap(string, max_width)
    val = "\n".join(test)
    return val

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
