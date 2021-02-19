#mi propia funcion/metodo find

def find(sentencia, busqueda):
	posicion=0
	for i in sentencia:
		if i==busqueda:
			return posicion
		posicion+=1
		

#prueba
p='Hola mundo'
print(find(p, 'H'))
