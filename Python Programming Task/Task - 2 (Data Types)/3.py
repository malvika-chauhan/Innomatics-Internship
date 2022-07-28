'''
Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s
) having the second lowest grade.
'''

if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        dic = [name,score]
    print(dict(dic))

