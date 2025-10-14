import flet as ft

class Home_view:
    def __init__(self, page: ft.Page):
        self.page = page
    
    def build(self) -> ft.View:
        return ft.View(
            route="/",
            controls=[
                ft.Container(
                    content=ft.Column(
                        [
                            ft.Text(
                                "Simulador de Autómatas",
                                size=32,
                                weight=ft.FontWeight.BOLD
                            ),
                            ft.Divider(height=40, color=ft.Colors.TRANSPARENT),
                            ft.ElevatedButton(
                                "Definir AFD",
                                icon=ft.Icons.BUILD_OUTLINED,
                                on_click=lambda _: self.page.go("/definir_afd"),
                                style=ft.ButtonStyle(
                                    padding=20,
                                )
                            ),
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    width=600,
                    padding=50,
                )
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            vertical_alignment=ft.MainAxisAlignment.CENTER,
        )