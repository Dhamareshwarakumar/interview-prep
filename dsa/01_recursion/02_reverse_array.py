def reverse_array(arr, i, n):
    if i >= n:
        return
    arr[i], arr[n - 1] = arr[n - 1], arr[i]
    reverse_array(arr, i + 1, n - 1)

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    reverse_array(arr, 0, len(arr))
    print(arr)