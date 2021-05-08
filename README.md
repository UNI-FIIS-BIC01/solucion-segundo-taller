# BIC01: Segundo Taller

En el archivo `contador.py` realice lo siguiente:

1. Cree una función llamada `contador_letras` que reciba como parámetro la cadena de caracteres
    `cadena_de_caracteres` y retorne una lista de tuplas. Esta lista contiene las letras de `cadena_de_caracteres`
   (primer elemento de cada tupla) y el número de veces que la letra aparece en `cadena_de_caracteres` 
   (segundo elemento de cada tupla). La lista debe estar ordenada alfabéticamente, respecto al primer elemento de 
   cada tupla. Considere que `cadena_de_caracteres` solo contiene letras del 
   alfabeto ingles (sin tildes ni eñe).
   
```python
    print(contador_letras("Hay, hermanos, muchisimo que hacer."))
    # En consola: [('a', 3), ('c', 2), ('e', 3), ('h', 4), ('i', 2), ('m', 3), ('n', 1), ('o', 2), ('q', 1), ('r', 2),
    # ('s', 2), ('u', 2), ('y', 1)]
```

2. Cree una función llamada `es_pangrama` que reciba como parámetro la cadena de caracteres
    `cadena_de_caracteres` y retorne un valor booleano. La función retorna `True` si `cadena_de_caracteres`
   contiene **todas** las letras del alfabeto ingles (sin tildes ni eñe) y `False` en caso contrario.
   
```python
    print(es_pangrama("Jovencillo emponzonado de whisky, que mala figurota exhibes."))
    # En consola: True
```

3. Complete la función `iniciar`, de modo que solicite al usuario el ingreso de texto. Para el texto ingresado, mostrar 
    la frecuencia de cada carácter utilizando `contador_letras` (implementada en el paso 1). En caso contenga todas
   las letras del alfabeto ingles de acuerdo a `es_pangrama` (implementada en el paso 2), mostrar un mensaje en consola.
   
```commandline
Ingrese texto:Jovencillo emponzonado de whisky, que mala figurota exhibes.
Letra: a frecuencia: 4
Letra: b frecuencia: 1
Letra: c frecuencia: 1
Letra: d frecuencia: 2
Letra: e frecuencia: 6
Letra: f frecuencia: 1
Letra: g frecuencia: 1
Letra: h frecuencia: 2
Letra: i frecuencia: 4
Letra: j frecuencia: 1
Letra: k frecuencia: 1
Letra: l frecuencia: 3
Letra: m frecuencia: 2
Letra: n frecuencia: 3
Letra: o frecuencia: 6
Letra: p frecuencia: 1
Letra: q frecuencia: 1
Letra: r frecuencia: 1
Letra: s frecuencia: 2
Letra: t frecuencia: 1
Letra: u frecuencia: 2
Letra: v frecuencia: 1
Letra: w frecuencia: 1
Letra: x frecuencia: 1
Letra: y frecuencia: 1
Letra: z frecuencia: 1
El texto contiene TODAS las letras del alfabeto
```