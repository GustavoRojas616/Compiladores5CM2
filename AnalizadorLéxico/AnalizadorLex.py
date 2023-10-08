#Practica1 COMPILADORES 5CM2; Arreola Rojas Gustavo Adolfo; Ramirez Ayala Erandi
import os
import sys

lista_tokens=[]
def main():
    if len(sys.argv) > 2:
        print("Uso correcto: python Practica1.py nombre_archivo.txt")
        sys.exit(64)
    elif len(sys.argv) == 2:
        ejecutar_archivo(sys.argv[1])
    else:
        ejecutar_prompt()

def ejecutar_archivo(nombre_archivo):
    global lista_tokens
    if os.path.isfile(nombre_archivo):
        entrada = open(nombre_archivo)
        entrada = ''.join(entrada)
        tokens = list(entrada)
        b = tokens
        while len(b) > 0:
            # print(len(b))
            if str(b[0]) in simbolos_key or str(b[0]).isdigit() == True or str(b[0]).isalpha() == True or str(b[0]) == '\n' or str(b[0]) == ' ' or str(b[0]) == '"':
                aux = 0
                pass
            else:
                aux = 1
                print("Error léxico.")
                lista_tokens = []
                break
                if len(b) == 1:
                    # print("Hola")
                    break
                elif len(b) > 1:
                    # print(len(b))
                    b.pop(0)
                    # print(len(b))
                    # print(len(b))
                    pass
            if str(b[0]).isalpha() == True:
                b = automataRESIDEN(tokens)
            elif str(b[0]).isspace() == True:
                if len(b) == 1:
                    break
                else:
                    b.pop(0)
                    if str(b[0]).isalpha() == True:
                        b = automataRESIDEN(tokens)
            elif str(b[0]) == '"':
                b = automataCAD(tokens)
                # print(b)
                # elif str(b[0]).isspace()==False and str(b[0])
            elif str(b[0]).isdigit() == False and str(b[0]).isalpha() == False and aux == 0:
                if len(b) == 1:
                    b = automata1CARAC(tokens)
                else:
                    if (str(b[0]) == '/' and str(b[1]) == '/') or (str(b[0]) == '/' and str(b[1]) == '*'):
                        a, b = automataCOMEN(tokens)
                        if a == 0:
                            b = automata1CARAC(tokens)
                    else:
                        b = automata1CARAC(tokens)
            elif str(b[0]).isdigit() == True:
                b = automataNUM(tokens)
        print("Tokens registrados:", lista_tokens)


    else:
        print("El archivo no existe.")

def ejecutar_prompt():
    global lista_tokens
    while True:
        a = 1
        lista_tokens = []
        entrada = input(">>> ")
        tokens = list(entrada)
        b = tokens
        while len(b) > 0:
            # print(len(b))
            if str(b[0]) in simbolos_key or str(b[0]).isdigit() == True or str(b[0]).isalpha() == True or str(b[0]) == '\n' or str(b[0]) == ' ' or str(b[0]) == '"':
                aux = 0
                pass
            else:
                aux = 1
                print("Error léxico.")
                lista_tokens = []
                break
                if len(b) == 1:
                    # print("Hola")
                    break
                elif len(b) > 1:
                    # print(len(b))
                    b.pop(0)
                    # print(len(b))
                    # print(len(b))
                    pass
            if str(b[0]).isalpha() == True:
                b = automataRESIDEN(tokens)
            elif str(b[0]).isspace() == True:
                if len(b) == 1:
                    break
                else:
                    b.pop(0)
                    if str(b[0]).isalpha() == True:
                        b = automataRESIDEN(tokens)
            elif str(b[0]) == '"':
                b = automataCAD(tokens)
                # print(b)
                # elif str(b[0]).isspace()==False and str(b[0])
            elif str(b[0]).isdigit() == False and str(b[0]).isalpha() == False and aux == 0:
                if len(b) == 1:
                    b = automata1CARAC(tokens)
                else:
                    if (str(b[0]) == '/' and str(b[1]) == '/') or (str(b[0]) == '/' and str(b[1]) == '*'):
                        a, b = automataCOMEN(tokens)
                        if a == 0:
                            b = automata1CARAC(tokens)
                    else:
                        b = automata1CARAC(tokens)
            elif str(b[0]).isdigit() == True:
                b = automataNUM(tokens)


        print("Tokens registrados:", lista_tokens)


