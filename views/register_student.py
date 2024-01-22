import flet as ft
from DataBase import students_database

class RegisterStudent(ft.UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page

    def build(self):

        menu_button = ft.ElevatedButton(text='Volver', height=50, width=400)
        menu_button.on_click = lambda _: self.page.go('/students_list')

        register_student_button = ft.ElevatedButton(text='Registrar estudiante', height=50, width=400)
        register_student_button.on_click = lambda _: register_student()

        def register_student():
            students_database.add_student_record(first_name_field.value, last_name_field.value, id_field.value)
            first_name_field.value = ''
            last_name_field.value = ''
            id_field.value = ''

        first_name_field = ft.TextField (expand=True, label='Nombre')
        last_name_field = ft.TextField (expand=True, label='Apellido')
        id_field = ft.TextField (expand=True, label='Cedula')

        fields = ft.Column(
            [
                ft.Row([
                    first_name_field
                ],
                alignment=ft.MainAxisAlignment.CENTER
                ),
                ft.Row([
                    last_name_field
                ],
                alignment=ft.MainAxisAlignment.CENTER
                ),
                ft.Row([
                    id_field
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
                        register_student_button
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