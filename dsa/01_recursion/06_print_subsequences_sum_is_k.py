def backtrack(index, arr, temp, result, k):
    if (index == len(arr)):
        if (sum(temp) == k):
            result.append(temp[:])
        return
    temp.append(arr[index])
    backtrack(index + 1, arr, temp, result, k)
    temp.pop()
    backtrack(index + 1, arr, temp, result, k)

def k_sum_subsequences(arr, k):
    result = []
    backtrack(0, arr, [], result, k)
    return result

if __name__ == '__main__':
    # n = int(input())                        
    n = 9
    # arr = list(map(int, input().split()))
    arr = [1,2,3,4,5,6,7,8,9]
    # k = int(input())
    k = 10

    print(k_sum_subsequences(arr, k))