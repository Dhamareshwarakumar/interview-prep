def print_upto_n(n):
    if (n>0):
        print_upto_n(n-1)
        print(n)

if __name__ == "__main__":
    print_upto_n(5)