import json
from tkinter import Tk, filedialog


def save_automaton(alfabeto: list, estados: list, estados_finales: list, transiciones: dict):

    datos = {
        "alfabeto": alfabeto,
        "estados": estados,
        "estados_finales": estados_finales,
        "transiciones": transiciones
    }

    try:
        root = Tk()
        root.withdraw()
        root.wm_attributes('-topmost',1)

        archivo = filedialog.asksaveasfilename(
            title="Guardar Automata",
            defaultextension=".json",
            filetypes=[
                ("Archivos JSON", "*.json")
            ],
            initialfile="mi_automata.json"
        )

        root.destroy()
        if archivo:
            with open(archivo, 'w', encoding='utf-8') as f:
                json.dump(datos, f, indent=4)
                print(f"✅ Guardado en: {archivo}")
        else:
            print("❌ Operación cancelada")
    except Exception as ex:
        print(f"❌ Error al guardar: {ex}")


