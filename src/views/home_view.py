import flet as ft

class Home_view:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.title = "AFD Builder"
    
    def build(self) -> ft.View:
        return ft.View(
            route="/",
            controls=[
                ft.Container(
                    content=ft.Column(
                        [
                            ft.Text(
                                "AFD Builder",
                                size=32,
                                weight=ft.FontWeight.BOLD
                            ),
                            ft.Divider(height=40, color=ft.Colors.TRANSPARENT),

                            ft.ElevatedButton(
                                "Definir/Editar/Visualizar AFD",
                                icon=ft.Icons.BUILD_OUTLINED,
                                on_click=lambda _: self.page.go("/definir_afd"),
                                style=ft.ButtonStyle(
                                    padding=20,
                                )
                            ),

                            ft.ElevatedButton(
                                "Simular AFD",
                                icon=ft.Icons.PLAY_ARROW,
                                on_click=lambda _: self.page.go("/simulacion_afd"),
                                style=ft.ButtonStyle(
                                    padding=20,
                                ),
                            ),

                            ft.ElevatedButton(
                                "Calcular Subcadenas",
                                icon=ft.Icons.TEXT_FIELDS,
                                on_click=lambda _: self.page.go("/calcular_subcadenas"),
                                style=ft.ButtonStyle(
                                    padding=20,
                                ),
                            ),

                            ft.ElevatedButton(
                                "Calcular Cerraduras",
                                icon=ft.Icons.FUNCTIONS,
                                on_click=lambda _: self.page.go("/calcular_cerraduras"),
                                style=ft.ButtonStyle(
                                    padding=20,
                                ),
                            ),

                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    width=600,
                    padding=50,
                )
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )