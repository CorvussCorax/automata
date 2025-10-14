import flet as ft
import os
from utils.utilidades import Indicador
from utils.tabla_transiciones import TablaTransiciones
from utils.mk_img_automaton import mk_img_automaton


class Definir_afd_view:
    def __init__(self, page: ft.Page):

    
        self.page = page
        self.page.title = "Definir AFD"
        
        self.transiciones = {}
        self.transiciones_text = ft.Text(value = "")

        self.alfabeto = []
        self.ind_alfabeto = Indicador()
        self.alfabeto_tf = ft.TextField(
            hint_text = "0,1", 
            on_submit=self.mk_alfabeto,
            expand=True
        )
        

        self.estados = []
        self.ind_estados = Indicador()
        self.estados_tf  = ft.TextField(
            hint_text = "q0, q1, q2", 
            on_submit=self.mk_estados,
            expand=True
        )
        
        self.estados_fin = []
        self.ind_estados_fin = Indicador()
        self.estados_fin_tf = ft.TextField(
            hint_text = "q0, q1",
            on_submit=self.mk_estados_fin,
            expand=True     
        )

        self.table_container = ft.Column()
        self.tabla_transiciones = None
        self.dicc_transiciones = {}
        self.table_buttons = ft.Row()

        self.img_automaton_container = ft.Column(height=200)
        self.img_automaton = None
        self.img_generar_boton = ft.TextButton(
                text= "Generar Imagen del Automata",
                on_click= self.generar_imagen,
                visible= False
            )



    def build(self) -> ft.View:
        return ft.View(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            scroll= "Auto",
            route="/definir_afd",
            controls=[    
                ft.Column(
                    width = 700,
                    controls= [

                        #Definicion del Afabeto
                        ft.Row(
                            controls = [
                                self.ind_alfabeto, 
                                ft.Text(" Alfabeto (Σ)")
                            ]
                        ),
                        ft.Row(
                            controls = [
                                self.alfabeto_tf,
                                ft.IconButton(
                                    icon=ft.Icons.SAVE,
                                    on_click= self.mk_alfabeto
                                )
                            ]
                        ),
                        
                        #Definicion del conjunto de estados
                        #El primer elemento sera nuestro estado incial
                        ft.Row(
                            controls = [
                                self.ind_estados,
                                ft.Text(" Conjunto de estados (Q) -> (El primer estado sera el inicial)")
                            ]
                        ),
                        ft.Row(
                            controls=[
                                self.estados_tf,
                                ft.IconButton(
                                    icon=ft.Icons.SAVE,
                                    on_click=self.mk_estados
                                )
                            ]
                        ), 

                        #Definicion del conjunto de estados finales
                        ft.Row(
                            controls = [
                                self.ind_estados_fin,
                                ft.Text(" Conjunto de estados Finales (F)"),
                            ]
                        ),
                        
                        ft.Row(
                            controls=[
                                self.estados_fin_tf,
                                ft.IconButton(
                                    icon=ft.Icons.SAVE,
                                    on_click=self.mk_estados_fin
                                )
                            ]
                        ), 

                        ft.Row(
                            controls = [
                                ft.Text(" Tabla de transiciones (δ):"),
                                ft.TextButton(
                                text="Crear Tabla de Transiciones",
                                on_click= self.mkTabla
                                ),
                                self.transiciones_text,
                            ]
                        ),

                        self.table_container,
                        self.img_generar_boton,
                        self.img_automaton_container,  
                        
                    ]
                )
            ]
            
        )

    #Convierte un string a lista, limpia el string
    def parse_symbol_groups(self, cadena):
        elementos = cadena.split(',')
        return list(dict.fromkeys([x.replace(' ', '') for x in elementos]))
    
    #ALFABETO
    def mk_alfabeto(self, e):
        self.alfabeto = []
        #Si no hay ningun elemento en el alfabeto
        if not self.alfabeto_tf.value.strip():
            self.alfabeto_tf.error_text = "No puede estar vacio"
            self.ind_alfabeto.change_color(False)
        #Creamos el alfabeto
        else:
            self.alfabeto_tf.error_text = None
            self.alfabeto = self.parse_symbol_groups(self.alfabeto_tf.value)
            self.ind_alfabeto.change_color(True)
            
        print(self.alfabeto)
        
        self.page.update()

    #ESTADOS
    def mk_estados(self, e):
        self.estados = []
        #El conjunto de estados no puede estar vacio      
        if not self.estados_tf.value.strip():
            self.estados_tf.error_text = "No puede estar vacio"
            self.ind_estados.change_color(False)
        #Creamos el conjunto de estados, EL ESTADO INICIAL SERA EL PRIMER ESTADO EN LA LISTA
        else:
            self.estados_tf.error_text = None
            self.estados = self.parse_symbol_groups(self.estados_tf.value)
            self.ind_estados.change_color(True)
            
        print(self.estados)
        
        self.page.update()

    #ESTADOS FINALES
    def mk_estados_fin(self, e): 
        self.estados_fin = []
        #Checamos si los estados base han sido definidos y que el conjunto de estados finales no se nulo
        self.ind_estados_fin.change_color(False)
        if not self.estados_fin_tf.value.strip():
            self.estados_fin_tf.error_text = "No puede estar vacio"  
        if not self.estados:
            self.estados_fin_tf.error_text = "Primero define los estados"
        
        else:
            self.estados_fin_tf.error_text = None
            aux = self.parse_symbol_groups(self.estados_fin_tf.value)
            remove_estados = aux.copy()
            #Checamos que los estados finales esten definidos en los estados base
            for estado in aux:
                if estado not in self.estados:
                    self.estados_fin_tf.error_text = f"Advertencia: {estado} ∉Q, {estado} no se incluyo en la lista de estados finales"
                    remove_estados.remove(estado)
            aux = remove_estados.copy()
            if aux:
                self.ind_estados_fin.change_color(True)
                self.estados_fin = aux.copy()
            

        print(self.estados_fin)
        self.page.update()

    def generar_imagen(self, e):
        # Limpiar archivos antiguos (solo si usas Opción 2)
        for archivo in os.listdir('.'):
            if archivo.startswith('automata_') and archivo.endswith('.png'):
                try:
                    os.remove(archivo)
                except:
                    pass
        
        # Limpiar contenedor
        self.img_automaton_container.controls.clear()
        
        # Generar nueva imagen
        self.img_automaton = mk_img_automaton(
            transiciones=self.transiciones, 
            estados_finales=self.estados_fin
        )
        
        self.img_automaton_container.controls.append(self.img_automaton)
        self.page.update()  # ← Importante: actualizar toda la página

    def mkTabla(self, e):          
        if(self.ind_alfabeto.status and self.ind_estados.status and self.ind_estados_fin.status):
            
            self.transiciones_text.value = "¡Tabla creada!"
            self.table_container.controls.clear()
            
            # Crear la tabla
            self.tabla_transiciones = TablaTransiciones(estados=self.estados, alfabeto=self.alfabeto, transiciones= self.transiciones)
            self.tabla_transiciones.create_dicc_trans()
            # Agregar directamente el DataTable
            self.table_container.controls.append(self.tabla_transiciones.build())

            self.img_generar_boton.visible = True
            
            self.page.update()
        else: 
            self.transiciones_text.value = "¡Antes llene los campos correctamente!"
            self.page.update()
