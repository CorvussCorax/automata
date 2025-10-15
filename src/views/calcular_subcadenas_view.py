import flet as ft

class Calcular_subcadenas_view:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.title = "Calculo de Subcadenas"
    
    def build(self) -> ft.View:
        return ft.View(
            route="/calcular_subcadenas",
            controls=[
                ft.Text("holacalcular")
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )