import flet as ft
from views.routes import router

def main(page: ft.Page):

    page.theme_mode = "dark"
    page.on_route_change = router.route_change
    router.page = page
    page.add(
        router.body
    )
    page.go('/')

ft.app(target=main, assets_dir="assets")