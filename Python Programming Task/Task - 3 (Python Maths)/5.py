'''

You are given three integers: , , and . Print two lines.
On the first line, print the result of pow(a,b). On the second line, print the result of pow(a,b,m).

'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
a=input()
b=input()
m=input()
print(pow(int(a),int(b)),pow(int(a),int(b),int(m)),sep='\n')
