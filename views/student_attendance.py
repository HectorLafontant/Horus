import flet as ft
from DataBase import days_database
from DataBase import attendance_database
from DataBase import students_database

class StudentAttendance(ft.UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page

    def build(self):
        print(attendance_database.query_attendances())
        register_student_attendance_button = ft.ElevatedButton(text='Registrar Asistencia', height=50, width=400)
        register_student_attendance_button.on_click = lambda _: self.page.go('/register_student_attendance')

        menu_button = ft.ElevatedButton(text='Volver al menu principal', height=50, width=400)
        menu_button.on_click = lambda _: self.page.go('/')

        table = ft.DataTable(
            expand=True,
            columns = [
                ft.DataColumn(ft.Text('Estudiantes')),
            ],
        )

        for records in days_database.query_days():
            table.columns.append(
                ft.DataColumn(
                    ft.Text(records[1] + '/' + records[2])
                )
            )
        for student_record in students_database.query_students():
            data_cells = []
            data_cells.append(
                ft.DataCell(ft.Text(student_record[2]))
            )
            for day_record in days_database.query_days():

                data_cells.append(
                    ft.DataCell(ft.Icon(name=ft.icons.CLOSE))
                )
            table.rows.append(
                ft.DataRow (
                    cells=data_cells
                )
            )
        
        check = ft.DataCell(ft.Icon(name=ft.icons.CHECK))

        for records in attendance_database.query_attendances():
            row = table.rows[records[0] - 1]
            row.cells[records[4]] = check
            table.rows[int(records[0])-1] = row
        view = ft.Column(
            [
                ft.Row(
                    [
                        ft.Text(
                            value='LISTA DE\nASISTENCIA',
                            weight=ft.FontWeight.BOLD,
                            size=32,
                            text_align=ft.TextAlign.CENTER
                            )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                ft.Row(
                    [
                        register_student_attendance_button
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