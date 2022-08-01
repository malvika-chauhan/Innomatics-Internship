'''

You are given a string .
Your task is to find out if the string  contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.


'''

if __name__ == '__main__':
    s = input()  
    print(any(map(str.isalnum,s)))
    print(any(map(str.isalpha,s)))
    print(any(map(str.isdigit,s)))
    print(any(map(str.islower,s)))
    print(any(map(str.isupper,s)))
   
