import io

numbres = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
# File read
ROOT = "./file.dmc"

# codes for tokens
ERROR = -1
NOTACION = 1

# vars
pila = []
retorno = ""
lexema = str

def run():
    print("******* Analizador lexico: Notacion cientifica *******")
    
    # Open file
    f = open(ROOT)
    cadena = f.read()
    cadena = cadena[::-1]
    
    # fill pila
    for e in cadena:
        if e != ' ':
            pila.append(e.upper())


    # while len(pila) > 0:

    status = estado1()

    if (status == ERROR): # Error
        print(f"Error de token\n caracter no esperado {lexema}")
        # for c in cadena:
        print(f"syntax error")
    
    elif (status == NOTACION): # Punto y coma
        print(f" Token NOTACION\n\tLexema: {lexema}\n\tRetorno: {retorno}")


def estado1():
    global lexema
    # print("edo 1")
    c = pila.pop()
    lexema = c

    if c == '+' or c == '-':
        return estado2()
    else:
        return estado8(c)
    
def estado2():
    global lexema
    # print("edo 2")
    c = pila.pop()
    lexema = lexema + c
    
    for i in numbres:
        if c == i:
            return estado3()
    
    return estado8(c)

def estado3():
    global lexema
    # print("edo 3")
    c = pila.pop()
    lexema = lexema + c

    if c == '.':
        return estado4()
    
    if c == 'E':
        return estado5()
    
    for i in numbres:
        if c == i:
            return estado3()
        
    return estado8(c)

def estado4():
    global lexema
    # print("edo 4")
    c = pila.pop()
    lexema = lexema + c
    
    for i in numbres:
        if c == i:
            return estado4()
        

    if c == 'E':
        return estado5()

    return estado8(c)

def estado5():
    global lexema
    # print("edo 5")
    c = pila.pop()
    lexema = lexema + c

    if c == '+' or c == '-':
        return estado6()
    
    return estado8(c)

def estado6():
    global lexema
    # print("edo 6")
    c = pila.pop()
    lexema = lexema + c

    for i in numbres:
        if c == i:
            return estado7()
        
    return estado8(c)

def estado7():
    global lexema
    # print("edo 7")
    c = pila.pop()
    
    for i in numbres:
        if c == i:
            lexema = lexema + c
            return estado7()
        
    return estado9(c)

def estado8(c):
    global lexema
    lexema = c
    return ERROR

def estado9(c):
    global retorno
    retorno = c
    return NOTACION

# Entry point
if __name__ == '__main__':
    run()