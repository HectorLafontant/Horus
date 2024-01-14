import flet as ft

class RegisterStudent(ft.UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page

    def build(self):

        #funciones

        def regis_estudiante(e):

            text_est.controls.append(ft.Text(value=f'El estudiante es: {first_name_field.value}'))
            first_name_field.value = ''
            view.update()

        #########

        menu_button = ft.ElevatedButton(text='Volver al menu principal', height=50, width=400)
        menu_button.on_click = lambda _: self.page.go('/')


        first_name_field = ft.TextField(expand=True, label='Nombre')

        last_name_field = ft.TextField(expand=True, label='Apellido')

        id_field = ft.TextField(expand=True, label='Cedula')

        text_est = ft.Column()
                   
        fields = ft.Column(
            [
                ft.Row([
                    first_name_field
                ],
                alignment=ft.MainAxisAlignment.CENTER
                ),
                ft.Row([
                    last_name_field
                ],
                alignment=ft.MainAxisAlignment.CENTER
                ),
                ft.Row([
                    id_field
                ],
                alignment=ft.MainAxisAlignment.CENTER
                )
            ],
            spacing=25
        )

        buttons = ft.Column(
                [
                ft.Row(
                    [
                        ft.ElevatedButton(text='Registrar estudiante', height=50, width=400, on_click=regis_estudiante)
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                ft.Row(
                    [
                        menu_button
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                text_est
            ],
            spacing=20
        )

        view = ft.Column(
            [
                ft.Row(
                    [
                        ft.Text(value='REGISTRAR ESTUDIANTES', weight=ft.FontWeight.BOLD, size=32)
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                fields,
                buttons
            ],
            spacing= 50,
        )
        
        return view