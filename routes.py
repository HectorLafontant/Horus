import flet as ft
from views.main_menu import MainMenu
from views.register_student import RegisterStudent

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
      )
    }