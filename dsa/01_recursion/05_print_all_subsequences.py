def backtrack(index, arr, temp, result):
    if index == len(arr):
        result.append(temp[:])
        return
    temp.append(arr[index])
    backtrack(index + 1, arr, temp, result)
    temp.pop()
    backtrack(index + 1, arr, temp, result)

def getAllSubsequences(arr):
    result = []
    backtrack(0, arr, [], result)
    return result

if __name__ =="__main__":
    print(getAllSubsequences([3,1,2]))