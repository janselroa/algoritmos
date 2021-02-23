l=[1, 2, 4, 5, 6]

def index(array, sentencia):
	pocicion=0
	for i in array:
		if i==sentencia:
			return pocicion
			break

		pocicion+=1

print(index(l, 1))
