'''

In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left.

'''
def count_substring(string, sub_string):
    c =0
    while sub_string in string:
        c+=1
        string = string[string.find(sub_string)+1:]
    return(c)

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)