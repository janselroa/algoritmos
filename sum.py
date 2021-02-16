# mi propia funcion  sum

def sum(array):
	suma=0
	for i in array:
		suma+=i

	return suma

#prueba
l=[1, 3, 5, 6, 10]
print(sum(l))