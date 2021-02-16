#sucecion de fibonachi

n=int(input())
num1=1
num2=1

for i in range(n):
	print(num1)
	temp=num2
	num2=num1
	num1+=temp
