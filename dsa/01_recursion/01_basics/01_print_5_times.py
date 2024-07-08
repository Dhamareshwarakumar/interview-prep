def print_n_times(n):
    if n > 0:
        print("Hello")
        print_n_times(n-1)


if __name__ == "__main__":
    print_n_times(5)

