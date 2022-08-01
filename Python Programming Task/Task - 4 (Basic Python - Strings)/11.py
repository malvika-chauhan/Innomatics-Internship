'''

You are given an integer, N. Your task is to print an alphabet rangoli of size N . (Rangoli is a form of Indian folk art based on creation of patterns.)


'''

import string
def print_rangoli(size):
    # your code goes here
    alpha = string.ascii_lowercase
    for i in range(size):
        s = "-".join(alpha[i:size])
        L.append((s[::-1]+s[1:]).center(4*n-3, "-"))

        print(s)
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)