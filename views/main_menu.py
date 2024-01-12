import flet as ft

class MainMenu(ft.UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page
    
    def build(self):

        img = ft.Image(
            src=f"images\HORUS_1.png",
            width=200,
            height=200,
            fit=ft.ImageFit.CONTAIN
        )
        
        register_student_button = ft.ElevatedButton(text='Registrar estudiante', height=50, width=400)
        register_student_button.on_click = lambda _: self.page.go('/register')


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
                ),
                ft.Row([
                    ft.ElevatedButton(text='Lista de estudiantes registrados', height=50, width=400, on_click=lambda _: self.page.go('/student'))
                ],
                alignment=ft.MainAxisAlignment.CENTER
                )
            ],
            spacing= 20,
        )
        return view