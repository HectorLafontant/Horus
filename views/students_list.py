import flet as ft

class StudentsList(ft.UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page

    def build(self):

        register_student_button = ft.ElevatedButton(text='Registrar estudiante', height=50, width=400)
        register_student_button.on_click = lambda _: self.page.go('/register')

        def cambio(e):
            pass
    
        def enter(e):
            pass

        def presionar(e):
            pass
        
        # filter_students = ft.SearchBar(
        #     view_elevation=4,
        #     divider_color=ft.colors.AMBER,
        #     bar_hint_text="Buscar Estudiante",
        #     view_hint_text="Coloque el nombre del estudiante",
        #     on_change=cambio,
        #     on_submit=enter,
        #     on_tap=presionar,
        #     icon=ft.icons.SEARCH
        #     )
        
        table = ft.DataTable(
            column_spacing=200,
            columns = [
                ft.DataColumn(ft.Text('Nombre')),
                ft.DataColumn(ft.Text('Apellido')),
                ft.DataColumn(ft.Text('Cedula'), numeric = True)
            ],
            rows = [
                 ft.DataRow(
                    cells = [
                        ft.DataCell(ft.Text('Yorgel')), #Variable para el nombre del estudiante
                        ft.DataCell(ft.Text('Páez')), #variable para el apellido de un estudiante
                        ft.DataCell(ft.Text(1000000)), #Variable para la cedula de un estudiante
                    ],
                ),
            ]
        )

        view = ft.Column([
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
                    ft.ElevatedButton(text='Volver al menu principal', height=50, width=400, on_click=lambda _: self.page.go('/'))
                ],
                alignment=ft.MainAxisAlignment.CENTER
            )
        ],
        spacing = 50,
        )
        return view