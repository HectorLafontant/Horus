import flet as ft
from DataBase import days_database

class RegisterDay(ft.UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page

    def build(self):

        menu_button = ft.ElevatedButton(text='Volver', height=50, width=400)
        menu_button.on_click = lambda _: self.page.go('/attendance_days')

        register_day_button = ft.ElevatedButton(text='Registrar dia', height=50, width=400)
        register_day_button.on_click = lambda _: register_day()

        def register_day():
            if day_field.value == '' or month_field.value == '':
                return
            days_database.add_day_record(day_field.value, month_field.value)
            day_field.value = ''
            month_field.value = ''
            fields.update()

        day_field = ft.TextField (expand=True, label='Dia')
        month_field = ft.TextField (expand=True, label='Mes')

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
                        register_day_button
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
                        ft.Text(
                            value='REGISTRAR DIA DE\nASISTENCIA',
                            weight=ft.FontWeight.BOLD, size=32,
                            text_align=ft.TextAlign.CENTER
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                fields,
                buttons
            ],
            spacing = 50,
            height=self.page.height,
            alignment=ft.MainAxisAlignment.CENTER
        )
        
        return view