import json
from tkinter import Tk, filedialog

def load_automaton():
    try:
        root = Tk()
        root.withdraw()
        root.wm_attributes('-topmost', 1)
        
        archivo = filedialog.askopenfilename(
            title="Seleccionar archivo JSON",
            filetypes=[("Archivos JSON", "*.json")]
        )
        
        root.destroy()
        
        if archivo:
            with open(archivo, "r", encoding='utf-8') as f:
                datos = json.load(f)
            
            alfabeto = datos.get("alfabeto", [])
            estados = datos.get("estados", [])
            estados_finales = datos.get("estados_finales", [])  
            transiciones = datos.get("transiciones", {})
            
            return alfabeto, estados, estados_finales, transiciones
        else:
            print("❌ Operación cancelada")
            return None, None, None, None  
            
    except Exception as ex:
        print(f"❌ Error al cargar: {ex}")
        return None, None, None, None 