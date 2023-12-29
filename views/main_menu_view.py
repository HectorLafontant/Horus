from typing import Union
import flet as ft
from views.Router import Router, DataStrategyEnum

def MainMenuView(router_data: Union[Router, str, None] = None):

    img = ft.Image(
        src=f"images\HORUS_1.png",
        
        width=200,
        height=200,
        fit=ft.ImageFit.CONTAIN
    )

    def register_student(event: ft.ControlEvent):
        event.page.go("/register")
    
    register_student_button = ft.ElevatedButton(text='Registrar estudiante', height=50, width=400)
    register_student_button.on_click = register_student


    view = ft.Column(
        [
            ft.Row(
                [
                    ft.Text(value="\n\n¡BIENVENIDO!", weight=ft.FontWeight.BOLD)
                ],
                alignment=ft.MainAxisAlignment.CENTER
            ),
            ft.Row(
                [
                    img
                ],
                alignment=ft.MainAxisAlignment.CENTER
            ),
            ft.Row(
                [
                    ft.ElevatedButton(text='Gestion de asistencia', height=50, width=400)
                ],
                alignment=ft.MainAxisAlignment.CENTER
            ),
            ft.Row(
                [
                    register_student_button
                ],
                alignment=ft.MainAxisAlignment.CENTER
            ),
            ft.Row(
                [
                    ft.ElevatedButton(text='Registrar asistencia', height=50, width=400)
                ],
                alignment=ft.MainAxisAlignment.CENTER
            )
        ],
        spacing= 20,
        # alignment=ft.MainAxisAlignment.CENTER,
        
        # horizontal_alignment= ft.CrossAxisAlignment.CENTER
    )
    return view