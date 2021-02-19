#mi propia funcion/metodo find

def find(string, busqueda):
	posicion=0
	for i in string:
		if i==busqueda:
			return posicion
		posicion+=1
		

#prueba
p='Hola mundo'
print(find(p, 'H'))
