import flet as ft
from DataBase import students_database
import VoiceCommand as vc
from threading import Timer
class StudentsList(ft.UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page

    def build(self):

        register_student_button = ft.ElevatedButton(text='Registrar estudiante', height=50, width=400)
        register_student_button.on_click = lambda _: self.page.go('/register_student')

        menu_button = ft.ElevatedButton(text='Volver', height=50, width=400)
        menu_button.on_click = lambda _: self.page.go('/')

        def talk():
            command = vc.talk()
            if command == 'registrar estudiante' or command == 'registrar estudiantes':
                self.page.go('/register_student')
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
                ft.DataColumn(ft.Text('Nombre')),
                ft.DataColumn(ft.Text('Apellido')),
                ft.DataColumn(ft.Text('Cedula'), numeric = True)
            ],
        )
        for records in students_database.query_students():
            table.rows.append(
                ft.DataRow (
                    cells = [
                        ft.DataCell(ft.Text(records[1])),
                        ft.DataCell(ft.Text(records[2])),
                        ft.DataCell(ft.Text(records[3]))
                    ]
                )
            )

        content = ft.Column(
            [
                ft.Row(
                    [
                        register_student_button
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
        )

        view = ft.Column(
            [
                ft.Row(
                    [
                        ft.Text(value='LISTA DE ESTUDIANTES', weight=ft.FontWeight.BOLD, size=32)
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                content
            ],
            spacing = 50,
            # height=self.page.height,
            # alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        )
        return view