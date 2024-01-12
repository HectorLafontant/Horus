import flet as ft

class RegisterStudent(ft.UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page

    def build(self):

        menu_button = ft.ElevatedButton(text='Volver al menu principal', height=50, width=400)
        menu_button.on_click = lambda _: self.page.go('/')

        firstname = ft.Ref[ft.TextField]
        lastname = ft.Ref[ft.TextField]
        id_stu = ft.Ref[ft.TextField]


        first_name_field = ft.Column(
            [
                ft.Row(
                    [
                        ft.Text(value='Nombre', weight=ft.FontWeight.BOLD, size=24)
                    ]
                ),
                ft.Row(
                    [
                        ft.TextField(ref=firstname, expand=True)
                    ]
                )
            ],
            spacing= 10
        )

        last_name_field = ft.Column(
            [
                ft.Row(
                    [
                        ft.Text(value='Apellido', weight=ft.FontWeight.BOLD, size=24)
                    ]
                ),
                ft.Row(
                    [
                        ft.TextField(ref=lastname, expand=True)
                    ]
                )
            ],
            spacing= 10
        )

        id_field = ft.Column(
            [
                ft.Row(
                    [
                        ft.Text(value='Cedula', weight=ft.FontWeight.BOLD, size=24)
                    ]
                ),
                ft.Row(
                    [
                        ft.TextField(ref=id_stu, expand=True)
                    ]
                )
            ],
            spacing= 10
        )

        fields = ft.Column(
            [
                first_name_field,
                last_name_field,
                id_field
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