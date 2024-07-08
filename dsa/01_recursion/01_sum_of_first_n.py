def sum_of_first_n(n):
    if (n < 1):
        return 0
    return n + sum_of_first_n(n - 1)
    

if __name__ == "__main__":
    print(sum_of_first_n(10))