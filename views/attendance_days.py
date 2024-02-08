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
                ft.DataColumn(ft.Text('Mes')),
                ft.DataColumn(ft.Text('Borrar'))
            ],
        )

        def delete_record(e):
            days_database.delete_day_record_by_id(e.control.data)
            table.rows.clear()
            for records in days_database.query_days():
                button = ft.IconButton(icon=ft.icons.DELETE, on_click=delete_record, data=records[0])
                table.rows.append(
                    ft.DataRow (
                        cells = [
                            ft.DataCell(ft.Text(records[1])),
                            ft.DataCell(ft.Text(records[2])),
                            ft.DataCell(button)
                        ]
                    )
                )
            table.update()

        for records in days_database.query_days():
            button = ft.IconButton(icon=ft.icons.DELETE, on_click=delete_record, data=records[0])
            table.rows.append(
                ft.DataRow (
                    cells = [
                        ft.DataCell(ft.Text(records[1])),
                        ft.DataCell(ft.Text(records[2])),
                        ft.DataCell(button)
                    ]
                )
            )

        content = ft.Column(
            [
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
                )
            ],
            height=500,
            scroll="always",
            on_scroll_interval=0
        )

        view = ft.Column(
            [
                ft.Row(
                    [
                        ft.Text(value='DIAS DE ASISTENCIA', weight=ft.FontWeight.BOLD, size=32)
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                content
            ],
            spacing = 50,
        )
        
        return view