__author__ = 'a4'
import random
t1 = "trivaganzo","korioto","castillo","esquina","plomo","estrellas","susana","horia","elvio","lado","dino",\
    "soperga","rex","anderon","cañada","nuñez","pantano","interpalaza","victoria","yrigoyen"

def validate(tipo,inf,sup,mensaje):
    n = inf
    while n <= inf or n > sup:
        n = tipo(input(mensaje))
        if n <= inf or n > sup:
            print("VALOR INCORRECTO")
    return n


def read_hoteles_man(v1,v2,v3,v4):
    n = len(v1)
    for i in range(n):
        v1[i] = input("ingrese el nombre de hotel "+str(i+1)+" :")
        if i == (n-1):
            for i in range(n):
                v2[i] = validate(float,-1,10000,"ingrese el precio[1] del hotel "+str(v1[i])+": $")
                v3[i] = validate(float,-1,10000,"ingrese el precio[2] del hotel "+str(v1[i])+": $")
                v4[i] = validate(float,-1,10000,"ingrese el precio[3] del hotel "+str(v1[i])+": $")
                print("="*30)

def read_precio(v):
    n = len(v)
    for i in range(n):
        v[i] = validate(float,-1,99999999999.99,"ingrese el precio del hotel "+str(i+1)+" :$")
    return v

def read_aut(v1,v2,v3,v4):
    n = len(v1)
    for i in range(n):
        v1[i] = t1[i]
        v2[i] = random.randint(0,10000)
        v3[i] = random.randint(0,10000)
        v4[i] = random.randint(0,10000)


def menu_opc():
    print('------------ MENU DE OPCIONES ----------------\n'
    '1-resultados de la busqueda\n'
    '2-cantidad de hoteles disponibles y porcentaje sobre el total.\n'
    '3-mejor precio y sugerencias de los hoteles.\n'
    '4-hoteles disponibles en los tres sitios(despegar,booking,expedia)\n'
    '5-tabla de precios\n'
    '6-ofertas especiales\n'
    '7-presupuesto limitado\n'
    '8-mejor precio\n'
    '9-salir')

def mostrar(n,p1,p2,p3):
    texto = "Hotel          Despegar  Booking  Expedia\n"
    texto += ("-" * 30) + "\n"
    for i in range(len(n)):
        texto += '{:<15}'.format(n[i])
        texto += "$"'{:>5}'.format(p1[i])
        texto += '{:>10}'.format(p2[i])
        texto += '{:>9}'.format(p3[i])
        texto += '\n'
    print(texto)


def disponibilidad(s1,s2,s3):
    c1 = c2 = c3 = 0
    tam = len(s1)
    for i in range(tam):
        if s1[i] != 0:
            c1 += 1
        if s2[i] != 0:
            c2 += 1
        if s3[i] != 0:
            c3 += 1
    porc_s1 = c1 * 100 / tam
    porc_s2 = c2 * 100 / tam
    porc_s3 = c3 * 100 / tam
    return c1,c2,c3,porc_s1,porc_s2,porc_s3


def test():
    mejor_precio = 0.0
    n = validate(int,0,20,"ingrese la cantidad de hoteles:")
    h = [None] * n
    precios_des = [0] * n
    precios_boo = [0] * n
    precios_esp = [0] * n
    carga = validate(int,0,2,"forma de cargar: ingrese '1'(manual) o '2'(automatico):")

    if carga == 1:
        read_hoteles_man(h,precios_des,precios_boo,precios_esp)
    elif carga == 2:
        read_aut(h,precios_des,precios_boo,precios_esp)


    opc = -1
    while opc != 9:
        menu_opc()
        opc = int(input('ingrese la opcion a elegir: '))
        if opc == 1:
            mostrar(h,precios_des,precios_boo,precios_esp)
        elif opc == 2:
            c1,c2,c3,por1,por2,por3=disponibilidad(precios_des,precios_boo,precios_esp)
            print("en el sitio despegar ,hay",c1,"hoteles disponibles y representa",round(por1,2),"%")
            print("en el sitio booking ,hay",c2,"hoteles disponibles y representa",round(por2,2),"%")
            print("en el sitio expedia ,hay",c3,"hoteles disponibles y representa",round(por3,2),"%")
        elif opc == 3:
            hotel = input("ingrese el nombre de un hotel (en minuscula porfavor):")
            if hotel in h:
                for i in range(n):
                        if h[i] == hotel:
                            if precios_des != 0 and precios_boo != 0 and precios_esp != 0:
                                mejor_precio = min(precios_des[i],precios_boo[i],precios_esp[i])

                print("el mejor precio para el hotel",hotel,"es :$",mejor_precio)
            else:
                print("el hotel ingresado NO exite")

        elif opc == 4:
            pass
        elif opc == 5:
            pass
        elif opc == 6:
            pass
        elif opc == 7:
            pass
        elif opc == 8:
            pass
        elif opc == 9:
            print('fin del programa')
        else:
            print('Error, ingrese una de las opciones anteriores...,')


test()


