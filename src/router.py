import flet as ft
from views.home_view import Home_view
from views.definir_afd_view import Definir_afd_view
from views.simulacion_afd_view import Simulacion_afd_view
from views.calcular_subcadenas_view import Calcular_subcadenas_view

def handle_route_change(e: ft.RouteChangeEvent):
    page = e.page
    page.views.clear()
    
    # Diccionario de rutas
    routes = {
        "/": Home_view,
        "/definir_afd": Definir_afd_view,
        "/simulacion_afd":Simulacion_afd_view,
        "/calcular_subcadenas":Calcular_subcadenas_view, 
    }
    
    # Obtener la vista correspondiente
    view_class = routes.get(page.route)
    
    if view_class:
        view = view_class(page)
        page.views.append(view.build())
    else:
        # Ruta no encontrada - redirigir al home
        page.go("/")
        return
    
    page.update()