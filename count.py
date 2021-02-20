#mi propia funcion/metodo count

def count(objet,sentencia):
	contador=0
	for i in objet:
		if i==sentencia:
			contador+=1

	return contador
#prueba
v=[1, 2, 2, 4, 7]
print(count(v, 2))
