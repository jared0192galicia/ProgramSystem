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
operators = {'+', '*', '/', '-'}

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
        if e != ' ':
            pila.append(e.lower())


    while len(pila) > 0:
        status = estado1()
        # print(f'status {status} : numero {ENTERO}')
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

    elif c == 's': #String
        return estado17()

    elif c == 'b': # Boolean
        return estado23()

    elif c == 'd': # Double
        return estado30()

    # Compare 'c' with letters
    for e in letters:
        if e == c:
            # print("In letters")
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
    if len(pila) > 0:
        c = pila.pop()
    else:
        return estado5()

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
    return ID

def estado6():
    return ASIGNAR

def estado7():
    global lexema
    c = pila.pop()

    lexema = lexema + c

    for n in numbres:
        if n == c:
            return estado7()
        
    return estado8(c)

def estado8(c):
    pila.append(c)
    return NUMERO

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
    global lexema
    c = pila.pop()

    lexema = lexema + c

    if c == 'n':
        return estado15()
    
    elif c == 'f':
        return estado37()

    for l in operators:
        if c == l:
            return estado5()

    lexema = lexema[: len(lexema) - 1]
    return estado4()

def estado15():
    global lexema
    c = pila.pop()

    lexema = lexema + c
    if c == 't':
        return estado16()
    
    for l in operators:
        if c == l:
            return estado5(c)

    lexema = lexema[: len(lexema) - 1]
    return estado4()

def estado16():
    return ENTERO

def estado17():
    global lexema
    c = pila.pop()
    lexema = lexema + c

    if c == 't':
        return estado18()
        
    for l in operators:
        if c == l:
            return estado5(c)

    lexema = lexema[: len(lexema) - 1]
    return estado4()
    


def estado18():
    global lexema
    c = pila.pop()
    lexema = lexema + c

    if c == 'r':
        return estado19()
        
    for l in operators:
        if c == l:
            return estado5(c)

    lexema = lexema[: len(lexema) - 1]
    return estado4()

def estado19():
    global lexema
    c = pila.pop()
    lexema = lexema + c

    if c == 'i':
        return estado20()
        
    for l in operators:
        if c == l:
            return estado5(c)

    lexema = lexema[: len(lexema) - 1]
    return estado4()

def estado20():
    global lexema
    c = pila.pop()
    lexema = lexema + c

    if c == 'n':
        return estado21()
        
    for l in operators:
        if c == l:
            return estado5(c)

    lexema = lexema[: len(lexema) - 1]
    return estado4()

def estado21():
    global lexema
    c = pila.pop()
    lexema = lexema + c

    if c == 'g':
        return estado22()
        
    for l in operators:
        if c == l:
            return estado5(c)

    lexema = lexema[: len(lexema) - 1]
    return estado4()

def estado22():
    return CADENA

def estado23():
    global lexema
    c = pila.pop()
    lexema = lexema + c

    if c == 'o':
        return estado24()
        
    for l in operators:
        if c == l:
            return estado5(c)

    lexema = lexema[: len(lexema) - 1]
    return estado4()

def estado24():
    global lexema
    c = pila.pop()
    lexema = lexema + c

    if c == 'o':
        return estado25()
        
    for l in operators:
        if c == l:
            return estado5(c)

    lexema = lexema[: len(lexema) - 1]
    return estado4()

def estado25():
    global lexema
    c = pila.pop()
    lexema = lexema + c

    if c == 'l':
        return estado26()
        
    for l in operators:
        if c == l:
            return estado5(c)

    lexema = lexema[: len(lexema) - 1]
    return estado4()

def estado26():
    global lexema
    c = pila.pop()
    lexema = lexema + c

    if c == 'e':
        return estado27()
        
    for l in operators:
        if c == l:
            return estado5(c)

    lexema = lexema[: len(lexema) - 1]
    return estado4()

def estado27():
    global lexema
    c = pila.pop()
    lexema = lexema + c

    if c == 'a':
        return estado28()
        
    for l in operators:
        if c == l:
            return estado5(c)

    lexema = lexema[: len(lexema) - 1]
    return estado4()

def estado28():
    global lexema
    c = pila.pop()
    lexema = lexema + c

    if c == 'n':
        return estado29()
        
    for l in operators:
        if c == l:
            return estado5(c)

    lexema = lexema[: len(lexema) - 1]
    return estado4()

def estado29():
    return BOOLEAN

def estado30():
    global lexema
    c = pila.pop()
    lexema = lexema + c

    if c == 'o':
        return estado31()
        
    for l in operators:
        if c == l:
            return estado5(c)

    lexema = lexema[: len(lexema) - 1]
    return estado4()

def estado31():
    global lexema
    c = pila.pop()
    lexema = lexema + c

    if c == 'u':
        return estado32()
        
    for l in operators:
        if c == l:
            return estado5(c)

    lexema = lexema[: len(lexema) - 1]
    return estado4()

def estado32():
    global lexema
    c = pila.pop()
    lexema = lexema + c

    if c == 'b':
        return estado33()
        
    for l in operators:
        if c == l:
            return estado5(c)

    lexema = lexema[: len(lexema) - 1]
    return estado4()

def estado33():
    global lexema
    c = pila.pop()
    lexema = lexema + c

    if c == 'l':
        return estado34()
        
    for l in operators:
        if c == l:
            return estado5(c)

    lexema = lexema[: len(lexema) - 1]
    return estado4()

def estado34():
    global lexema
    c = pila.pop()
    lexema = lexema + c

    if c == 'e':
        return estado35()
        
    for l in operators:
        if c == l:
            return estado5(c)

    lexema = lexema[: len(lexema) - 1]
    return estado4()

def estado35():
    return DOUBLE

def estado36():
    return ERROR

def estado37():
    return IF

# Entry point
if __name__ == '__main__':
    run()