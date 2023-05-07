import os
import io

ROOT = "./file.dmc"

ERROR = -1
PTOCOMA = 1
EOF = 2
ID = 3
ASIGNAR = 4
NUMERO = 5
COMA  = 6
SUMA = 7
RESTAR = 8
DIV = 9
MULTIPLICACION = 10
ENTERO = 11
CADENA = 12
DOUBLE = 13
BOOLEAN = 14
IF = 15
THEN = 16

letters = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'}
numbres = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
operator = {'+', '*', '/', '-'}

pila = []
index = 10
retorno = ""
lexema = str

def run():
    print("******* Analizador lexico *******")
    
    # Open file
    f = open(ROOT)
    cadena = f.read()
    cadena = cadena[::-1]

    # fill pila
    for e in cadena:
        pila.append(e)


    while len(pila) > 0:
        status = estado1()

        # Responde segun el status
        if (status == ERROR): # Error
            print(f"Error de token\n")
            for c in cadena:
                print(f"Caracter inesperado, linea {index} caracter {c}")
        
        elif (status == PTOCOMA): # Punto y coma
            print(f" Token PTOCOMA\n  Lexema: {lexema}")

        elif (status == EOF): # Fin de cadena
            print(" Token EOF\n  Lexema: \\0")
        
        elif (status == ID): # Identificador
            print(f" Token ID\n  Lexema: {lexema}")

        elif (status == ASIGNAR):
            print(f" Token ASIGNAR\n  Lexema: {lexema}")

        elif (status == NUMERO):
            print(f" Token NUMERO\n  Lexema: {lexema}")

        elif (status == COMA):
            print(f" Token COMA\n  Lexema: {lexema}")

        elif (status == SUMA):
            print(f" Token SUMA\n  Lexema: {lexema}")

        elif (status == RESTAR):
            print(f" Token PRESTAR\n  Lexema: {lexema}")

        elif (status == DIV):
            print(f" Token DIVICION\n  Lexema: {lexema}")

        elif (status == MULTIPLICACION):
            print(f" Token MULTIPLICACION\n  Lexema: {lexema}")

        elif (status == ENTERO):
            print(f" Token ENTERO\n  Lexema: {lexema}")

        elif (status == CADENA):
            print(f" Token CADENA\n  Lexema: {lexema}")

        elif (status == DOUBLE):
            print(f" Token DOUBLE\n  Lexema: {lexema}")

        elif (status == BOOLEAN):
            print(f" Token BOOLEAN\n  Lexema: {lexema}")

        elif (status == IF):
            print(f" Token IF\n  Lexema: {lexema}")

        elif (status == THEN):
            print(f" Token THEN\n  Lexema: {lexema}")

    

def estado1():
    global lexema
    c = pila.pop()
    lexema = c
    # print(c)

    if c == ';':
        return estado2()

    elif c == '\0':
        return estado3()

    elif c == '+':
        return estado10()

    elif c == '-':
        return estado11()

    elif c == '*':
        return estado12()

    elif c == '/':
        return estado13()

    elif c == ',':
        return estado9()

    elif c == '=':
        return estado6()

    elif c == 'i': # Integer
        return estado14()

    elif c == 'S': #String
        return estado17()

    elif c == 'b': # Boolean
        return estado23()

    elif c == 'd': # Double
        return estado30()

    # Compare 'c' with letters
    for e in letters:
        if e == c:
            return estado4()

    # Compare 'c' with numbers
    for e in numbres:
        return estado7()
    
    return ERROR

def estado2():
    return PTOCOMA

def estado3():
    return EOF

def estado4():
    global lexema
    c = pila.pop()

    lexema = lexema + c

    for i in letters:
        if i == c:
            return estado4()
    
    for n in numbres:
        if n == c:
            return estado4()

    # Delete last char
    lexema = lexema[: len(lexema) - 1]  
    return estado5(c)

def estado5(c):
    pila.append(c)
    retorno = c
    return ID

def estado6():
    return ASIGNAR

def estado7():
    pass

def estado8():
    pass

def estado9():
    return COMA

def estado10():
    return SUMA

def estado11():
    return RESTAR

def estado12():
    return MULTIPLICACION

def estado13():
    return DIV

def estado14():
    pass

def estado15():
    pass

def estado16():
    pass

def estado17():
    pass

def estado18():
    pass

def estado19():
    pass

def estado20():
    pass

def estado21():
    pass

def estado22():
    pass

def estado23():
    pass

def estado24():
    pass

def estado25():
    pass

def estado26():
    pass

def estado27():
    pass

def estado28():
    pass

def estado29():
    pass

def estado30():
    pass

def estado31():
    pass

def estado32():
    pass

def estado33():
    pass

def estado34():
    pass

def estado35():
    pass

def estado36():
    pass

def estado37():
    pass

def estado38():
    pass

if __name__ == '__main__':
    run()