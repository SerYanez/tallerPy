# PROGRAMA BÁSICO DE REGISTRO DE GASTO DIARIO
#
# Bienvenida al programa

# Se solicita al usuario que ingrese el monto del gasto que quisiera registrar, guardando el
#valor en una variable

# Se pide que ingrese la categoría del gasto, guardándola en una variable distinta

# Se solicita ingresar una descripción del gasto, que se guarda en su variable correspondiente

# Se consulta la fecha del gasto, primero día, después mes y por último año. Se guarda cada
#valor en una variable diferente para evitar conflicto de formato

# Al finalizar el ingreso de datos, se muestra todo lo ingresado con las relaciones correspondientes


#BIENVENIDA
print(f"Hola! Anotemos el gasto que tuviste! \nSolo necesito hacerte unas preguntitas:")

#Consulta por el monto
monto = float(input("De cuánto fue el gasto? $"))

#Consulta por la categoría
categoria = input("A qué corresponde? ")

#Pedido de descripción
descripcion = input("Describe en qué se gastó: ")

#Ingreso de fecha
dia = input("Ingrese día (ej.: 07): ").strip()
mes = input("Ingrese mes (ej.: 11): ").strip()
anio = input("Ingrese año (ej.: 1995): ").strip()

fecha = dia + "/" + mes + "/" + anio

#Se muestran los datos
print(f"El gasto de {fecha} fue : ${monto} \nEsto fue en {categoria}, más específicamente en {descripcion}")
input()

##########NOTAS#########
# Hay maneras de romper este programa, pero sin usar estructuras de control y manejo de errores es difícil
# remediar esto.
# Se podría llegar a prevenir el uso de letras en la fecha o el monto colocando condicionales que insten
# al usuario a volver a ingresar el dato de la manera correspondiente.
# Se podría llegar a hacer mucho más completo el programa usando una base de datos que lleve un registro
# real y no se pierdan los datos cada vez que se usa. También con esto se podría diferenciar entre
# categorías y hacer un análisis de gastos más detallado.