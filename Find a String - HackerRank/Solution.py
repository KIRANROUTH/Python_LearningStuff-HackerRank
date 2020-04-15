#Question Link: https://www.hackerrank.com/challenges/find-a-string/problem?isFullScreen=false
def count_substring(string, sub_string):
    times = 0
    index = 0
    while sub_string in string[index:]:
        times += 1
        index = string.index(sub_string)
        lstring = list(string)
        lstring.remove(lstring[index])
        string = "".join(lstring)
        
    return times

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
