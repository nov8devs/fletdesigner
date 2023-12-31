import flet as ft


class ToolbarItem(ft.UserControl):
    def __init__(self, text, widget):
        self.text = text
        self.selected = False
        self.widget = widget
        # the names of the control to display in the toolbar
        self.container = ft.Container(
            bgcolor=ft.colors.with_opacity(color=ft.colors.BLACK38, opacity=0.2),
            height=40,
            border_radius=12,
            clip_behavior=ft.ClipBehavior.HARD_EDGE,
            padding=ft.padding.all(1),
            animate=200,
            alignment=ft.alignment.center,
            content=ft.Text(
                value=self.text,
                size=16,
                style=ft.TextStyle(weight=ft.FontWeight.W_900, font_family="Hack"),
                text_align=ft.TextAlign.JUSTIFY,
            ),
        )
        super().__init__()

    def build(self):
        self.toolbaritem = ft.Draggable(
            group="widget",
            content_feedback=ft.Container(
                width=20,
                height=20,
                content=ft.Icon(name=ft.icons.ADD, color=ft.colors.GREEN),
                margin=ft.margin.only(left=140),
            ),
            content=self.container,
        )
        return self.toolbaritem

    def add_selectionchanged_callback(self, callback):
        self.container.on_click = callback
