def is_palindrome(string, i, n):
    if i >= n:
        return True
    if string[i] != string[n]:
        return False
    return is_palindrome(string, i + 1, n - 1)

if __name__ == '__main__':
    string = "MADAM"
    print(is_palindrome(string, 0, len(string) - 1))