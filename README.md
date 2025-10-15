# Automata app

/mi_app/
│
├── 
├── main.py               
├── router.py             
├── utils/
│   ├──utilidades.py
├── views/
│   ├── __init__py
│   ├── home_view.py           
│   └── definir_afd_view.py    <-- (aqui quiero importar utilidades)


# View template:

```python
import flet as ft

# views/home_view.py
import flet as ft


#Template para una vista
class Some_view:
    def __init__(self, page: ft.Page):
        self.page = page
    
    def build(self) -> ft.View:
        return ft.View(
            route="/some_view",
            controls=[
                ft.Container(
                    content=ft.Column([
                        #Some controls    
                    ]),
                    width=700,  
                    padding=20,
                )
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER 
        )
```


                ft.TextButton(
                    text="Definir un Autómata",
                    on_click=lambda e: self.page.go("/definir_afd") 
                )