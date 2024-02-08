import flet as ft
from DataBase import students_database
from DataBase import days_database
from DataBase import attendance_database
import VoiceCommand as vc
from threading import Timer
class RegisterStudentAttendance(ft.UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page

    def build(self):

        register_student_attendance_button = ft.ElevatedButton(text='Registrar asistencia', height=50, width=400)
        register_student_attendance_button.on_click = lambda _: register_student_attendance()

        menu_button = ft.ElevatedButton(text='Volver', height=50, width=400)
        menu_button.on_click = lambda _: self.page.go('/student_attendance')

        def talk():
            command = vc.talk()
            if command == 'registrar asistencia':
                register_student_attendance()
            elif command == 'volver':
                self.page.go('/student_attendance')
            else:
                t = Timer(1.0, talk)
                t.start()
        t = Timer(1.0, talk)
        t.start()

        def register_student_attendance():
            if students_drop_down.value == None or days_drop_down.value == None:
                return
            for records in attendance_database.query_attendances():
                if int(records[0]) == int(students_drop_down.value) and int(records[4]) == int(days_drop_down.value):
                    return
            attendance_database.add_attendance_record(days_drop_down.value, students_drop_down.value)

        students_drop_down = ft.Dropdown(width=200)
        days_drop_down = ft.Dropdown(width=200)

        for records in students_database.query_students():
            students_drop_down.options.append(ft.dropdown.Option(key=records[0], text=records[2]))

        for records in days_database.query_days():
            days_drop_down.options.append(ft.dropdown.Option(key=records[0], text=records[1] + '/' + records[2]))

        fields = ft.Column(
            [
                ft.Row([
                    students_drop_down,
                    days_drop_down
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
                        register_student_attendance_button
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
                        ft.Text(value='REGISTRAR ASISTENCIA', weight=ft.FontWeight.BOLD, size=32)
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