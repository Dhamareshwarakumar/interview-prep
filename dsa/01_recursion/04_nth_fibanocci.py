def fibanocci(n):
    if n < 1:
        return -1
    if n <= 2:
        return n - 1
    return fibanocci(n - 1) + fibanocci(n - 2)

if __name__ == '__main__':
    n = 1
    print(fibanocci(n))