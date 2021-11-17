    #Listas
#Se pueden ampliar y cambiar
milista = ["manzana", "pera", "limon"]

#Acceso a datos
milista[0]

#Longitud de Lista
len(milista)

#Convertir a Lista
estalista = list(("manzana", "pera", "limon"))

#Modificar Lista
estalista[1] = "platano"

#Modificar conjunto de valores
estalista[0:2] = ["manzana", "uva"]

#Sustituir un elemento por varios valores
estalista[1:2] = ["pera", "uva"]

#Añadir elementos al final
estalista.append("tomate")

#Añadir elementos en un index
estalista.insert(1, "lechuga")

#Juntar con iterable
estalista.extend(milista)

#Eliminar un elemento
estalista.remove("lechuga")

#Eliminar por index
estalista.pop(1)
del estalista[0]

#Vaciar lista
estalista.clear()

#Eliminar el ultimo elemento
estalista.pop()

#Ordenar lista
estalista.sort()
estalista.sort(reserve = True)