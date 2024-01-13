import flet as ft

from views.main_menu import MainMenu
from views.register_student import RegisterStudent
from views.students_list import StudentsList
from views.attendance_days import AttendanceDays

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
        '/students_list': ft.View(
            route='/students_list',
            controls=[
                StudentsList(page)
            ]
        ),
        '/attendance_days': ft.View(
            route='/attendance_days',
            controls=[
                AttendanceDays(page)
            ]
        )
    }