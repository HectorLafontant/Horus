import flet as ft
from DataBase import days_database
import VoiceCommand as vc
from threading import Timer
class AttendanceDays(ft.UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page

    def build(self):

        register_day_button = ft.ElevatedButton(text='Registrar día', height=50, width=400)
        register_day_button.on_click = lambda _: self.page.go('/register_day')

        menu_button = ft.ElevatedButton(text='Volver', height=50, width=400)
        menu_button.on_click = lambda _: self.page.go('/')

        def talk():
            command = vc.talk()
            if command == 'registrar día':
                self.page.go('/register_day')
            elif command == 'volver':
                self.page.go('/')
            else:
                t = Timer(1.0, talk)
                t.start()
        t = Timer(1.0, talk)
        t.start()

        table = ft.DataTable(
            expand=True,
            columns = [
                ft.DataColumn(ft.Text('Dia')),
                ft.DataColumn(ft.Text('Mes'))
            ],
        )
        for records in days_database.query_days():
            table.rows.append(
                ft.DataRow (
                    cells = [
                        ft.DataCell(ft.Text(records[1])),
                        ft.DataCell(ft.Text(records[2]))
                    ]
                )
            )

        view = ft.Column(
            [
                ft.Row(
                    [
                        ft.Text(value='DIAS DE ASISTENCIA', weight=ft.FontWeight.BOLD, size=32)
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                ft.Row(
                    [
                        register_day_button
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                ft.Row(
                    [
                        table
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                ft.Row(
                    [
                        menu_button
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
            ],
            spacing = 50,
            height=self.page.height,
            alignment=ft.MainAxisAlignment.CENTER
        )
        
        return view