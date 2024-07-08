def print_upto_one(n):
    if n > 0:
        print(n)
        print_upto_one(n-1)

if __name__ == "__main__":
    print_upto_one(5)