# funcion len propia
def len(objeto):
    contador=0
    for i in objeto:
        contador+=1
    return contador

print (len([1, 2,3,4]))
print (len ("hola"))
