from tkinter import Tk, filedialog
import xml.etree.ElementTree as ET

def load_jff():
    try:
        root = Tk()
        root.withdraw()
        file = filedialog.askopenfilename(
            title="Seleccione un Archivo JFLAP",
            filetypes=[("Archivos JFLAP", "*.jff"),
                        ("Archivos AFD", "*.afd")
                    ]
        )
        root.destroy()

        if file:
            tree = ET.parse(file)
            root = tree.getroot()
            automaton = root.find('automaton')

            alfabeto = set()
            aux_estados = {}
            estados = []
            estados_finales = []
            transiciones = {}

            # Recorrer los estados y extraer la informacion
            for estado in automaton.findall('state'):
                id_state = estado.get('id')
                name_state = estado.get('name')
                aux_estados[id_state] = name_state            
                
                if estado.find('initial') is not None:
                    estados.insert(0, name_state)
                else: 
                    estados.append(name_state)
                
                if estado.find('final') is not None:
                    estados_finales.append(name_state)
            
            # Inicializar todos los estados en transiciones
            for estado in estados:
                transiciones[estado] = {}
                
            # Recorrer las transiciones y extraer la informacion
            for transicion in automaton.findall('transition'):
                desde_id = transicion.find('from').text
                hacia_id = transicion.find('to').text
                simbolo = transicion.find('read').text or ''
                
                desde = aux_estados[desde_id]
                hacia = aux_estados[hacia_id]

                if simbolo:
                    alfabeto.add(simbolo)
                
                transiciones[desde][simbolo] = hacia
            
            # Completar transiciones faltantes con ""
            for estado in transiciones:
                for simbolo in alfabeto:
                    if simbolo not in transiciones[estado]:
                        transiciones[estado][simbolo] = ""
            
            return list(alfabeto), estados, estados_finales, transiciones
        else:
            print("❌ Operación cancelada")
            return None, None, None, None 

    except Exception as ex:
        print(f"❌ Error al cargar: {ex}")
        return None, None, None, None
#alfabeto, estados, estados_finales, transiciones = load_jff()
#print(alfabeto)
#print(estados)
#print(estados_finales)
#print(transiciones)
