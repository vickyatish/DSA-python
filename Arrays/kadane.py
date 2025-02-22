import sys

def maxSubArray(arr):
    maxi = -sys.maxsize-1
    sum = 0
    start, end = -1, -1

    for i in range(len(arr)):
        if sum==0:
            start = i

        sum+=arr[i]

        if sum>maxi:
            maxi = sum
            end = i

        if sum<0:
            sum = 0

    return ["max sum = ", maxi, "in [ ",start, ",", end, " ]"]

if __name__ == '__main__':
    arr = [-2,1,-3,4,-1,2,1,-5,4]
    print(maxSubArray(arr))