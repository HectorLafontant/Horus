import flet as ft

class RegisterStudent(ft.UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page

    def build(self):

        menu_button = ft.ElevatedButton(text='Volver', height=50, width=400)
        menu_button.on_click = lambda _: self.page.go('/students_list')

        firstname = ft.Ref[ft.TextField]
        lastname = ft.Ref[ft.TextField]
        id_stu = ft.Ref[ft.TextField]


        first_name_field = ft.TextField(ref=firstname, expand=True, label='Nombre')

        last_name_field = ft.TextField(ref=lastname, expand=True, label='Apellido')

        id_field = ft.TextField(ref=id_stu, expand=True, label='Cedula')
                   
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
                        ft.ElevatedButton(text='Registrar estudiante', height=50, width=400)
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                ft.Row(
                    [
                        menu_button
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                )
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