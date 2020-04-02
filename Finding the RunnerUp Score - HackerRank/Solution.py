#Question Link: https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    set_arr = set(arr)
    new_arr = list(set_arr)
    new_arr.sort(reverse = True)
    print(new_arr[1])
