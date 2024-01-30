import flet as ft
import VoiceCommand as vc
from threading import Timer
class MainMenu(ft.UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page
    
    def build(self):

        img = ft.Image(
            src=f"images\HORUS_1.png",
            width=200,
            height=200,
            fit=ft.ImageFit.CONTAIN
        )

        list_students_button = ft.ElevatedButton(text='Lista de estudiantes', height=50, width=400)
        list_students_button.on_click = lambda _: self.page.go('/students_list')

        attendance_days_button = ft.ElevatedButton(text='Días de asistencia', height=50, width=400)
        attendance_days_button.on_click = lambda _: self.page.go('/attendance_days')

        student_attendance_button = ft.ElevatedButton(text='Lista de asistencia', height=50, width=400)
        student_attendance_button.on_click = lambda _: self.page.go('/student_attendance')

        def talk():
            command = vc.talk()
            if command == 'lista de estudiantes':
                self.page.go('/students_list')
            elif command == 'días de asistencia':
                self.page.go('/attendance_days')
            elif command == 'lista de asistencia':
                self.page.go('/student_attendance')
            else:
                t = Timer(1.0, talk)
                t.start()
        t = Timer(1.0, talk)
        t.start()

        view = ft.Column(
            [
                ft.Row(
                    [
                        ft.Text(value="\n\n¡BIENVENIDO!", weight=ft.FontWeight.BOLD)
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                ft.Row(
                    [
                        img
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                ft.Row(
                    [
                        list_students_button
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                ft.Row(
                    [
                        attendance_days_button
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                ft.Row(
                    [
                        student_attendance_button
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                )
            ],
            spacing= 20,
        )
        return view