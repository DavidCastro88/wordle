import random
import datetime
def tiempo_gastado(start,end): #Función para calcular el tiempo en que se demora en adivinar el Pais
    time=end-start
    time=time.total_seconds()
    return(round(time))
class coloresAISI:             #APARTADO PARA TENER SALIDAS CON COLORES, CONSULTADAS EN https://www.delftstack.com/es/howto/python/python-print-colored-text/
    OK = '\033[92m' #Color verde
    WARNING = '\033[93m' #Color Amarillo
    RESET = '\033[0m' #Color Original
def Colorear(letra,color): #Funcion Colorear que recibe como parametro el string  texto, y el color con el que se va colorear (VERDE o Amarillo)
    if color=="verde":  
        return coloresAISI.OK+letra+coloresAISI.RESET
    else:
        return coloresAISI.WARNING+letra+coloresAISI.RESET
paises=[["chile","ghana","china","kenia","india","malta","siria","tunez","rusia","suiza","haiti","japon"],["mexico","monaco","belize","brazil","canada","egipto","grecia","israel","angola","italia","panama","ruanda","serbia","zambia"],["polonia","algeria","albania","andorra","bolivia","austria","croacia","ecuador","francia","liberia","nigeria","noruega"]]  #Tabla con la las listas de los paises que se van a usar tomados por numero de letras
X="V"                 #Variable para determinar cuando jugar y cuando parar
while X.upper()=="V":                          
    print(Colorear("REGLAS DEL JUEGO","amarillo"))    #SE INDICAN LAS REGLAS
    print(Colorear('DEBERAS DE ADIVINAR EL NOMBRE DE UN PAIS COMPUESTO POR EL NUMERO DE LETRAS QUE DESEES',"amarillo"))
    print(Colorear("ELIJE LA CANTIDAD DE LETRAS QUE QUIERES QUE CONTENGA EL PAIS: ","amarillo")) 
    print(Colorear("Digite 5, Para tener que adivinar un pais de 5 letras","verde"))
    print(Colorear("Digite 6, Para tener que adivinar un pais de 6 letras","verde"))
    print(Colorear("Digite 7, Para tener que adivinar un pais de 7 letras","verde"))
    numero=int(input("Ingrese el numero aqui: "))                   
    paisADIV=random.choice(paises[numero-5]) #SE USA CHOICE PARA ELEGIR UN PAIS DEPENDIENDO DEL NUMERO DE LETRAS
    print(Colorear("Si en la palabra ingresada hay una letra del pais a adivinar en la posicion correcta se marcara con verde.","verde"))
    print(Colorear("Si en la palabra hay una letra del pais a adivinar en la posicion incorrecta se marcara con amarillo.","amarillo"))
    print("Si la letra no hace parte del pais no se va marcar.")
    print(f'Tienes {numero} oportunidades')
    inicio=datetime.datetime.now()  #SE EMPIEZA A MEDIR EL TIEMPO QUE SE TARDARA EN ADIVINAR LA PALABRA
    for i in range(numero):               #Ciclo con un rango dependiendo del numero de letras, que representa las oportunidades 
        adivinar,advinada=[],[]   #LISTAS PARA ALMACENAR LAS LETRAS
        print()
        pais=input(f'Ingresa un pais de {numero} letras en minuscula: ')    #SE LE PIDE AL USUARIO QUE ADVINE EL PAIS
        print()
        while not (len(pais)==numero):         
            pais=input(f'Error! Debes Ingresar un pais de {numero} letras en minuscula: ') #FILTRO PARA QUE EL PAIS SI SEA DE LAS LETRAS ELEGIDAS
        if paisADIV==pais.lower():                                    #SI LO ADIVINA SE CORTA EL CICLO
            break                                                      
        else:
            for elemento in paisADIV:                                      
                adivinar.append(elemento)
            for elemento in pais:
                advinada.append(elemento)
        for i in range(numero):         
            if advinada[i] in adivinar[i]:       #CONDICION PARA SABER SI LA LETRA ESTA Y EN LA POSICION CORRECTA                                  
                print(Colorear(advinada[i],"verde"), end="")                   
            if not advinada[i] in adivinar:            #CONDICION POR SI LA LETRA NO ESTA EN LA PALABRA
                print(advinada[i], end="")                                           
            elif advinada[i] in adivinar and not (advinada[i] in adivinar[i]):   #CONDICION PARA SABER SI LA LETRA ESTA PERO NO EN LA POSICION CORRECTA
                print(Colorear(advinada[i],"amarillo"), end="")
    print()
    if pais.lower()==paisADIV:                       #SI ACIERTA EL PAIS SE LE MANDA UN MENSAJE Y SE PREGUNTA SI QUIER VOLVER A JUGAR
        final=datetime.datetime.now()                                       
        print(Colorear(pais,"verde"))                                                
        print(Colorear("HAS ACERTADO EL PAIS, FELICIDADES!","amarillo"))
        print(Colorear("TU TIEMPO PARA ADIVINAR LA PALABRA FUE DE: ","amarillo"),tiempo_gastado(inicio,final),"Segundos") #TIEMPO QUE SE DEMORO EN ADIVINAR 
    else:        #SI NO ADIVINA SE LE NOTIFICA Y SE LE PREGUNTA SI QUIER VOLVER A JUGAR
        print("SE TE ACABARON LOS INTENTOS,VUELVE A INTENTARLO")
    X=input("Quieres volverlo a intentar? Escribe V para volverlo a intentar o F de lo contrario: ")                            
    while not X.upper() in ["V","F"]:
        X=input("Error! Escribe V para volverlo a intentar o F de lo contrario: ")
print(Colorear("GRACIAS POR JUGAR","amarillo"))