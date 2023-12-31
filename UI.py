import flet as ft
from time import sleep


from UI.animationpage import __view__
from DesignPage import DesignPage


def main(page: ft.Page):
    page.window_height = 800
    page.window_height = 800
    page.go("/welcome")

    def routechange(e: ft.RouteChangeEvent):
        # if page.route == "/welcome":
        #     page.views.clear()
        #     index = __view__()
        #     page.views.append(index.build())
        #     page.update()
        #     sleep(1)
        #     index.randomize("None")
        #     sleep(1)
        #     index.assemble("None")
        #     sleep(2.5)

        # page.window_maximized = True
        page.go(route="/design")
        if page.route == "/design":
            design_page = DesignPage()
            page.views.clear()
            page.update()
            # page.window_full_screen = True
            sleep(0.3)
            page.views.append(design_page.build())
            page.update()
            # design_page.bringintoview()
            page.update()

    page.bgcolor = ft.colors.BLACK
    page.on_route_change = routechange

    page.update()


if __name__ == "__main__":
    ft.app(main)
