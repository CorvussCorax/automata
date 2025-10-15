#Retorna Verdadero o Falso segun la aceptacion

def traza_simulacion(cadena:str, transiciones:dict, estado_inicial:str ,estados_finales:list):
        estado_actual = estado_inicial
        print(" ↓")
        for i,letra in enumerate(cadena):
                if i == 0: print(f"({estado_actual}, {cadena[i:]})")
                else: print(f" ⊢({estado_actual}, {cadena[i:]})")
                
                if not transiciones[estado_actual][letra]:
                        return False
                estado_actual = transiciones[estado_actual][letra]
                
        return estado_actual in estados_finales

cadena = "11111111111111111"
estados = ["q0","q1","q2"]
transiciones = {"q0":{"0":"", "1":"q1"},"q1":{"0":"", "1":"q2"},"q2":{"0":"", "1":"q2"}}
estados_finales = ["q2"]

aceptacion = traza_simulacion(cadena=cadena, transiciones=transiciones, estado_inicial=estados[0], estados_finales=estados_finales)
print(aceptacion)
