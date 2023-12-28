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
        width= 800,
        controls = [
            ft.Text(value="\n\n¡BIENVENIDO! ACCEDIENDO A", text_align=ft.TextAlign.CENTER),
            img,
            ft.ElevatedButton(text='Gestion de asistencia'),
            ft.ElevatedButton(text='Registrar estudiante'),
            ft.ElevatedButton(text='Registrar asistencia')
        ]
    )
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.add(view)

ft.app(target=main)