import flet as ft

class TablaTransiciones:
    def __init__(self, estados: list, alfabeto: list, transiciones: dict):
        self.estados = estados
        self.alfabeto = alfabeto
        self.transiciones = transiciones
    
    def create_dicc_trans(self):
        self.transiciones.clear()
        self.transiciones.update({estado: {simbolo: "" for simbolo in self.alfabeto} for estado in self.estados})
    
    def actualizar_transicion(self, estado, simbolo, e):
        self.transiciones[estado][simbolo] = e.control.value
        print(f"δ({estado}, {simbolo}) = {e.control.value}")
    
    def build(self) -> ft.DataTable:
        columnas = [ft.DataColumn(ft.Text("Estado", weight="bold"))]
        columnas += [ft.DataColumn(ft.Text(str(simbolo), weight="bold")) for simbolo in self.alfabeto]
        
        filas = []
        for estado in self.estados:
            celdas = [ft.DataCell(ft.Text(estado))]
            for simbolo in self.alfabeto:
                dropdown = ft.Dropdown(
                    options=[ft.dropdown.Option("Ø")] + [ft.dropdown.Option(e) for e in self.estados],
                    width=200,
                    text_size=12,
                    on_change=lambda e, est=estado, sim=simbolo: self.actualizar_transicion(est, sim, e)
                )
                celdas.append(ft.DataCell(dropdown))
            filas.append(ft.DataRow(cells=celdas))
        
        return ft.DataTable(columns=columnas, rows=filas)
    
    def obtener_transiciones(self) -> dict:
        """Retorna el diccionario de transiciones"""
        return self.transiciones