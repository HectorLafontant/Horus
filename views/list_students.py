import flet as ft

class ListStudents(ft.UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page

    def build(self):
        
        filter_students = ft.TextField(
            label='Buscar Estudiante',
            text_align='justify',
            border_radius=10,
            content_padding=10,
            focused_border_color='#6DB9EF',
            cursor_radius=40,
            icon=ft.icons.SEARCH
            )
        
        view = ft.DataTable(
            columns = [
                ft.DataColumn(ft.Text('Nombre')),
                ft.DataColumn(ft.Text('Apellido')),
                ft.DataColumn(ft.Text('Cedula'), numeric = True)
            ],
            rows = [
                 ft.DataRow(
                    cells = [
                        ft.DataCell(), #Variable para el nombre del estudiante
                        ft.DataCell(), #variable para el apellido de un estudiante
                        ft.DataCell(), #Variable para la cedula de un estudiante
                    ],
                ),
            ]
        )
        self.page.scroll = 'always'

        return view