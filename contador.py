import string


def contador_letras(cadena_de_caracteres):
    """
    :param cadena_de_caracteres: Un texto.
    :return: Una lista de tuplas, donde cada tupla esta compuesta por una letra del alfabeto y el numero de veces que
    aparece en cadena_de_caracteres
    """
    todas_las_letras = string.ascii_lowercase

    frecuencias = []
    for letra_a_contar in todas_las_letras:
        frecuencia = 0

        for letra_en_texto in cadena_de_caracteres.lower():
            if letra_en_texto == letra_a_contar:
                frecuencia += 1

        if frecuencia > 0:
            frecuencias.append((letra_a_contar, frecuencia))

    return frecuencias


def es_pangrama(cadena_de_caracteres):
    """
    :param cadena_de_caracteres: Un texto.
    :return: True, si cadena_de_caracteres contiene TODAS las letras del alfabeto. False, caso contrario.
    """

    cadena_de_caracteres = cadena_de_caracteres.lower()

    for letra_alfabeto in string.ascii_lowercase:
        if letra_alfabeto not in cadena_de_caracteres:
            return False

    return True


def iniciar():
    una_cadena = input("Ingrese texto:")
    resultado_funcion = contador_letras(una_cadena)

    for tupla in resultado_funcion:
        letra = tupla[0]
        frecuencia = tupla[1]
        print(f"Letra: {letra} frecuencia: {frecuencia}")

    if es_pangrama(una_cadena):
        print("El texto contiene TODAS las letras del alfabeto")


if __name__ == "__main__":
    iniciar()
