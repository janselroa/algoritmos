def reverse(array):
	longitud=len(array)-1
	for i in range(0, longitud):
	        temp=array[i]
		array[i]=array[i+1]
		array[i+1]=temp

	return array


#prueba
print(reverse([1, 2, 3]))
