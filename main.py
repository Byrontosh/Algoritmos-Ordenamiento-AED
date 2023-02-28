
def imprimir_Arreglo(arreglo):

  for i in range(len(arreglo)):
    print(f' [{arreglo[i]}]',end="")

def algoritmo_Burbuja(arreglo):
  for i in range(len(arreglo)-1):
    for j in range(len(arreglo)-1-i):
      if arreglo[j] > arreglo[j+1]:
        aux=arreglo[j]
        arreglo[j]=arreglo[j+1]
        arreglo[j+1]=aux



listaSueldos=[20.8,150.5,170.5,180.8,190,30,75.6,200]
print("Lista de sueldos sin ordenar\n\n")
imprimir_Arreglo(listaSueldos)
algoritmo_Burbuja(listaSueldos)
print("\n\nLista de sueldos ordenado\n\n")
imprimir_Arreglo(listaSueldos)