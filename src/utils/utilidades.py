import flet as ft

class Indicador(ft.Container):
    def __init__(self):
        super().__init__(
            width=10,
            height=10,
            bgcolor=ft.Colors.RED,
            border_radius=10
        )
        self.status = False
    
    def change_color(self, valido: bool):
        self.status = valido
        if valido:
            self.bgcolor = ft.Colors.GREEN
        else:
            self.bgcolor = ft.Colors.RED
        self.update()