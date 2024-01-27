import flet as ft

from views.main_menu import MainMenu
from views.register_student import RegisterStudent
from views.students_list import StudentsList
from views.register_day import RegisterDay
from views.attendance_days import AttendanceDays
from views.student_attendance import StudentAttendance
from views.register_student_attendance import RegisterStudentAttendance

def router_handler(page):
    return {
        '/': ft.View(
            route='/',
            controls=[
                MainMenu(page)
            ]
        ),
        '/register_student': ft.View(
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
        '/register_day': ft.View(
            route='/register_day',
            controls=[
                RegisterDay(page)
            ]
        ),
        '/attendance_days': ft.View(
            route='/attendance_days',
            controls=[
                AttendanceDays(page)
            ]
        ),
        '/register_student_attendance': ft.View(
            route='/register_student_attendance',
            controls=[
                RegisterStudentAttendance(page)
            ]
        ),
        '/student_attendance': ft.View(
            route='/student_attendance',
            controls=[
                StudentAttendance(page)
            ]
        )
    }