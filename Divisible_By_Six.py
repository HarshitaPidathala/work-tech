'''
problem Statement:
Given a number, find out if it is divisible by 6 or not.

Input Format
There are multiple test cases.

First lines containing the number of test cases T.

Next T lines containing a number each ai.

Output Format
T lines each indicating if the number entered in the ith line is divisible by 6 or not. Print "True" if yes, "False" if no.

Examples
Sample Input
4
457
66
0
40
Expected Output
False
True
True
False
Constraints
0 < T <= 100000
0 <= ai <= 100000

'''
code:
n=int(input())
for i in range(n):
	divisible=int(input())
	if divisible%6==0:
		print("True")
	else:
		print("False")