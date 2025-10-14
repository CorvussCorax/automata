import flet as ft
import json
from tkinter import Tk, filedialog


def save_automaton(alfabeto: list, estados: list, transiciones: dict):

    datos = {
        "alfabeto": alfabeto,
        "estados": estados,
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
                ("Archivos JSON", "*.jsonn")
            ],
            initialfile="mi_automata.json"
        )

        root.destroy()
        if archivo:
            with open(archivo, 'w', encoding='utf-8') as f:
                json.dump(datos, f, indent=4)
        else:
            pass
    except:
        pass


alfabeto = [0,1]
estados = ["q0","q1","q2"]
transiciones = {"q0":1, "q1":2}

save_automaton(alfabeto= alfabeto, estados= estados, transiciones=transiciones)

