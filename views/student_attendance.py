import flet as ft
from DataBase import days_database
from DataBase import attendance_database
from DataBase import students_database
import VoiceCommand as vc
from threading import Timer
class StudentAttendance(ft.UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page

    def build(self):

        register_student_attendance_button = ft.ElevatedButton(text='Registrar asistencia', height=50, width=400)
        register_student_attendance_button.on_click = lambda _: self.page.go('/register_student_attendance')

        menu_button = ft.ElevatedButton(text='Volver', height=50, width=400)
        menu_button.on_click = lambda _: self.page.go('/')

        def talk():
            command = vc.talk()
            if command == 'registrar asistencia':
                self.page.go('/register_student_attendance')
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
                ft.DataColumn(ft.Text('Estudiantes')),
            ],
        )

        higher_day_id = 0
        for days in days_database.query_days():
            if days[0] > higher_day_id:
                higher_day_id = days[0]

        data_columns = []
        for day_id in range(1, higher_day_id + 1):
            
            id_has_day = False
            for day_record in days_database.query_days():
                if day_id == day_record[0]:
                    id_has_day = True
                    data_columns.append(
                        ft.DataColumn(
                            ft.Text(day_record[1] + '/' + day_record[2])
                        )
                    )
                    break
            if id_has_day == False:
                data_columns.append(ft.DataColumn(ft.Text('erased'), visible=False))
        table.columns.extend(data_columns)
                    
        
        higher_student_id = 0
        for students in students_database.query_students():
            if students[0] > higher_student_id:
                higher_student_id = students[0]

        for ids in range(1, higher_student_id + 1):
            data_cells = []

            id_has_student = False
            for student_record in students_database.query_students():
                if ids == student_record[0]:
                    id_has_student = True
                    data_cells.append(
                        ft.DataCell(ft.Text(student_record[2]))
                    )
                    break
            if id_has_student == False:
                data_cells.append(ft.DataCell(ft.Text('erased')))

            for days in range(1, higher_day_id + 1):

                data_cells.append(
                    ft.DataCell(ft.Icon(name=ft.icons.CLOSE))
                )
            table.rows.append(
                ft.DataRow (
                    cells=data_cells,
                    visible=id_has_student
                )
            )
        
        check = ft.DataCell(ft.Icon(name=ft.icons.CHECK))

        for records in attendance_database.query_attendances():
            print(records)
            row = table.rows[int(records[0]) - 1]
            row.cells[records[4]] = check
            table.rows[int(records[0] - 1)] = row
        
        for idx, rows in enumerate(table.rows):
            pops = 0
            for idy, columns in enumerate(table.columns):
                if not columns.visible:
                    table.rows[idx].cells.pop(idy - pops)
                    pops += 1

        content = ft.Column(
            [
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
                        ft.Text(
                            value='LISTA DE\nASISTENCIA',
                            weight=ft.FontWeight.BOLD,
                            size=32,
                            text_align=ft.TextAlign.CENTER
                            )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                content
            ],
            spacing = 50
        )
        
        return view