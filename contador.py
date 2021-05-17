

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
    

def iniciar():
    return


if __name__ == "__main__":
    # iniciar()
    print(contador_letras("Hay, hermanos, muchisimo que hacer."))
    
    # En consola: [('a', 3), ('c', 2), ('e', 3), ('h', 4), ('i', 2), ('m', 3), ('n', 1), ('o', 2), ('q', 1), ('r', 2),
    # ('s', 2), ('u', 2), ('y', 1)]
    
