import random
import datetime
nombres=[["elisa","david", "diego", "jorge", "bryan", "edwin" , "pablo","kevin","oscar","maria","rocio","juana"],["abeja","araña","burro","cabra","cebra","cerdo","cisne","eriz","gallo","mosca","perro","pulpo","raton","zorro"],["chile","china","india","malta","siria","tunez","rusia","suiza","haiti","japon"]] #TABLA CON LAS CATEGORIAS
categorias={1:"Nombres de personas",2:"Nombres de animales",3:"Nombres de Paises"} #DICCIONARIO CON LAS TEMATICAS
class bcolors:             #APARTADO PARA TENER SALIDAS CON COLORES, CONSULTADAS EN https://www.delftstack.com/es/howto/python/python-print-colored-text/
    OK = '\033[92m' #Color verde
    FAIL = '\033[91m' #Color Rojo
    WARNING = '\033[93m' #YELLOW
    RESET = '\033[0m' #Color Original
def ColorearVerde(letra):  #Función para imprimir string de color verde
    return bcolors.OK+letra+bcolors.RESET
def ColorearRojo(letra):      #Función para imprimir string de color rojo
    return bcolors.FAIL+letra+bcolors.RESET
def ColorearAmarillo(letra):       #Función para imprimir string de color amarillo
    return bcolors.WARNING+letra+bcolors.RESET
var="si"                 #Variable para determinar cuando jugar y cuando parar
while var.lower()=="si":                          
    date=datetime.datetime.now()
    print(ColorearRojo("FECHA:"),date.strftime("%Y-%m-%d"))           #Datetime para conocer la fecha actual
    print(ColorearAmarillo("ELIJE UNA DE LAS SIGUIENTES TEMÁTICAS: "))           #Interfaz para que el usuario pueda elegir la tematica
    print(ColorearVerde("Digite 1, Para escoger la temática de nombres de personas"))
    print(ColorearVerde("Digite 2, Para escoger la temática de nombres de animales"))
    print(ColorearVerde("Digite 3, Para escoger la temática de nombres de paises"))
    opcion=int(input("Ingrese el numero aqui: "))                   
    correcto=random.choice(nombres[opcion-1])          #Uso de choice de la libreria random para escoger una palabra al azar de la tematica elegida por el usuario
    print(ColorearRojo("INSTRUCCIONES DEL JUEGO"))                        #INSTRUCCIONES
    print(ColorearAmarillo('DEBES ADIVINAR UNA PALABRA RESPECTO A LA TEMATICA'),ColorearRojo(categorias[opcion].upper()),ColorearAmarillo('QUE ESTA CONFORMADA POR 5 LETRAS'))
    print(ColorearVerde("Si en la palabra ingresada hay una letra de la palabra a adivinar en la posicion correcta se marcara con verde."))
    print(ColorearRojo("Si en la palabra hay una letra de la palabra a adivinar en la posicion incorrecta se marcara con rojo."))
    print("Si la letra no hace parte del nombre no se va marcar de algún color.")
    print("Tienes 6 oportunidades")
    inicio=datetime.datetime.now()                        #inicio para conocer el tiempo empleado por usuario al jugar, se empieza a contar a partir de tener las instrucciones
    for i in range(6):               #Ciclo con un rango de 6, que representa las oportunidades 
        sol,pal=[],[]                        #listas para almacenar la palabra que vaya ingresando el usuario como la que esta intentnado adivinar
        print()
        nombre=input("Ingresa una palabra de 5 letras: ")                   #Se le pide al usuario que ingrese la palabra a adivinar
        print()
        while not (len(nombre)==5):                                    #Si la palabra no tiene 5 letras, se le pide que la vuelva a ingresar hasta que las tenga
            nombre=input("Error! Debes Ingresar una palabra de 5 letras: ")
        if correcto==nombre.lower():                                    #Se convierte a minuscula por si el usuario la ingresa en mayuscula
            break                                                       #Si la llega advinar se termina
        else:
            for letra in correcto:                                      #De lo contrario se almacena la letra en las listas
                sol.append(letra)
            for letra in nombre:
                pal.append(letra)
        for i in range(5):                                              #Se empieza  a mirar que letras de la plabra ingresada concuerdan con la palabra a adivinar
            if pal[i] in sol[i]:                                         #Si la letra de la palabra ingresada esta en la misma posicion de la plabra a adivinar se pinta de verde
                print(ColorearVerde(pal[i]), end="")                    #El end es para que imprima las letras de manera horizontal
            if not pal[i] in sol:                                            #Si la letra no hace parte de la palabra a adivinar no se colorea solo se imprime
                print(pal[i], end="")                                           
            elif pal[i] in sol and not (pal[i] in sol[i]):         #Si la letra de la palabra ingresada esta en la palabra pero no en la posicion correcta se pinta de rojo
                print(ColorearRojo(pal[i]), end="")
    print()
    if nombre.lower()==correcto:                                            #Se toma cuando acabe y adivine la palabra
        final=datetime.datetime.now()                                       #Tiempo final cuando adivina la palabra
        print(ColorearVerde(nombre))                                                
        print(ColorearAmarillo("HAS GANADO LA PALABRA ES CORRECTA"))
        dif= final-inicio
        print(ColorearRojo("El tiempo empleado fue de: "),round(dif.total_seconds(),2),"Segundos")    #Se imprime el tiempo empleado en segundos redondeado a dos decimales
    else:                                                                               #Si la persona no la adivino en los 6 intentos se le indica que perdio
        print("PERDISTE :(")
        print("Se te han acabado las oportunidades")
    var=input("Deseas volver a jugar? Escribe si o no: ")                            #Se le da la opcion al usuario de volver a jugar
    while not var.lower() in ["si","no"]:
        var=input("Error! Introduce si o no: ")
print(ColorearRojo("FIN DEL JUEGO"))
        
            




