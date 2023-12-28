import flet as ft

def main(page: ft.Page):
    page.title='HORUS'
    img = ft.Image(
        src=f"images\HORUS_1.png",
        
        width=200,
        height=200,
        fit=ft.ImageFit.CONTAIN
    )
    view = ft.Column(
        controls= [
        ft.Text(value="\n\n¡BIENVENIDO!", text_align=ft.TextAlign.CENTER, weight=ft.FontWeight.BOLD),
        img,
        ft.ElevatedButton(text='Gestion de asistencia', height=40),
        ft.ElevatedButton(text='Registrar estudiante', height=40),
        ft.ElevatedButton(text='Registrar asistencia', height=40)
        ],
        spacing= 20,
        alignment=ft.MainAxisAlignment.START,
        horizontal_alignment= ft.CrossAxisAlignment.CENTER
    )
    
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.add(view)

ft.app(target=main)