import flet as ft

from views.main_menu import MainMenu
from views.register_student import RegisterStudent
from views.list_students import ListStudents

def router_handler(page):
    return {
        '/': ft.View(
            route='/',
            controls=[
                MainMenu(page)
            ]
        ),
        '/register': ft.View(
            route='/register',
            controls=[
                RegisterStudent(page)
            ]
        ),
        '/student': ft.View(
            route='/student',
            controls=[
                ListStudents(page)
            ]
        )
    }