def generar_cerraduras(alfabeto:list, longitud:int):
        def backtrack(actual):
            if 0 < len(actual) <= longitud:
                resultado.append(actual)
            if len(actual) == longitud:
                return
            for letra in alfabeto:
                backtrack(actual + letra)
        resultado = []
        backtrack('')
        return sorted(resultado, key=lambda x: (len(x), x))

#Ejemplo
a = ("a", "b", "c")
print(generar_cerraduras(alfabeto=a, longitud=2))


#palabras = ['ab', 'aa', 'b', 'a', 'ba', 'bb']
#ordenadas = sorted(palabras, key=lambda x: (len(x), x))
#print(ordenadas)
