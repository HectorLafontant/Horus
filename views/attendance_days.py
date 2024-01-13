import flet as ft

class AttendanceDays(ft.UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page

    def build(self):

        menu_button = ft.ElevatedButton(text='Volver al menu principal', height=50, width=400)
        menu_button.on_click = lambda _: self.page.go('/')

        day = ft.Ref[ft.TextField]
        month = ft.Ref[ft.TextField]


        day_field = ft.TextField(ref=day, expand=True, label='Dia')

        month_field = ft.TextField(ref=month, expand=True, label='Mes')
                   
        fields = ft.Column(
            [
                ft.Row([
                    day_field
                ],
                alignment=ft.MainAxisAlignment.CENTER
                ),
                ft.Row([
                    month_field
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
                        ft.ElevatedButton(text='Añadir dia', height=50, width=400)
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
                        ft.Text(value='DIAS DE ASISTENCIA', weight=ft.FontWeight.BOLD, size=32)
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                fields,
                buttons
            ],
            spacing= 50,
        )
        
        return view