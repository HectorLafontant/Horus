import flet as ft
from routes import router_handler

def main(page: ft.Page):

    def route_change(route):
        page.title = "HORUS"
        page.theme_mode = "dark"
        page.views.clear()
        page.views.append(
            router_handler(page)[page.route]
        )
    
    page.on_route_change = route_change
    page.go('/')

ft.app(target=main)