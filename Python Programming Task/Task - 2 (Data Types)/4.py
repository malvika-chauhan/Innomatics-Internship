'''
The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. Print the average of the marks array for the student name provided, showing 2 places after the decimal.
'''

if __name__ == '__main__':
    n = int(input())
    mydict = {}
    for line in range(n):
        info = input().split(" ")
        name,score = info[0],info[1:]
        scores = map(float,score)
        mydict[name] = scores
    query_name = input()
    query_score = mydict[query_name]
    l = len(list(query_score))
    print("{0:.2f}".format(sum(query_score)/l))
