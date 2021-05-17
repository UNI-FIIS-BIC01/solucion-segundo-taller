import string

def contador_letras(cadena_de_caracteres):
    """
    cadena_de_caracteres: string
    resultado: Lista de tuplas
    """
    
    cadena_de_caracteres = cadena_de_caracteres.lower()
    
    resultado = []
    todas_las_letras = string.ascii_lowercase
    
    for letra in todas_las_letras:
        frecuencia = 0
        # "habas"
        for letra_cadena in cadena_de_caracteres:
            if letra_cadena == letra:
                frecuencia += 1
        
        if frecuencia > 0:
            tupla_frecuencias = (letra, frecuencia)
            resultado.append(tupla_frecuencias)
    
    return resultado 

def es_pangrama(cadena_de_caracteres):
    """
    cadena_de_caracteres: string.
    resultado: Booleano
    """
    
    cadena_de_caracteres = cadena_de_caracteres.lower()
    todas_las_letras = string.ascii_lowercase
    
    for letra in todas_las_letras:
        if letra not in cadena_de_caracteres:
            return False
    
    return True
    

def iniciar():
    
    texto_del_usuario = input("Ingrese texto:")
    lista_de_tuplas = contador_letras(texto_del_usuario)
    print(lista_de_tuplas)
    
    for tupla in lista_de_tuplas:
        letra = tupla[0]
        frecuencia = tupla[1]
        print(f"Letra: {letra} frecuencia: {frecuencia}")
        
    if es_pangrama(texto_del_usuario):
        print("El texto contiene TODAS las letras del alfabeto")
    
    return


if __name__ == "__main__":
    iniciar()
    # print(es_pangrama("Hay, hermanos, muchisimo que hacer."))
    # En consola: True
    
